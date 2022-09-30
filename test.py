
def main():
    s = 'This dinner is not that bad!'

    notIndexNumber = s.index('not')
    badIndexNumber = s.index('bad') +2
    print(s[badIndexNumber])

    s = s.replace(s[notIndexNumber:badIndexNumber+3], 'good')
    print(s)

main()