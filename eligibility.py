def readInputs() -> tuple[int, int]:
    age = int(input("Please enter a person's age: "))
    cit = int(input("How long has this person been a citizen of the U.S.? "))
    return age, cit

def eligibleHR(age: int, citizen: int) -> bool:
    return False

def main(args: list[str]) -> int:
    age, cit = readInputs()
    print(f'A person who is {age} years old and has been a U.S. citizen for {cit} years ', end="")
    if eligibleHR(age, cit):
        print('is', end=' ')
    else:
        print('is NOT', end=' ')
    print('eligible to serve in the U.S. House of Representatives.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
