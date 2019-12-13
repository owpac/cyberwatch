class Options:
    """
    Configuration file.
    """

    SHODAN_API = "yQYeEjecPKAO0rNsxKUL2ahXsnBHOf0a"

    DIR = './reports'

    INDENT = ' ' * 2
    LIST_SUB = INDENT + "> "
    LIST_TITLE = "[+] "
    LIST_INFO = "[i] "
    LIST_ERROR = "[!] "

    SAMPLE = """
Type python3 cyberwatch.py -h to show help.

Command line examples:
    1- Get information about:
        - API : python3 cyberwatch.py -I api
        - Protocols : python3 cyberwatch.py -I protocols
        - Services : python3 cyberwatch.py -I services
    
    2- Get info about host and save it in a file:
        python3 cyberwatch.py -H [host] -s
        
    3- Get info about host and compare it with a baseline file:
        python3 cyberwatch.py -H [host] -c
        
    4- Print and save:
        python3 cyberwatch.py -H [host] -ps
    
    5- Print and compare.
        python3 cyberwatch.py -H [host] -pc
    """
