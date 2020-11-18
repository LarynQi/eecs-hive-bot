import urllib.request
import urllib.parse
import ssl
import time
from datetime import datetime, timezone

PORTS = [8000, 8080, 5000, 3000]
UNAVAILABLE = [16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
hive_url = "http://hive{!s}.cs.berkeley.edu:{!s}/{!s}"
fmt = '%Y-%m-%d %H:%M:%S %Z%z'
msg = "hello-fellow-61c-student!/let-me-know-if-you-saw-this-message-by-emailing-me-at/laryn@berkeley.edu/:D"

def main():
    ssl._create_default_https_context = ssl._create_unverified_context
    machines = [n for n in range(1, 31)]
    response = None
    for m in UNAVAILABLE:
        machines.remove(m)
    count = 1
    while True:
        for m in machines:
            for p in PORTS:
                url = hive_url.format(m, p, msg)
                try:
                    response = urllib.request.urlopen(url)
                    # https://stackoverflow.com/questions/25837452/python-get-current-time-in-right-timezone
                    utc_dt = datetime.now(timezone.utc)
                    dt = utc_dt.astimezone()
                    print(f"Successful Connection #{count}: {hive_url.format(m, p, str())} at {dt.strftime(fmt)}")
                    count += 1
                except Exception as e:
                    print(hive_url.format(m, p, str()), e)
                    pass
                time.sleep(1)

if __name__ == "__main__":
    main()