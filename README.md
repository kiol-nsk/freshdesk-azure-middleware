I continue to reinvent the wheel.

Since freshdesk can't handle schedules and un-assign tickets properly
Since Azure can't handle "az vm auto-shutdown" without webhooks...

This, sort-of middleware, growth.
Currently this middleware:
- store department's schedule and vm list in MySQL database
- enables auto-shutdown for engineers on a shift
- unassing tickets in freshdesk after the shift

Each script has separate README
