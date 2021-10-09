# ----------------------------------------------------------------
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# ----------------------------------------------------------------

import re


def time_conversion(time):
    pattern = re.compile(r'(\d{2}):(\d{2}):(\d{2})([AP]M)$')
    converted = ''
    
    # print(pattern)
    h, m, s, am_pm = re.search(pattern, time).groups()
    if am_pm == 'AM' and h == '12':
        converted = re.sub(re.compile(r'^12'), '00', time)
        converted = re.sub(re.compile(r'AM$'), '', converted)

    elif am_pm == 'AM':
        converted = re.sub(re.compile(r'AM$'), '', time)

    elif am_pm == 'PM':
        h_p = re.compile(r'^\d{2}')
        h = str(int(re.match(h_p, time).group()) % 12 +12)
        converted = re.sub(r'^\d{2}', str.zfill(h, 2), time)
        converted = re.sub(r'PM$', '', converted)
    return converted

     



if __name__ == '__main__':
    test_times = ['12:00:05AM', '12:00:05PM', '05:00:00PM', '05:00:00AM','07:05:45PM']

    for time in test_times:
        print(f'Original Time: {time}')
        print (time_conversion(time))