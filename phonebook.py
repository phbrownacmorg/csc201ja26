def make_phonebook() -> dict[str, dict[str, str]]:
    book: dict[str, dict[str, str]] = {}
    entries: tuple[tuple[str, str], ...] = (('Peter Brown', '9156'),
                ('Joseph Barrera', '9128'), ('Amanda Mangum', '9127'), 
                ('Jessica Sorrells', '9149'), ('Scott Robbins', '9021'),
                ('Laura Feitzinger Brown', '9690'), ('Jennifer Hawk', '9402'),
                ('Edward Woodfin', '9102'))
    for entry in entries:
        nameparts = entry[0].split()
        ext = entry[1]
        d = {'name': entry[0], 'firstname': nameparts[0], 
             'lastname': nameparts[-1], 'number': '864.596.' + ext }
        book[d['lastname'] + ', ' + d['firstname']] = d

    book['Brown, Peter']['office'] = 'Kuhn 223'
    book['Woodfin, Edward']['office'] = 'Carmichael 308A'
    return book

def print_alphabetically(phonebook: dict[str, dict[str, str]]) -> None:
    names = list(phonebook)
    names.sort() # Sorts the list of names
    for name in names:
        print(phonebook[name])

def find_entries_with_office(phonebook: dict[str, dict[str, str]]) -> list[str]:
    office_people: list[str] = []
    names = phonebook.keys()
    for name in names:
        if 'office' in phonebook[name]:
            office_people.append(name)
    return office_people
    
def main(args: list[str]) -> int:
    phonebook = make_phonebook()
    print(phonebook)
    print_alphabetically(phonebook)
    print(find_entries_with_office(phonebook))


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
