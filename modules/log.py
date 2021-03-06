"""
***************************************************************************
Class File:             Runconfig Log Module
Authors/Maintainers:    Rich Nason (rnason@appcontainers.io)
Copyright:              Copyright 2016 Richard Nason
Description:            This class will provide very basic logging capabilities.
***************************************************************************
"""
# *******************************************************************
# Required Modules:
# *******************************************************************
import os  # Used for various os level calls
import datetime  # Used for timestamp

# *******************************************************************
# Class Definitions:
# *******************************************************************


class Log():
    """This module will handle logging config info to the console and to the logfile"""

    def __init__(self):
        """Set instantiation variables"""
        self.date = datetime.datetime.now()
        self.date = str(self.date)
        self.log_path = "/var/log/docker/"
        self.log_filename = "install.log"
        self.log_file = os.path.join(self.log_path, self.log_filename)

        if not os.path.isdir(self.log_path):
            os.makedirs(self.log_path)

    def write_log(self, msg):
        """Write sent message to logfile"""
        try:
            with open(self.log_file, 'a') as log:
                log.write(self.date + " : " + msg + "\n")
                log.close()
        except Exception as e:
            print("Failed to write to " + self.log_file + "\n")
            print(e)

    def write_log_console(self, msg1, msg2):
        """Write the sent messages to the log and to the console"""
        print("\n")
        print("**************************************************")
        print(msg1)
        print(msg2)
        print("**************************************************")
        print("\n")

        try:
            with open(self.log_file, 'a') as log:
                log.write("\n")
                log.write("**************************************************\n")
                log.write(self.date + " : " + msg1 + "\n")
                log.write(self.date + " : " + msg2 + "\n")
                log.write("**************************************************\n")
                log.write("\n")
                log.close()
        except Exception as e:
            print("Failed to write to " + self.log_file + "\n")
            print(e)

    def step_complete(self):
        """Echo that the step has completed."""
        try:
            with open(self.log_file, 'a') as log:
                print("Complete")
                log.write(self.date + " : Complete\n")
                log.close()
        except Exception as e:
            print("Failed to write to " + self.log_file + "\n")
            print(e)
