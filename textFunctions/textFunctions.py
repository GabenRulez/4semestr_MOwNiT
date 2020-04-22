# Są to funkcje w całości napisane przeze mnie (Wojciech Kosztyła),
# a ich celem jest poprawa czytelności programów bez interfejsu
# (tj. tych wypisujących wyniki w konsoli)

spacer = ""
defaultWidth = 90
lineOf2Stars    = "**"
lineOf4Stars    = "****"
lineOf8Stars    = "********"
lineOf16Stars   = "****************"
lineOf32Stars   = "********************************"
lineOf64Stars   = "****************************************************************"


def printSpacer(number=1):
    for i in range(number):
        print(spacer)


def printLineSpacer(spacers=1):
    printSpacer(spacers)

    tempText = ""
    tempWidth = defaultWidth
    while tempWidth > 0:
        if tempWidth >= 64:
            tempText += lineOf64Stars
            tempWidth -= 64
        elif tempWidth >= 32:
            tempText += lineOf32Stars
            tempWidth -= 32
        elif tempWidth >= 16:
            tempText += lineOf16Stars
            tempWidth -= 16
        elif tempWidth >= 8:
            tempText += lineOf8Stars
            tempWidth -= 8
        elif tempWidth >= 4:
            tempText += lineOf4Stars
            tempWidth -= 4
        elif tempWidth >= 2:
            tempText += lineOf2Stars
            tempWidth -= 2
        else:
            tempText += "*"
            tempWidth -= 1

    print(tempText)
    printSpacer(spacers)
    return


def printTitle(text,spacers=1):
    howManyStars = int( (defaultWidth - len(text) - 2)/2 )

    tempStars = ""
    for i in range(howManyStars):
        tempStars += "*"
    tempText = tempStars + " " + text + " " + tempStars
    if(howManyStars > 0):
        if (len(text) %2 == 1):
            tempText += "*"

    printSpacer(spacers)
    print(tempText)
    printSpacer(spacers)
    return

