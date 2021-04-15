import pyperclip, re

text = str(pyperclip.paste())  # to use the copied content from clipbord
matches = []  # Empty list to store matches


def PhoneNumCheck():

    PhnNumregex = re.compile(r'''
        (\(?(\+?\d{1,3})\)?  #area code
        [\s_.-]?)?           #separator or space
        (\d{3})              #first three-digit
        [\s_.-]?             #separator or space
        (\d{3})              #second three-digits
        [\s_.-]?             #separator or space
        (\d{4,5})            #last four/five-digits
    ''', re.VERBOSE)         # VERBOSE is used to ignore whitespace and comments inside the regex string

    for num in PhnNumregex.findall(text):
        if num[1] != '':
            #leadingZeros = "^\+?0*"
            #newNum1 = re.sub(leadingZeros,"",num[1])
            PhoneNum = '(' + num[1] + ')'
        else:
            PhoneNum = ''
        PhoneNum += "-".join([num[2],num[3],num[4]])
        matches.append(PhoneNum)


def EmailCheck():
    emailCheck = re.compile(r'''
        ([a-zA-Z0-9._%-]+        #username
        @                        #@ character
        [a-zA-Z0-9_-]+           #domain name
        \.                       # .(dot) 
        [a-zA-Z]{2,3}            #domain type
        (\.[a-zA-Z]{2,3})?)      #second domain type like co.in 
    ''', re.VERBOSE)

    for emails in emailCheck.findall(text):
        matches.append(emails[0])

# printing the output from matches list
def PrintMatches():
    if len(matches) > 0:
        print('Found matches: '+ str(len(matches)))
        for i in range(0, len(matches)):
            print(matches[i])
    else:
        print('***No Phone Number or Email Address found.***')


def main():
    PhoneNumCheck()
    EmailCheck()
    PrintMatches()


if __name__ == '__main__':
    main()