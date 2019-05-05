import unittest
from unittest import mock


from login_counter.adapters import SystemJournalAdapter
from login_counter.extractors import FailedLoginExtractor


class TestFailedLoginExtractor(unittest.TestCase):
    '''Test for the extractor of number of failed logins in the last hour'''

    def test_no_failed_logins(self):
        with mock.patch(
            'login_counter.adapters.SystemJournalAdapter.logins_last_hour',
            return_value=[]
        ):
            self.assertEqual(
                FailedLoginExtractor(adapter=SystemJournalAdapter).count(),
                0
            )

    def test_failed_logins(self):
        with mock.patch(
            'login_counter.adapters.SystemJournalAdapter.logins_last_hour',
            return_value=[
                (
                    'pam_unix(login:auth): authentication failure; '
                    'logname=LOGIN uid=0 euid=0 tty=/dev/tty1 '
                    'ruser= rhost=  user=rombr'
                ),
                (
                    "FAILED LOGIN (1) on '/dev/tty1' FOR 'rombr', "
                    "Authentication failure"
                ),
                (
                    'Operator of unix-session:3 successfully authenticated as '
                    'unix-user:rombr to gain ONE-SHOT authorization '
                    'for action org.freedesktop.udisks2.ata-smart-update '
                    'for system-bus-name::1.76 [psensor] '
                    '(owned by unix-user:rombr)'
                ),
            ]
        ):
            self.assertEqual(
                FailedLoginExtractor(adapter=SystemJournalAdapter).count(),
                1
            )
