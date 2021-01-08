I continue to reinvent the wheel.

Since freshdesk can't handle schedules and un-assign tickets properly...

Since Azure can't handle "az vm auto-shutdown" without webhooks...

This, sort-of middleware, growth.
Currently this middleware:
- store department's schedule and vm list in MySQL database
- enables auto-shutdown for engineers on a shift
- unassing tickets in freshdesk after the shift


# az-autoshutdown for Python3
Alternative solution for for "az vm auto-shutdown"

"az vm auto-shutdown -g MyResourceGroup -n MyVm --time 1730" works like a charm untill you should notify someone via email about VM shutdown. Notifications are enabled **only** if webhook is specified.

This script **az-autoshutdown.py** provides AzureCP-like experience. In this version I have a schedule and the list of emails in DB when VM should go down.

**Prerequirements:**
- Azure CLI (https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-yum?view=azure-cli-latest)
- (sudo) pip3 install pymysql

**Thanks to:**
The script is based on the Solution for PowerShell from https://gallery.technet.microsoft.com/scriptcenter/Enable-or-disable-auto-c7837c84


# Unassign.py for Python3
**Script logic:** After 'Auto-Shutdown' time (11 PM and 8 AM) for every shift VM status is verified for every engineer who had a shift. If an engineer's VM is deallocated, then the script un-assign tickets from en engineer to nobody.

Usage "python3 unassign.py D" or "python3 unassign.py N" - for Day and Night shift respectively

It makes sense to add commands to crontab

Script logs it's actions in /home/username/az-log/ folder, log name unassign.log-*
Log level might be decreased by commenting/removing print()


# Database
Solution relys on MySQL Database (any DB can be used)

    CREATE DATABASE <db_name>;
    GRANT ALL PRIVILEGES ON *.* TO '<db_user>' @'%';
    
    CREATE TABLE staff (
    vm_name VARCHAR(30) PRIMARY KEY NOT NULL,
    email VARCHAR(50) NOT NULL,
    team_name VARCHAR(30) NOT NULL,
    as_enabled VARCHAR(1),
    flag VARCHAR(30),
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
    
    create table schedule (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(30) NOT NULL,
    dow INT(1),
    shift VARCHAR(1),
    as_time INT(4),
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    );
 
Freshdesk requires 'AgentID', this value is stored in 'staff' table, column 'flag'
