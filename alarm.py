import datetime

class Alarm:

    def __init__(self,alarm_time, day):
        self.alarm_time = alarm_time
        self.day = day
        self.snooze_count = 0

    def snooze(self):
        if self.snooze_count < 3:
            self.alarm_time += datetime.timedelta(minutes=5)
            self.snooze_count += 1
            return True

        return False
    

class AlarmClock:

    def __init__(self):
        self.alarms = []
        self.current_time = datetime.datetime.now()
    
    def display_time(self):
        self.current_time = datetime.datetime.now()
        print(f"Current time: {self.current_time}")

    def add_alarm(self, alarm_time, day):
        
        self.alarms.append(Alarm(alarm_time,day))
        print("New alarm added")
    
    def delete_alarm(self, alarm_time, day):
        for alarm in self.alarms:
            if alarm.alarm_time == alarm_time and alarm.day_of_week == day:
                self.alarms.remove(alarm)
                print("Alarm deleted")
                return
    
    def snooze_alarm(self,alarm_time,day):
        for alarm in self.alarms:
            if alarm.alarm_time == alarm_time and alarm.day == day:
                if alarm.snooze():
                    print("Alarm snoozed")
                else:
                    print("Maximum snooze limit reached")
                return
        print("Alarm not found")

alr = AlarmClock()
alr.display_time()
alr.add_alarm((datetime.datetime.now() + datetime.timedelta(seconds=30)), 'Friday')
alr.add_alarm((datetime.datetime.now() + datetime.timedelta(minutes=1)), 'Friday')