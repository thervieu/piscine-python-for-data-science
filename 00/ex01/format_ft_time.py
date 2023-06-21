import datetime

now = datetime.datetime.now()
timestamp = now.timestamp()
print("Seconds since January 1, 1970: {:,} or {:.2e} in scientific notation".format(timestamp, timestamp))
print(now.strftime("%B %d %Y"))