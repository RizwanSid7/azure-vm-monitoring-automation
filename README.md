Below is a \*\*more professional, recruiter-ready README.md\*\* for your GitHub project.

You can \*\*copy this completely into your `README.md` file\*\*.



It includes:



\* Clear project objective

\* Architecture explanation

\* Step-by-step setup

\* Troubleshooting

\* Commands used

\* Best practices

\* Future improvements



This is written like a \*\*real DevOps project documentation\*\*.



\---



\# Azure VM Monitoring Automation



\## Project Overview



This project demonstrates how to build a \*\*production-style Azure VM monitoring automation system\*\* using Python and Azure APIs.



The script continuously monitors all Virtual Machines within an Azure subscription and automatically detects any \*\*stopped or deallocated VMs\*\*. When such VMs are detected, the system sends an \*\*email alert notification\*\* to administrators.



This project simulates a \*\*real-world cloud operations monitoring workflow\*\* used by Cloud Engineers and DevOps teams.



The automation runs every \*\*5 minutes using Windows Task Scheduler\*\*, ensuring continuous monitoring without manual intervention.



\---



\# Technologies Used



| Technology             | Purpose                                 |

| ---------------------- | --------------------------------------- |

| Python                 | Automation scripting                    |

| Azure CLI              | Authentication with Azure               |

| Azure SDK for Python   | Access Azure resources programmatically |

| SMTP                   | Email alert notifications               |

| Windows Task Scheduler | Automated execution                     |

| Git                    | Version control                         |

| GitHub                 | Code hosting and documentation          |



Key Python Libraries:



\* azure-identity

\* azure-mgmt-compute

\* smtplib

\* logging



\---



\# Project Architecture



```

Azure Subscription

&#x20;       │

&#x20;       │

Python Monitoring Script

&#x20;       │

&#x20;       │

Azure SDK Authentication (Azure CLI)

&#x20;       │

&#x20;       │

Retrieve VM List

&#x20;       │

&#x20;       │

Check VM Power State

&#x20;       │

&#x20;┌───────────────┐

&#x20;│               │

Running       Stopped

&#x20;│               │

&#x20;│         Send Email Alert

&#x20;│               │

&#x20;│         Log Event

&#x20;│

Continue Monitoring

```



\---



\# Project Features



\* Monitors \*\*all virtual machines in Azure subscription\*\*

\* Detects \*\*Stopped / Deallocated VM states\*\*

\* Sends \*\*automated email alerts\*\*

\* Logs monitoring results into log files

\* Runs automatically every \*\*5 minutes\*\*

\* Uses \*\*secure Azure authentication\*\*

\* Built using \*\*Azure Python SDK\*\*



\---



\# Use Case



In production cloud environments, organizations may have hundreds of virtual machines running across multiple regions.



Manual monitoring is inefficient.



This project demonstrates how DevOps engineers can automate monitoring to:



\* Detect downtime quickly

\* Alert operations teams

\* Reduce manual effort

\* Improve system reliability



\---



\# Prerequisites



Before running this project ensure the following tools are installed.



\### Install Python



Download from:



\[https://www.python.org/downloads/](https://www.python.org/downloads/)



Verify installation:



```

python --version

```



\---



\### Install Azure CLI



Download from:



\[https://learn.microsoft.com/en-us/cli/azure/install-azure-cli](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)



Verify installation:



```

az version

```



\---



\### Install Required Python Libraries



Run the following command:



```

pip install azure-identity

pip install azure-mgmt-compute

pip install azure-mgmt-resource

pip install smtplib

```



\---



\# Authentication with Azure



Login to Azure using CLI:



```

az login

```



If Multi-Factor Authentication is required:



```

az login --scope https://management.azure.com/.default

```



Verify subscription:



```

az account show

```



\---



\# Project Structure



```

azure-vm-monitor

│

├── azure\_vm\_monitor.py

├── vm\_monitor.log

├── README.md

├── .gitignore

```



Explanation:



| File                | Purpose                  |

| ------------------- | ------------------------ |

| azure\_vm\_monitor.py | Main monitoring script   |

| vm\_monitor.log      | Execution logs           |

| README.md           | Project documentation    |

| .gitignore          | Ignore unnecessary files |



\---



\# Running the Script



Navigate to the project directory:



```

cd C:\\azure-vm-monitor

```



Run the script:



```

python azure\_vm\_monitor.py

```



Expected output example:



```

Starting Azure VM Monitoring...



Stopped Azure VMs Detected



VM Name: vm1-server

Resource Group: ssh-test-rg

Location: eastus



VM Name: vm2-client

Resource Group: ssh-test-rg

Location: eastus



Email alert sent!

```



If no stopped VMs are found:



```

Starting Azure VM Monitoring...

No stopped VM found

```



\---



\# Automating the Script (Every 5 Minutes)



To automate the monitoring system, Windows Task Scheduler was used.



Steps:



Open Task Scheduler



Create Basic Task



Set Trigger:



```

Repeat task every: 5 minutes

```



Set Action:



```

Program/script:

C:\\Users\\rizwa\\AppData\\Local\\Programs\\Python\\Python313\\python3.13t.exe

```



Add arguments:



```

C:\\azure-vm-monitor\\azure\_vm\_monitor.py

```



Now the monitoring script runs automatically every 5 minutes.



\---



\# Logging



The script generates a log file:



```

vm\_monitor.log

```



Logs include:



\* Script execution time

\* VM monitoring results

\* Errors and alerts



Example:



```

2026-05-20 14:35:02 Starting Azure VM Monitoring

2026-05-20 14:35:03 No stopped VM found

```



\---



\# Errors Encountered and Troubleshooting



During development several issues occurred.



\---



\### Azure Authentication Error



Error:



```

AADSTS50076: Multi-Factor Authentication required

```



Cause:



Azure tenant required MFA authentication.



Solution:



```

az login --scope https://management.azure.com/.default

```



\---



\### Azure CLI Session Expired



Error:



```

ClientAuthenticationError

```



Solution:



```

az logout

az account clear

az login

```



\---



\### Python Path Not Found



Command:



```

where python

```



Returned empty result.



Solution:



Find Python path using:



```

py -c "import sys; print(sys.executable)"

```



Result:



```

C:\\Users\\rizwa\\AppData\\Local\\Programs\\Python\\Python313\\python3.13t.exe

```



This path was used in Task Scheduler.



\---



\# Best Practices Implemented



\* Git version control

\* Log file monitoring

\* Error handling

\* Secure Azure authentication

\* Scheduled automation

\* Documentation



\---



\# Future Improvements



This project can be further improved by integrating additional Azure services.



Possible enhancements include:



\### Integration with Azure Monitor



Enable centralized monitoring and alerts.



\### Integration with Azure Logic Apps



Automate remediation workflows.



\### Integration with Azure Functions



Convert this monitoring script into a serverless architecture.



\### Integration with Terraform



Automate deployment of the monitoring system.



\### Slack / Microsoft Teams Alerts



Send notifications directly to DevOps channels.



\---



\# Learning Outcomes



Through this project the following concepts were implemented:



\* Azure SDK usage

\* Cloud infrastructure monitoring

\* Python automation

\* Task scheduling

\* Cloud authentication

\* DevOps project documentation

\* Troubleshooting cloud authentication errors



\---



\# Author



Rizwan Siddiqui



Cloud Engineer | DevOps Enthusiast



GitHub:



You can view the project repository on

GitHub



\---



