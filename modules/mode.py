"""Module to configure the container mode"""
# Import custom modules
import os  # Used for various os level calls
from modules.log import Log

# Instantiate the custom console logger.
config_logger = Log()


class Mode():
    """Class to configure the container mode"""

    def __init__(self):
        """Set instantiation variables"""
        # Get the OS version
        self.rhel_distro = False
        if os.path.isfile('/etc/redhat-release'):
            self.rhel_distro = True

        # Create a list of packages that get installed
        if self.rhel_distro:
            self.package_mgr = "yum -y erase"
            self.remove_pkgs = self.package_mgr + " %s"
            self.mysql_pkg = "mysql-server"
        else:
            self.package_mgr = "apt-get -y remove --purge"
            self.remove_pkgs = self.package_mgr + " %s" + "; apt-get -y autoremove"
            self.mysql_pkg = "mysql-server-5.5"

    def config_verif(self, checkfile):
        """Method to determine if the environment has already been configured, Returns True/False value"""
        if os.path.isfile(checkfile):
            config_logger.write_log_console("Existing $APPLICATION Instance detected..." "skipping...")
            return True
        else:
            return False

    def datavol(self, deplist):
        """Configure DataVol Mode"""
        # Log to console/logfile
        config_logger.write_log_console("Data Volume Mode Detected...", "Removing unnecessary packages...")

        # Remove unnecessary packages without yanking apache, and recreate rpm/yum sync
        os.popen(self.remove_pkgs % (deplist,))

        # Mark step complete
        config_logger.step_complete()
