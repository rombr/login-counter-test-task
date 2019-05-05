'''Extrat data'''


class FailedLoginExtractor(object):
    '''Get the number of failed logins in the last hour'''

    failed_login_pattern = 'authentication failure; logname='

    def __init__(self, adapter: object):
        self.adapter = adapter

    def count(self) -> int:
        '''Return the number of failed logins in the last hour'''
        failed_logins_count = 0
        for record in self.adapter.logins_last_hour():
            if self.failed_login_pattern in record:
                failed_logins_count += 1
        return failed_logins_count
