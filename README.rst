ArGUI
=====

GUI for scripts using argparse

Argument Value Precendence Order
--------------------------------

The assumed precendence of argument values is as follows. The lowest number
wins, falling back to the next number and so on.

    1. GUI
    2. Command Line
    3. Environment Variables
    4. Configuration File
        4-1. Local Directory
        4-2. Home Directory
        4-3. System Directory
    5. Script's Defaults

ArgParse Features Supported
---------------------------


ArgParse Features In-Work
-------------------------

* bool (check box)
* int (spin box)
* float (text box)
* str (text box)
* choices (drop-down)
* file (file chooser)
* directory (directory chooser)
* list of all the above
* count (i.e. -vvv, spin box)
* argument groups (tabs?)
* subparsers/commands (drop-down)
* mutually exclusive (radio buttons)

ArGUI Features In-Work
----------------------

* Save/restore last settings
* Save/restore to/from arbitrary or script's assocaited configuration file

ArGUI Backends
--------------

* Tkinter
* PyQt5
* wxPython
