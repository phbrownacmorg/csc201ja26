def format_phone(area_code: int, exchange: int, extension: int) -> None:
    """Format a North American 10-digit phone number in multiple ways."""
    print('\nPhone number:')
    print(f'{area_code:03}-{exchange:03}-{extension:04}') # Usual form; force leading zeroes
    print(f'({area_code:03}) {exchange:03}-{extension:04}') # Old style; force leading zeroes
    print(f'{area_code:03}.{exchange:03}.{extension:04}') # Converse form
    print(f'1-{area_code:03}-{exchange:03}-{extension:04}') # Back when you dialed "1" for long distance...
    print(f'+1 {area_code:03}-{exchange:03}-{extension:04}') # Include the country code

def format_SSN(ssn: str) -> None:
    print('\nSSN:')
    print(ssn) # Without dashes
    print(f'{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}') # With dashes

def parse_ISO_date(isodate: str) -> tuple[int, int, int]:
    year = int(isodate[:4])
    month = int(isodate[5:7])
    day = int(isodate[8:])
    return year, month, day

def format_date(year: int, month: int, day: int) -> None:
    # Month names.  Note the empty entry for month 0.
    months = ('', 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December')
    print('\nDate:')
    print(f'{year:04}-{month:02}-{day:02}') # ISO date format, forcing leading zeroes
    print(f'{month}/{day}/{year}')          # Common American format, four-digit year
    print(f'{month}/{day}/{year % 100}')    # Common American format, two-digit year
    print(f'{day}/{month}/{year}')          # British format, four-digit year
    print(f'{day}/{month}/{year % 100}')    # British format, four-digit year
    print(f'{day}.{month}.{year}')          # German/Dutch format, four-digit year
    print(f'{day}.{month}.{year % 100}')    # German/Dutch format, two-digit year
    print(f'{day}-{months[month][:3]}-{year % 100}') # 1990's DOS format
    print(f'{months[month]} {day}, {year}') # American text format
    print(f'{day} {months[month]} {year}')  # British/military format

def main(args: list[str]) -> int:
    format_phone(864, 867, 5309)
    format_phone(864, 867, 0000)

    format_SSN('123456789')

    format_date(*parse_ISO_date('2026-01-21')) # * unpacks the tuple into its three component values

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
