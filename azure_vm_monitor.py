import subprocess
import smtplib
import logging
from email.mime.text import MIMEText
from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient

# ----------------------------
# CONFIGURATION
# ----------------------------

SUBSCRIPTION_ID = "63e7eab5-570c-479b-a496-220ebb0f3b07"

SENDER_EMAIL = "rizwansiddiqui483@gmail.com"
RECEIVER_EMAIL = "rizwansiddiqui483@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
APP_PASSWORD = "cztbhymmxbacthzk"

# ----------------------------
# LOGGING
# ----------------------------

logging.basicConfig(
    filename="vm_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# EMAIL FUNCTION
# ----------------------------

def send_email(message):

    msg = MIMEText(message)
    msg["Subject"] = "Azure VM Monitoring Alert"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()

        logging.info("Email alert sent successfully")
        print("Email alert sent!")

    except Exception as e:
        logging.error(f"Email sending failed: {e}")
        print("Email failed:", e)


# ----------------------------
# AZURE AUTHENTICATION
# ----------------------------

credential = AzureCliCredential()

compute_client = ComputeManagementClient(
    credential,
    SUBSCRIPTION_ID
)

# ----------------------------
# VM MONITORING
# ----------------------------

def check_vms():

    stopped_vms = []

    for vm in compute_client.virtual_machines.list_all():

        resource_group = vm.id.split("/")[4]

        instance_view = compute_client.virtual_machines.instance_view(
            resource_group,
            vm.name
        )

        for status in instance_view.statuses:

            if "PowerState/deallocated" in status.code:

                stopped_vms.append({
                    "name": vm.name,
                    "resource_group": resource_group,
                    "location": vm.location
                })

    return stopped_vms


# ----------------------------
# MAIN PROGRAM
# ----------------------------

print("Starting Azure VM Monitoring...")

vms = check_vms()

if not vms:

    print("No stopped VM found")
    logging.info("No stopped VM found")

else:

    message = "Stopped Azure VMs Detected\n\n"

    for vm in vms:

        message += f"""
VM Name: {vm['name']}
Resource Group: {vm['resource_group']}
Location: {vm['location']}

"""

    print(message)

    send_email(message)