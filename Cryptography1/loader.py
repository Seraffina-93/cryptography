import time
import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s %s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def loading():
    total = 100
    i = 0
    while i <= total:
        progress(i, total, status='Encrypting and Decrypting...')
        time.sleep(0.1)  # emulating loading
        i += 1
