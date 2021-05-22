# probeKit
A simple tool written in Python for basic reconnaissance

# Requirements:

Python: `3.x`, Python `3.x` compatible pip, nmap, python-scapy, python-nmap

OS: Unix based operating system(macOS, Linux, etc.)

Not yet tested no DOS systems

# Installation
This toolkit does not require any extra configurations as it is a basic plug'n'play toolkit.

## Debian/Ubuntu ##

```
sudo apt install nmap
git clone https://github.com/theEndurance-del/probeKit.git
pip install -r requirements.txt
```

## ArchLinux ##

```
sudo pacman -Sy nmap
git clone https://github.com/theEndurance-del/probeKit.git
pip install -r requirements.txt
```

# Customization

This toolkit has it's own default set of colors.

```
red => Alerts or critical points
yellow => warnings or significant changes
green => successfull result or helpful text
blue => default prompt color
```

If the user feels to customize the colors for themselves please edit `colors.py` file.

# Usage:
Start the interpreter by typing the following in your terminal:
`python ./probeKit/interpreter.py`

To use a module simply type:
`use [module]`

Once into the module's interpreter the shell will display the module's name.

To know about the options available with the module simply type `options` in the interpreter shell.

To know about the configured options for a module or to check assigned values to available options type `info` in the interpreter

To assign value to an available option:
`set [OPTION] [VALUE]`

To run the module simply type `run`

*Note: This project is still not completed as a whole and still requires a lot of rewriting any suggestions for improvement are kindly accepted but may require some time to be worked upon*

## Thank You!! ##
