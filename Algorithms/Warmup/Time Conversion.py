import time

timedata = time.strptime(raw_input().strip(), '%I:%M:%S%p')
print time.strftime('%H:%M:%S', timedata)
