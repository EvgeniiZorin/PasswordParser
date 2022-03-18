import pandas as pd
import colorama; from colorama import Style, Fore, Back; colorama.init(autoreset=True)


def parse_credentials(website_name: str, credentials_df: vars):
	"""
	Accesses information in the row where value for column Website is website_name.
	"""
	count = 0
	for iter, i in enumerate(credentials_df['Website']):
		if website_name.lower() in i.lower():
			print('--------------------------------------------------')
			print(credentials_df.loc[iter])
			print('--------------------------------------------------')
			count += 1
	return count

def print_password(website_name: str, credentials_df: vars):
	"""
	For a given value of Website, prints the corresponding value in the same row from the column Password.
	"""
	for iter, i in enumerate(credentials_df['Website']):
		if website_name.lower() in i.lower():
			return credentials_df.iloc[iter]['Password']
			# print(credentials_df.iloc[iter]['Password'])

def change_password(website_name: str, credentials_df: vars, new_value: str):
	"""
	For a given value of Website, find the corresponding value in the same row from the column Password and replace it with new_value. 
	"""
	for iter, i in enumerate(credentials_df['Website']):
		if website_name.lower() in i.lower():			
			credentials_df.iloc[iter]['Password'] = new_value
			new_var = credentials_df.iloc[iter]['Password']
	credentials_df.to_csv('Credentials.tsv', columns=['Website', 'Username', 'Email', 'Password', 'Notes'], index=False, sep="\t")
	return new_var

def add_new_website(website_add: str, username_add: str, email_add: str, pw_add: str, notes_add: str, credentials_df):
	# Check if website is already present
	for iter, i in enumerate(credentials_df['Website']):
		if website_add.lower() in i.lower():
			raise Exception("Value for website already present")
	credentials_df = credentials_df.append({'Website': website_add, 'Username': username_add, 'Email': email_add, 'Password': pw_add, 'Notes': notes_add}, ignore_index=True)
	credentials_df.to_csv('Credentials.tsv', columns=['Website', 'Username', 'Email', 'Password', 'Notes'], index=False, sep="\t")
	return credentials_df.iloc[-1]


if __name__ == "__main__":
	print(f"{Fore.GREEN}{Style.BRIGHT}Hello and welcome to my little program!")
	credentials_df = pd.read_csv('Credentials.tsv', delimiter='\t')

	while True:
		input_var = input(f"Please state which action you would like to perform on credentials - 'info', 'pw', 'change pw', 'add pw', or 'exit': ")
		if input_var == 'info':
			website_name = input("For which website you would like to view its credentials? ")
			count = parse_credentials(website_name, credentials_df)
			if count == 0:
				print(f"Website name not found!")
		elif input_var == 'pw':
			website_name = input("For which website you would like to view its password? ")
			print(f"Password for {website_name}: {print_password(website_name, credentials_df)}")
		elif input_var == 'change pw':
			try:
				website_name, new_password = input("Enter website name (var1) and new password (var2), e.g. 'Aeroflot, NewPassword' ").split(',')
				print(f"Old password for {website_name}: {print_password(website_name, credentials_df)}")
				print_new_password = change_password(website_name, credentials_df, new_password)
				print(f"New password for {website_name}: {print_new_password}")
				credentials_df = pd.read_csv('Credentials.tsv', delimiter='\t')
			except:
				print('Something went wrong, try again...')
		elif input_var in ['Exit', 'exit']:
			break
		elif input_var == 'add pw':
			website_add = input("Enter website name: ")
			username_add = input('Enter the username: ')
			email_add = input('Enter the email: ')
			pw_add = input("Enter the password: ")
			notes_add = input('Enter notes: ')
			# try: 
			new_pw_output = add_new_website(website_add, username_add, email_add, pw_add, notes_add, credentials_df)
			credentials_df = pd.read_csv('Credentials.tsv', delimiter='\t')
			# except: 
				# print('ERROR: Something went wrong, please try again')
			print(f"Added successfully! Please see details about the new entry below:\n{new_pw_output}")
		elif input_var not in ['info', 'pw', 'change pw', 'Exit', 'exit', 'add pw']:
			print('Argument not recognised, please try again...')

