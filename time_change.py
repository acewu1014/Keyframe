from datetime import datetime, timedelta

def milisec(timestamp):
    time = datetime.strptime(timestamp,"%H:%M:%S.%f")
    minutes = time.hour*60
    seconds = (minutes + time.minute) * 60
    miliseconds = (seconds + time.second)*1000 + time.microsecond/1000

    return miliseconds