def validSSN(ssn: str) -> bool:
    """Return True if and only if SSN complies with the Social Security
        Administration's rules (found at 
        https://primepay.com/learn/payroll/how-to-determine-a-valid-social-security-number/)
        for a valid Social Security number."""
    valid = True
    # If it has dashes, there must be exactly 2 and they have to be in the correct places
    if '-' in ssn:
        if ((ssn.count('-') != 2) or (ssn[3] != '-') or (ssn[6] != '-')):
            valid = False
        ssn = ssn.replace('-','') # Take out the dashes, so the rest can deal just with digits
    # SSN is now dash-free.  It better have exactly 9 digits (and only digits)
    if (len(ssn) != 9) or (not ssn.isdigit()):
        valid = False
    elif ssn == '123456789':
        valid = False
    elif ssn[:3] == '000' or ssn[:3] == '666':
        valid = False
    elif ssn[:3] >= '773':
        valid = False
    elif ssn[3:5] == '00':
        valid = False
    elif ssn[5:] == '0000':
        valid = False
    return valid 

def main(args: list[str]) -> int:
    # Read a Social Security number from the keyboard
    ssn = input('Please enter a Social Security number: ')
    print('The SSN', ssn, end=' ')
    if validSSN(ssn):
        print('could be', end=' ')
    else:
        print('could NOT be', end=' ')
    print('a valid Social Security number.')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
