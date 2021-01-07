import datetime
import random


def getHourStr(timeDelta: datetime.timedelta):
    timeDelta_seconds = timeDelta.seconds
    hours = timeDelta_seconds//3600
    minutes = (timeDelta_seconds//60) % 60
    seconds = timeDelta_seconds % 60
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)



startYear = datetime.datetime.now().year
startMonth = datetime.datetime.now().month
deltaoneDay = datetime.timedelta(1)
try:
    file = open("LAGC_{:02}_{:04}.csv".format(startMonth, startYear), 'w')
except FileNotFoundError:
    file = open("LAGC_{:02}_{:04}.csv".format(startMonth, startYear), 'x')

date2iterate = datetime.date(startYear, startMonth, 1)
while True:
    lineText = f"{date2iterate.day},"
    if not (date2iterate.weekday() == 5 or date2iterate.weekday() == 6):
        randomMinutes = random.randrange(-5, 5)
        initialHour = datetime.timedelta(hours=9, minutes=randomMinutes)
        del randomMinutes
        if not date2iterate.weekday() == 4:
            # Hora de entrada
            lineText += f"{getHourStr(initialHour)},"
            # Salida para comer
            randomMinutes = random.randrange(320, 400)
            initialHour += datetime.timedelta(minutes=randomMinutes)
            lineText += f"{getHourStr(initialHour)},,"
            # Entrada de comer
            randomMinutes = random.randrange(50, 70)
            initialHour += datetime.timedelta(minutes=randomMinutes)
            lineText += f"{getHourStr(initialHour)},"
            # Hora de salida
            randomMinutes = random.randrange(-5, 5)
            initialHour += datetime.timedelta(hours=18, minutes=randomMinutes) - initialHour
            lineText += f"{getHourStr(initialHour)},"
        else:
            # Hora de entrada
            initialHour -= datetime.timedelta(hours=1)
            lineText += f"{getHourStr(initialHour)},"
            # Hora de salida
            randomMinutes = random.randrange(0, 10)
            initialHour += datetime.timedelta(hours=7, minutes=randomMinutes)
            lineText += f"{getHourStr(initialHour)},,,,"
    else:
        lineText += ",,,,,"
    # New Line
    lineText += "\n"
    file.write(lineText)
    date2iterate += deltaoneDay

    if not date2iterate.month == startMonth:
        break
