# login-counter-test-task
Parse syslog for number of failed logins

## Task

We want to collect the number of failed logins in the last hour. Here's how to do this using journalctl:

```
$ journalctl -l SYSLOG_FACILITY=10 --priority=5 --since "1 hour ago" --no-pager
-- Logs begin at Fri 2019-03-08 00:05:21 PST, end at Fri 2019-03-08 03:31:14 PST. --
Mar 08 03:31:12 wott0 sshd[4698]: pam_unix(sshd:auth): check pass; user unknown
Mar 08 03:31:12 wott0 sshd[4698]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=192.168.x.y
```

In the above example, the result should be 1.

Please use the Python module (https://www.freedesktop.org/software/systemd/python-systemd/journal.html) rather than trying to read this from disk is required.
