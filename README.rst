pyserial_utils
==============


A set of utilities based on pyserial to identify usable serial ports
and to check, create and delete lock files in linux systems.

Usage
-----

in python

List device independent all available serial ports.
Takes care for lock files in linux Systems.

.. code:: python

   import pyserial_utils
   p = pyserial_utils.serial_ports()
   print(p)
   # gives e.g. on a Linux machine ['/dev/ttyACM0', '/dev/ttyS0']

   # Creating a lock file for port in /var/lock/LCK..ttyACM0
   # with the current PID
   serial_lock_file('/dev/ttyACM0')
   # Removes serial lock file
   serial_lock_file('/dev/ttyACM0',remove=True)
   # Tests a serial lock file, if no process with the PID was found
   # removing the lock file (brutal = True)
   test_serial_lock_file('/dev/ttyACM0',brutal = True)


	  

