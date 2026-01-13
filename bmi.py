# Travis Kelce: 6'5", 250 lbs.: https://en.wikipedia.org/wiki/Travis_Kelce
# Gronk: 6'6", 265 lbs.: https://en.wikipedia.org/wiki/Rob_Gronkowski
# Lionel Messi: 5'7", 148 lbs.: https://www.intermiamicf.com/players/lionel-messi/
# Roger Federer: 6'1", 187 lbs.: https://www.atptour.com/en/players/roger-federer/f324/overview
# Simone Biles: 4'8", 104 lbs.: https://www.espn.com/olympics/summer/2016/athletes/_/athlete/55510/simone-biles
# Bryson DeChambeau: 6'1", 235 lbs.: https://www.foxsports.com/golf/bryson-dechambeau-player-bio

def calc_bmi(height: float, weight: float) -> float:
    """Takes a HEIGHT in inches and a WEIGHT in pounds and returns the corresponding BMI."""
    return weight / height**2 * 703

def classify_bmi(bmi: float) -> str:
    """Takes a BMI and returns the CDC classification (from 
    https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html) for that BMI."""
    result = ''
    if bmi < 18.5:
        result = 'underweight'
    elif bmi < 25:
        result = 'healthy'
    elif bmi < 30:
        result = 'overweight'
    elif bmi < 35:
        result = 'obese, class 1'
    elif bmi < 40:
        result = 'obese, class 2'
    else:
        result = 'severely obese (class 3)'

    return result


def main(args: list[str]) -> int:
    print("This program calculates a person's BMI.")
    height = float(input("Please enter the person's height in inches: "))
    weight = float(input("Please enter the person's weight in pounds: "))
    print('The person is ',height,'" tall and weighs ',weight,' pounds',sep="")

    bmi = calc_bmi(height, weight)
    print('This person has a BMI of', round(bmi,1))
    print('This person is classified as', classify_bmi(bmi))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
