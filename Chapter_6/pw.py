#! python3
# pw.py - An insecure password locker program.

# Password dictionary to store passwords
PASSWORDS = {'email' : 'th1s1smyp455w0rd',
            'blog' : 'th1st001sm1n3',
            'luggage' : '12345'}

# Handle command line arguments
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # First command line arg is the account name

# Copy the right password
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named' + account)
