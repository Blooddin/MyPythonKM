#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
import argparse


symbols_dict = {
    'latin': (97, 122),
    'digits': (48, 57),
    'cyrillic': (1072, 1105),
    'utf-8': (33, 65535)
}


def strtotuple(value):
    value = value[1:-1]
    value = tuple(map(int, value.split(', ')))
    return value


def checkpositive(value):
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError(f'The {value}'
                                         f'is invalid(not positive)')
    return value


def printprogressbar(progress):
    sys.stdout.write('\r')
    sys.stdout.flush()
    progress = round(progress)
    printline = '|'*progress + '.'*(100-progress) + ' ' + str(progress) + '%'
    sys.stdout.write(printline)


def makeoneline(lenght, symbols='latin', word=(5, 9)):
    res = []
    for i in range(lenght):
        if isinstance(word, tuple):
            one_word = ''.join([chr(random.randint(*symbols_dict[symbols]))
                                for x in range(random.randint(*word))])
            res.append(one_word)
        else:
            one_word = ''.join([chr(random.randint(*symbols_dict[symbols]))
                                for x in range(word)])
            res.append(one_word)
    return res


def makelines(size, symbols='latin', line=(10, 50),
              word=(5, 9), enableprogressbar=0):
    filesize = int(size * (1024 ** 2))
    filesizeleft = int(size * (1024 ** 2))
    print(filesizeleft)
    while filesizeleft > 0:
        if isinstance(line, tuple):
            numberofwords = random.randint(*line)
        else:
            numberofwords = line
        currline = makeoneline(numberofwords, symbols, word)
        resline = ' '.join(currline) + '\n'
        resline = resline.encode('utf8', 'replace')
        resline = resline[:filesizeleft]
        yield resline
        filesizeleft -= len(resline)
        currprogress = (1-(filesizeleft/filesize))*100
        if(enableprogressbar):
            printprogressbar(currprogress)


def makefile(size, symbols='latin', line=(10, 50),
             word=(5, 9), enableprogressbar=0, path='text.txt'):
    with open(path, 'wb') as f:
        f.writelines(makelines(size, symbols, line, word, enableprogressbar))


if __name__ == '__main__':

    size = 2
    symbols = 'latin'
    line = (10, 50)
    word = (5, 9)
    enableprogressbar = 0
    path = 'text.txt'

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="The size of the output file",
                        type=checkpositive)
    parser.add_argument("-symbols", "--symbols", type=str,
                        help="The type of symbols(digits, latin, "
                             "cyrillic or utf-8)")
    parser.add_argument("-l", "--line", help="The size of the line")
    parser.add_argument("-w", "--word", help="The size of the word")
    parser.add_argument("-enableprogressbar", "--enableprogressbar",
                        help="Enabling the progress bar", action="store_true")
    parser.add_argument("-p", "--path", help="The path to the text file")
    args = parser.parse_args()

    if(args.size):
        size = int(args.size)

    if (args.symbols):
        symbols = args.symbols

    if (args.line):
        if(args.line.isdigit()):
            line = int(args.line)
        else:
            line = strtotuple(args.line)

    if (args.word):
        if (args.word.isdigit()):
            word = int(args.word)
        else:
            word = strtotuple(args.word)

    if (args.enableprogressbar):
        enableprogressbar = args.enableprogressbar

    if (args.path):
        path = args.path

    if(not args.size):
        size = int(input("Enter the size of the file, it's obligatorily: "))
        print("Next arguments are not necessary, "
              "if you don't want to enter them type '-' ")

        symbols = str(input("Input the type of symbols"
                            "(digits, latin, cyrillic, utf-8): "))
        if(symbols == '-'):
            symbols = 'latin'

        line = str(input("Input the amount of words in lines: "))
        if (line == '-'):
            line = (10, 50)
        else:
            if(line[0] == '('):
                line = strtotuple(line)
            else:
                line = int(line)

        word = str(input("Input the amount of letters in words: "))
        if (word == '-'):
            word = (5, 9)
        else:
            if (word[0] == '('):
                word = strtotuple(word)
            else:
                word = int(word)

        enableprogressbar = str(input("Enabling the progress bar: "))
        if (enableprogressbar == '-'):
            enableprogressbar = 0
        else:
            enableprogressbar = 1

        path = str(input("Input the Path Dir value: "))
        if (path == '-'):
            path = 'text.txt'

    makefile(size, symbols, line, word, enableprogressbar, path)
