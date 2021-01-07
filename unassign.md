Script logic:
After 'Auto-Shutdown' time (11 PM and 8 AM) for every shift VM status is verified for every engineer who had a shift. If an engineer's VM is deallocated, then the script un-assign tickets from en engineer to nobody.

Usage "python3 unassign.py D" or "python3 unassign.py N" - for Day and Night shift respectively

It makes sense to add commande to crontab

Script logs it's actions in /home/username/az-log/ folder, log name unassign.log-*

Log level might be decreased by commenting/removing print()

Freshdesk requires 'AgentID', this value is stored in 'staff' table, column 'flag'
