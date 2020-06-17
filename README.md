# az-autoshutdown
Alternative solution for for "az vm auto-shutdown"

"az vm auto-shutdown ..." can enable notification via e-mail only if webhook is specified.
this script provides AzureCP-like experience.

Here we have a schedule in DB when VM should go down.

The script is based on the Solution for PowerShell from https://gallery.technet.microsoft.com/scriptcenter/Enable-or-disable-auto-c7837c84
