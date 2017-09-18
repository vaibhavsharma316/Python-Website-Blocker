import pandas as pd
import sys


help="-h"
host='C:\Windows\System32\drivers\etc\hosts'
redirect='127.0.0.1'


try:
    file_input = sys.argv[1]

    if file_input == help:
       print('Command: filename path [space] option')
       print('Ex: websites.csv -b')
       print('Ex: websites.csv -u')
       print('Option: -u for unblock and -b for block')
       exit(0)
    command=sys.argv[2]

    if command == "-b":

        df = pd.read_csv(file_input)
        websites = list(df.iloc[:,1])

        for website in websites:

            with open(host ,"r+") as file:
                file.seek(0,0)
                content = file.read()

                if website in content:
                    pass
                else:
                    file.write("\r"+redirect + " " + website)

    elif command == '-u':
        df = pd.read_csv(file_input)
        websites = list(df.iloc[:, 1])

        for website in websites:

            with open(host, "r+") as file:
                content = file.read()
                file.seek(0)
                if website in content:
                    file.truncate()
                else:
                    pass

    else:
        print('Incorrect file format passed. It must be csv')

except Exception:
        print('Incorrect argument passed')





