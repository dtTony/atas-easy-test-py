import time


class TimeUtil:
    @staticmethod
    def get_current_time():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

