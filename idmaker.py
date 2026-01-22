from csv import DictReader, DictWriter

def name_to_dict(name: str) -> dict[str, str]:
    # Split off the last name
    parts = name.split(',') # Note there may not be just two items in the list
    lastname = parts[0]
    othernames = parts[-1]
    return {'lastname': lastname, 'othernames': othernames}

def make_userid(namedict: dict[str, str]) -> str:
    """Given a NAME in last-name-first format, create and return a 
        Converse-style user ID."""
    lastname = namedict['lastname']
    # If the name contains a comma, get rid of tha part from the comma to the end
    if ',' in lastname:
        lastname = lastname[:lastname.find(',')]

    othernames = namedict['othernames']

    # Clear the last name of characters we don't want to include
    goodchars = '-'
    for c in lastname:
        if not c.isalpha() and c not in goodchars:
            lastname = lastname.replace(c, '')

    # Get the first two initials
    parts = othernames.split()
    initials = ''
    for i in range(min(2, len(parts))):
        initials = initials + parts[i][0]

    # Put it all together
    id = (initials + lastname + '001').lower()
    return id

def runFromFiles(infile: str, outfile: str) -> None:
    names: list[dict[str, str]] = []
    with open(infile, 'r') as f:
        reader = DictReader(f)
        for row in reader:
            userdict = row.copy()
            userdict['userid'] = make_userid(row)
            names.append(userdict)

    with open(outfile, 'w', newline='') as f:
        writer = DictWriter(f, names[0].keys())
        writer.writeheader()
        writer.writerows(names)

def main(args: list[str]) -> int:
    infilename = input('Please enter the name of the CSV file to read from: ')
    outfilename = input('Please enter the name of the CSV file to output to: ')
    runFromFiles(infilename, outfilename)
    # raw_name = input('Please enter a full name, last name first, separated by a comma: ')
    # print(f'The user id for the name "{raw_name}" is', end=' ')
    # print(f'"{make_userid(name_to_dict(raw_name))}"')
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
