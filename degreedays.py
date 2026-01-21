def get_data() -> tuple[tuple[str, int, int],...]:
    # Data for October 2025 in Spartanburg, SC from 
    #   https://www.weather.gov/wrh/Climate?wfo=gsp, 2026-01-21
    return (('10/1/2025',0,6),
            ('10/2/2025',0,3),
            ('10/3/2025',3,0),
            ('10/4/2025',3,0),
            ('10/5/2025',0,2),
            ('10/6/2025',0,3),
            ('10/7/2025',0,7),
            ('10/8/2025',0,10),
            ('10/9/2025',0,5),
            ('10/10/2025',5,0),
            ('10/11/2025',4,0),
            ('10/12/2025',0,3),
            ('10/13/2025',0,6),
            ('10/14/2025',0,1),
            ('10/15/2025',0,1),
            ('10/16/2025',0,0),
            ('10/17/2025',3,0),
            ('10/18/2025',0,2),
            ('10/19/2025',0,2),
            ('10/20/2025',8,0),
            ('10/21/2025',7,0),
            ('10/22/2025',6,0),
            ('10/23/2025',8,0),
            ('10/24/2025',9,0),
            ('10/25/2025',10,0),
            ('10/26/2025',11,0),
            ('10/27/2025',11,0),
            ('10/28/2025',15,0),
            ('10/29/2025',16,0),
            ('10/30/2025',10,0),
            ('10/31/2025',13,0))

def make_degree_day_dict(entries: tuple[tuple[str, int, int],...]) -> dict[str, dict[str, int]]:
    deg_days: dict[str, dict[str, int]] = {}
    for entry in entries:
        deg_days[entry[0]] = {'heating': entry[1], 'cooling': entry[2]}
    return deg_days

def accumulate_degree_days(deg_days: dict[str, dict[str, int]]) -> dict[str, int]:
    totals = {'heating': 0, 'cooling': 0} # Accumulator variable
    for date in deg_days.keys():          # Loop
        totals['heating'] = totals['heating'] + deg_days[date]['heating'] # Update the accumulators
        totals['cooling'] = totals['cooling'] + deg_days[date]['cooling']
    return totals

def main(args: list[str]) -> int:
    entries = get_data()
    degreedays = make_degree_day_dict(entries)
    #print(degreedays)
    print(accumulate_degree_days(degreedays))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
