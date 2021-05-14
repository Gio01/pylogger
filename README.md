<h1>Pylogger: Keylogger & Detector</h1>

The idea behind making this project is to learn some hacking techniques and understand how they work.
Currently Pylogger contains a basic Keylogger implementation that can successfully record keystrokes.

In addition there is a basic Keylogger Detector for the same Keylogger attack implemented in Pylogger. 
This KLDetector is able to find the process of the Keylogger running and is able to kill it to ensure that keystrokes are not recorded.

(Pylogger is developed for Linux.)


# Running Pylogger:

To run the logger, you need to run: 

> sudo python3 logger.py


While logger.py is running you can run the detector by running: 

> sudo python3 kldetect.py


Why Sudo?
> For the logger, the keyboard module needs sudo because it needs to access raw device files which are located at 
	/dev/input/input* but to access this file requires you to be root. (root is part of the sudo group so can simply 
	use the sudo command) The reason for having done it this way is that we are not dependent on the X server Linux
	to get access to the input devices.

> For the kldetect, it requires you to be sudo because when we run the logger, we are running it with sudo. That means
	that it has higher privileges than we currently have and will get a 'Operation not permitted' error unless if 
	we kill the process with sudo privileges.  
