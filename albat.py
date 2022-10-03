from psutil import sensors_battery
from time import sleep
import chime
from plyer import notification
import csv


def alarm_sound() -> None:
    chime.theme('zelda')
    chime.success()


def alarm_view() -> None:
    notification.notify(
        title="Alarm-warning",
        message="акамулятор разряжен",
        timeout=20
    )


def read_csv() -> None:
    with open("customiz.csv", encoding="utf-8") as file:
        file_rider = csv.reader(file, delimiter=";")
        for row in file_rider:
            print(row)


def battery() -> None:
    battery: tuple = sensors_battery()
    if not battery[2]:
        battery = sensors_battery()[0]
        if 30 < battery < 50:
            sleep(60 * 2)
            battery = sensors_battery()[0]
            while battery > 22:
                # print(strftime("%H:%M:%S", gmtime()))
                # print(f' timer two = ', battery)
                sleep(60)
                battery = sensors_battery()[0]
            alarm_view()
            alarm_sound()
        else:
            print("battery's level anymore 50% ")
            exit()
    else:
        print("The noteboook is connect to networks")
        exit()


if __name__ == "__main__":
    battery()

