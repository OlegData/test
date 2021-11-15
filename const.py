# List of command const
C_CREATE = 'CREATE'
C_MOVE = 'MOVE'
C_LIST = 'LIST'
C_DELETE = 'DELETE'
C_HELP = 'HELP'
C_EXIT = 'EXIT'

# Hint messages
HINT = "Enter one of command CREATE/DELETE/LIST/MOVE/EXIT/HELP"

# Error message
E_FILE_NAME = "Incorrect file name"
E_COMMAND = "Incorrect command"

# Help message
HELP = """ This is program let a user create, move, delete the directory and show list of directories
If you enter as a second parameter the file name with commands the program is executed thais file.
If you execute the program without of a parameter you will open command string where you ought to enter command.
"""

HELP_CREATE = """CREATE [path]/dir
    Command CREATE creates directory in the path 
    For example:
        CREATE foo, or 
        CREATE data/foo
"""

HELP_MOVE = """MOVE [path]/dir [path]
    Command MOVE moves directory from the path to other path 
    For example:
        MOVE  foo data, or 
        MOVE data/foo fruits
"""

HELP_DELETE = """DELETE [path]/dir [path]
    Command DELETE deletes the directory   
    For example:
        DELETE  foo, or 
        DELETE data/foo
"""

HELP_LIST = """ LIST [path]
    Command LIST shows the directories  
    For example:
        LIST  foo, or 
        LIST data/foo
"""
HELP_PARAM = """Program name [file name]
"""