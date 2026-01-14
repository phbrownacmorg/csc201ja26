def article(word: str) -> str:
    """Return the proper article ("a" or "an") for the given WORD."""
    result = 'a'
    if word[0] in 'aeiou':
        result = 'an'
    return result

def printVerse(animals: str, sound: str) -> None:
    """Print one verse of 'Old Macdonald'."""
    a_an = article(sound) # Note that the proper article for double_sound will be the same
    double_sound = a_an + ' ' + sound + ', ' + sound
    sound = a_an + ' ' + sound
    print('Old Macdonald had a farm, E-I-E-I-O!')
    print('And on that farm he had some ', animals, ', E-I-E-I-O!', sep="")
    print('With', double_sound, 'here and', double_sound, 'there,')
    print('Here ', sound, ', there ', sound, ', everywhere ', double_sound, ',', sep="")
    print('Old Macdonald had a farm, E-I-E-I-O!')
    print()

def main(args: list[str]) -> int:
    printVerse('chickens', 'cluck')
    printVerse('cows', 'moo')
    printVerse('ducks', 'quack')
    printVerse('sheep', 'baa')
    printVerse('horses', 'neigh')
    printVerse('pigs', 'oink')
    printVerse('cats', 'meow')
    printVerse('dogs', 'woof')

    # 19 lines of code instead of 60
    # Adding another verse takes a single new line of code, not 8

    ## The old way:
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some chickens, E-I-E-I-O!')
    # print('With a cluck, cluck here and a cluck, cluck there,')
    # print('Here a cluck, there a cluck, everywhere a cluck, cluck,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 2
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some cows, E-I-E-I-O!')
    # print('With a moo, moo here and a moo, moo there,')
    # print('Here a moo, there a moo, everywhere a moo, moo,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 3
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some ducks, E-I-E-I-O!')
    # print('With a quack, quack here and a quack, quack there,')
    # print('Here a quack, there a quack, everywhere a quack, quack,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 4
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some sheep, E-I-E-I-O!')
    # print('With a baa, baa here and a baa, baa there,')
    # print('Here a baa, there a baa, everywhere a baa, baa,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 5
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some horses, E-I-E-I-O!')
    # print('With a neigh, neigh here and a neigh, neigh there,')
    # print('Here a neigh, there a neigh, everywhere a neigh, neigh,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 6
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some pigs, E-I-E-I-O!')
    # print('With an oink, oink here and an oink, oink there,')
    # print('Here an oink, there an oink, everywhere an oink, oink,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 7
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some cats, E-I-E-I-O!')
    # print('With a meow, meow here and a meow, meow there,')
    # print('Here a meow, there a meow, everywhere a meow, meow,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    # # Verse 8
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print('And on that farm he had some dogs, E-I-E-I-O!')
    # print('With a woof, woof here and a woof, woof there,')
    # print('Here a woof, there a woof, everywhere a woof, woof,')
    # print('Old Macdonald had a farm, E-I-E-I-O!')
    # print()

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))