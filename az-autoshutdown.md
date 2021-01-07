# az-autoshutdown for Python3
Alternative solution for for "az vm auto-shutdown"

"az vm auto-shutdown -g MyResourceGroup -n MyVm --time 1730" works like a charm untill you should notify someone via email about VM shutdown. Notifications are enabled only if webhook is specified.

This script **az-autoshutdown.py** provides AzureCP-like experience. In this version I have a schedule and the list of emails in DB when VM should go down.

**Prerequirements:**
- Azure CLI (https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest)
- (sudo) pip3 install pymysql

**Thanks to:**
The script is based on the Solution for PowerShell from https://gallery.technet.microsoft.com/scriptcenter/Enable-or-disable-auto-c7837c84
