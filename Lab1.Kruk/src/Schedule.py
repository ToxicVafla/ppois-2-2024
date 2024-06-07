class Schedule:
    def __init__(self, action, scheduled_time):
        self.action = action
        self.scheduled_time = scheduled_time

    def is_time_to_run(self, current_time):
        return self.scheduled_time <= current_time

    def display_schedule(self):
        print("schedule info:", self.scheduled_time, self.action)
