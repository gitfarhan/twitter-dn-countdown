from datetime import datetime
from twitter_handler import update_displayname
import schedule
import time
from retry import retry

class CountDown:

    def __init__(self, end_date, menuju):
        self.end_date = end_date
        self.menuju = menuju

    def _get_countdown(self): 

        def date_diff_in_seconds(dt2, dt1):
            timedelta = dt2 - dt1
            return timedelta.days * 24 * 3600 + timedelta.seconds

        def dhms_from_seconds(seconds):
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            return (days, hours, minutes)

        #Specified date
        date1 = datetime.strptime(self.end_date, '%Y-%m-%d')

        #Current date
        date2 = datetime.now()

        days, hours, mins = dhms_from_seconds(date_diff_in_seconds(date1, date2))

        message = f"{days}days, {hours}hours, {mins}mins until {self.menuju}."
        return message

    @retry(tries=3, delay=5)
    def main_task(self):
        message = self._get_countdown()
        update_displayname(name=message)


if __name__ == "__main__":

    print(f"scheduler countdown is now running")

    def job():
        CountDown(end_date="2022-05-03", menuju="lebaran").main_task()

    schedule.every().minute.at(":00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)