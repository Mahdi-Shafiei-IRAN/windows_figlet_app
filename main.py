import os, pyfiglet, random, time, argparse
from lists import FONTS, COLORS
from pyfiglet import Figlet
from termcolor import colored


def show_fonts():
    """
    showing list of fonts in list.py and get input
    """
    tmp = ""
    for i in FONTS:
        tmp += colored(str(FONTS.index(i)+1) + ". " + i + "   ",random.choice(COLORS))
        if (FONTS.index(i)+1)%10 == 0:
            tmp += "\n"
    print(tmp)

def show_colors():
    """
    showing list of colors in list.py and get input
    """
    tmp = ""
    for i in COLORS:
        tmp += colored(str(COLORS.index(i)+1) + ". " + i + "   ",i)
    print(tmp)

def figlet(ifont = "",icolor = ""):
    """
    main func in program and change text to figlet shapes
    """
    while True:
        print(colored("""
        To reset color and font : reset
        To see colors and choose : color
        To see fonts and choose : font
        Quit : exit
        ""","red"))

        txt = input(colored("Enter your text : ","red"))
        time.sleep(0.1)
        os.system("cls")
        figlet_text = ""

        if txt == "exit":
            break
        elif txt == "color":
            show_colors()
            print("\n\n")
            print(colored("Enter 'c' to cancle.",color="green"))
            icolor = input(colored("Which color? ","red"))
            os.system("cls")
            if icolor == "c":
                icolor = ""
        elif txt == "font":
            show_fonts()
            print("\n\n")
            print(colored("Enter 'c' to cancle.",color="green"))
            ifont = input(colored("Which font? ","red"))
            time.sleep(0.1)
            os.system("cls")
            if ifont == "c":
                ifont = ""
        elif txt == "reset":
            icolor = ""
            ifont = ""
        else:
            if ifont and ifont in FONTS:
                f = Figlet(font=ifont)
            else:
                f = Figlet(font=random.choice(FONTS))
            tmp = f.renderText(txt)

            if icolor and icolor in COLORS:
                color = icolor
            else:
                color = random.choice(COLORS)
            for i in tmp:
                if i == "\n" and (not icolor or not icolor in COLORS):
                    color = random.choice(COLORS)
                elif i == "\n" and icolor in COLORS:
                    color = icolor
                figlet_text += colored(i,color=color)
        print(figlet_text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--c",help="color of text")
    parser.add_argument("-f","--f",help="font of text")
    args = parser.parse_args()
    if str(args.c) in COLORS and str(args.f) in FONTS:
        figlet(str(args.f),str(args.c))
    else:
        figlet()
