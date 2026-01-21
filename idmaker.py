def make_userid(name: str) -> str:
    """Given a NAME in last-name-first format, create and return a 
        Converse-style user ID."""
    # Split off the last name
    parts = name.split(',') # Note there may not be just two items in the list
    lastname = parts[0]
    othernames = parts[-1]

    # Clear the last name of characters we don't want to include
    badchars = " '"
    for c in badchars:
        lastname = lastname.replace(c, '')

    # Get the first two initials
    parts = othernames.split()
    initials = ''
    for i in range(min(2, len(parts))):
        initials = initials + parts[i][0]

    # Put it all together
    id = (initials + lastname + '001').lower()
    return id

def main(args: list[str]) -> int:
    raw_name = input('Please enter a full name, last name first, separated by a comma: ')
    print(f'The user id for the name "{raw_name}" is', end=' ')
    print(f'"{make_userid(raw_name)}"')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
