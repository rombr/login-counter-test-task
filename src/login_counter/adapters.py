'''External adapters'''
import time

from systemd import journal


class SystemJournalAdapter(object):
    '''System journal reader'''

    @classmethod
    def logins_last_hour(cls) -> iter:
        '''Read journal logins in the last hour:
        journalctl -l SYSLOG_FACILITY=10 --priority=5
                   --since "1 hour ago" --no-pager
        '''
        reader = journal.Reader()
        reader.log_level(5)
        reader.add_match(SYSLOG_FACILITY=10)
        since_1_hour_ago = time.time() - 3600
        reader.seek_realtime(since_1_hour_ago)
        for entry in reader:
            yield entry['MESSAGE']


if __name__ == '__main__':
    for entry in SystemJournalAdapter.logins_last_hour():
        print(entry)
