# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

kb = (2 ** 10)
kB = (2 ** 10 * 8)
Mb = (2 ** 20)
MB = (2 ** 20 * 8)
Gb = (2 ** 30 )
GB = (2 ** 30 * 8)
Tb = (2 ** 40)
TB = (2 ** 40 * 8)


def convert_seconds(secs):
    hours =  int(secs/3600)
    secs = secs%3600
    minutes = int(secs/60)
    secs = float(secs%60)
    result = str(hours)
    if hours == 1:
        result = result+ ' hour, '
    else:
        result = result+ ' hours, '

    result = result + str(minutes)
    if minutes == 1:
        result = result+ ' minute, '
    else:
        result = result+ ' minutes, '

    result = result + str(secs)
    if secs == 1:
        result = result+ ' second'
    else:
        result = result+ ' seconds'
    return result


def download_time(file, file_form, band, band_form):
    time = 0
    if file_form == 'kb':
        file = file * kb
    elif file_form == 'kB':
        file = file *  kB
    elif file_form == 'Mb':
        file = file *  Mb
    elif file_form == 'MB':
        file = file *  MB
    elif file_form == 'Gb':
        file = file *  Gb
    elif file_form == 'GB':
        file = file *  GB
    elif file_form == 'Tb':
        file = file *  Tb
    elif file_form == 'TB':
        file = file *  TB
    else:
        return 'error'

    if band_form == 'kb':
        band = band *  kb
    elif band_form == 'kB':
        band = band *  kB
    elif band_form == 'Mb':
        band = band *  Mb
    elif band_form == 'MB':
        band = band *  MB
    elif band_form == 'Gb':
        band = band *  Gb
    elif band_form == 'GB':
        band = band *  GB
    elif band_form == 'Tb':
        band = band *  Tb
    elif band_form == 'TB':
        band = band *  TB
    else:
        return 'error'

    time = float(file / band)
    return convert_seconds(int(time))


print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print download_time(11,'GB', 5, 'MB')
