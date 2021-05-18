#! /usr/bin/env python3

# This is the data-information module which will print help for the interpreter and information about selected module

from colorama import Fore, Back, init

FGREEN = Fore.GREEN
FRED = Fore.RED
FWHITE = Fore.WHITE

# This class prints help for the interpreter
class Help():
	def __init__(self, MODULE):
		self.module = MODULE

	def showHelp(self):
		module = self.module
		
		# Checks whether the shell is module interpreter or module selector session
		if module == '':
			print(FGREEN+'\nUsage: [verb] [options]')
			print('Available verbs are: use, help, exit, terminate, clear\n')
			print('\t use\t\t specify a module to use\n\t\t\t | usage: use [module]\n')
			print('\t help\t\t prints this help message\n')
			print('\t list\t\t prints available modules\n')
			print('\t about\t\t prints details about specified module\n\t\t\t | Usage: about [moduleName]\n')
			print('\t exit\t\t exits the interpreter\n')
			print('\t terminate\t alias for exit\n')
			print('\t clear\t\t clears screen\n\t\t\t | usage: clear [option]\n\t\t\t | available options are: exit, terminate\n')

		else:
			print(FGREEN+'\nUsage: [verb] [options]')
			print('Available verbs are: set, help, exit, back, info, options, clear, getstat, run\n')
			print('\t options\t lists available options to configure\n')
			print('\t info\t\t shows values assigned to each option\n')
			print('\t set\t\t assignes values to available options\n\t\t\t | usage: set [option] [value]\n')
			print('\t help\t\t prints this help message\n')
			print('\t exit\t\t exits the whole interpreter\n')
			print('\t back\t\t moves back to the module selector\n')
			print('\t getstat\t prints the status of previous verb\n')
			print('\t clear\t\t clears screen\n')
			print('\t run\t\t runs the selected module\n')
			print('\t about\t\t prints details about specified module\n\t\t\t | Usage: about [moduleName]\n')
			print('\t list\t\t prints available modules\n')

# List available options for a selected module
class Options():
	def __init__(self, MODULE):
		self.module = MODULE

	def showOptions(self):
		module = self.module

		if module == 'probe':
			print(f'\n\t[*] LHOST => hosts ip4 address(required)(LHOST => lhost)')
			print(f'\t[*] LPORT => ports to scan on host(required)(LPORT => lport)')
			print(FRED+f'\t             | values can be set as [portnumber(single portscan)] or [startport/endport(multiple portscan)]\n')
			print(FWHITE+f'\t[*] PROTO => protocol to use for scanning(required)(PROTO => proto)')
			print(FRED+f'\t             | Available protocols: ')
			print(f'\t                                  | [TCP => tcp => TCP/IP => tcp/ip]')
			print(f'\t                                  | [UDP => udp]\n')
			print(FWHITE+f'\t[*] TMOUT => time to wait for incomming packet in seconds(set to \'1\' by default)(TMOUT => tmout)\n')

		elif module == 'osprobe':
			print(f'\n\t[*] LHOST => hosts ip4 address(required)(LHOST => lhost)')
			print(f'\t[*] TRYCT => number of tries to send the packet(set to \'1\' by default)(TRYC => tryc)\n')

		else:
			raise Exception(FRED+'Error: Invalid module')

# List values assigned to various options of the module
class Info():
	def __init__(self, MODULE, LHOST, LPORT, PROTOCOL, TIMEOUT, TRYCT):
		self.module  = MODULE
		self.lhost   = LHOST
		self.lport   = LPORT
		self.proto   = PROTOCOL
		self.timeout = TIMEOUT
		self.tryct = TRYCT

	def showInfo(self):
		if self.module == 'probe':
			if self.lhost != '':
				print(FGREEN+'\n\t[+] '+f'LHOST => {self.lhost}')
			else:
				print(FRED+'\n\t[-] '+f'LHOST => {self.lhost}')

			if self.lport != '':
				print(FGREEN+f'\t[+] '+f'LPORT => {self.lport}')
			else:
				print(FRED+'\t[-] '+f'LPORT => {self.lport}')

			if self.proto != '':
				print(FGREEN+'\t[+] '+f'PROTO => {self.proto}')
			else:
				print(FRED+'\t[-] '+f'PROTO => {self.proto}')

			print(FGREEN+f'\t[*] TMOUT => {self.timeout}\n')

		elif self.module == 'osprobe':
			if self.lhost != '':
				print(FGREEN+'\n\t[+] '+f'LHOST => {self.lhost}')
			else:
				print(FRED+'\n\t[+] '+f'LHOST => {self.lhost}')

			print(FGREEN+f'\t[*] TRYCT => {self.tryct}\n')

		else:
			raise Exception(FRED+'Error: Invalid module')