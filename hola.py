
def getSentence():
    return "{}: {} \n"

def  rick(ms1, ms2):
    return getSentence().format("Rick",ms1+"  "+ms2)

def morty(ms1,ms2):
    a=getSentence().format("Morty","ooooh gizzz")
    b=getSentence().format("Morty",ms1+" "+ms2)
    return a+b

def main():

    if 0<0.1:
        rickDialog=rick("m-m-m-orty","w-w-what are you doing!?")
        mortyDialog=morty("r-r-rick","i d-dont know..");

        print(rickDialog)
        print(len(rickDialog))

        print(mortyDialog)
        print(len(mortyDialog))
    elif 1<1.0:
        rick_text=str(raw_input("(Rick):"))
        morty_text=str(raw_input("(Morty):"))

        rickDialog = rick("m-m-m-orty", rick_text)
        mortyDialog = morty("r-r-rick", morty_text)

        print(rickDialog)
        print(mortyDialog)
    else:
        print("ERRRRRROR")


def bucle():
    arr=("1212","1212","fdfg","ytgfdx","dfghj",23423,(12312,123123))
    for x in arr:
        print "index number " +str(x)

bucle()
main()


# Un programa que me avise cada X mins que abra una URL de Youtube (time, webExplorer)
