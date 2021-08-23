import random

charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    plainText = input("Enter the plain text : ")
    keyword = input("Enter keyword : ")
    encrypted = encrypt(plainText, keyword)
    decrypted = decrypt(encrypted[0], encrypted[1], encrypted[2])

    print("Plain Text : " + plainText)
    print("Keyword : " + encrypted[2])
    print("OTP : " + encrypted[0])
    print("Encrypted: " + encrypted[1])
    print("Decrypted: " + decrypted)


def OTP(text, textList):
    for c in text:
        if c != ' ':
            textList.append(ord(c) - 65)

    return textList


def change2ascii(text, List, otpList):
    for t in text.upper():
        if t != ' ':
            List.append(otpList[charset.find(t)])

    return List


def keyRepeat(keywords, plainTexts):
    if len(keywords) < len(plainTexts):
        if len(plainTexts) % len(keywords) != 0:
            k = int(len(plainTexts) / len(keywords)) + 1
        else:
            k = int(len(plainTexts) / len(keywords))
        keywords = keywords * k
    return keywords


def encrypt(plainText, keyword):

    # create otp
    otp = "".join(random.sample(charset, len(charset)))
    otpList = []
    plainTexts = []
    keywords = []
    cipherText = ""

    # change otp to ascii
    otpList = OTP(otp, otpList)
    plainTexts = change2ascii(plainText, plainTexts, otpList)
    keywords = change2ascii(keyword, keywords, otpList)
    keywords = keyRepeat(keywords, plainTexts)

    i = 0
    for i in range(len(plainTexts)):
        n = plainTexts[i] + keywords[i]
        n=n%26
        cipherText += charset[otpList.index(n)]
        i += 1

    return otp, cipherText, keyword


def decrypt(otp, cipherText, keyword):
    plainText = ""
    otpList = []
    keywords = []
    cipherTexts = []

    otpList = OTP(otp, otpList)
    cipherTexts = change2ascii(cipherText, cipherTexts, otpList)
    keywords = change2ascii(keyword, keywords, otpList)
    keywords = keyRepeat(keywords, cipherTexts)

    i = 0
    for i in range(len(cipherTexts)):
        n = cipherTexts[i] - keywords[i]
        n= n%26
        plainText += charset[otpList.index(n)]
        i += 1

    return plainText


if __name__ == "__main__":
    main()
