# Cyberwatch
Search host and save results in a file or a Google Sheet.

# Installation

### 1. Clone the repo

```
$ git clone https://github.com/Owpac/cyberwatch
```

### 2. Create venv and install requirements

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### 3. Use it !

# How it work

To see help and examples:
```
$ python3 cyberwatch.py -h
```


Use examples:

1. Get information about:
  - API: ```$ python3 cyberwatch.py -I api```
  - Protocols: ```$ python3 cyberwatch.py -I protocols```
  - Services: ```$ python3 cyberwatch.py -I services```
  
2. Get info about host and print the output on console.

```$ python3 cyberwatch.py -H [host] -p```

3. Get info about host and save it in a file.

```$ python3 cyberwatch.py -H [host] -s```

4. Get info about host and compare it with a baseline file.

```$ python3 cyberwatch.py -H [host] -c```

> /!\ Before executing this command, you need to save a file which will be your baseline for teh comparison.

5. You can combine some options: 

```
$ python3 cyberwatch.py -H [host] -ps
$ python3 cyberwatch.py -H [host] -pc
```

> /!\ You can't combine options -s and -c.

6. You can change some configuration option in options.py:

For example, if you want to change some output format, modify ```LIST_SUB``` variable with another character.

