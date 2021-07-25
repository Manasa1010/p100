class Atm(object):
    def __init__(self,userAtmCardNo,pinNumber):
        self.userAtmCardNo=userAtmCardNo
        self.pinNumber=pinNumber

    def tellUserAtmCardNo(self):
        print("User's atm card number is"+str(self.userAtmCardNo))

    def tellPinNumber(self):
        print("Pin Munber of user is"+str(self.pinNumber))
    def cashWithDrawl(self):
        print("cash you with drawl is 10000")

    def balanceEnquiry(self):
        print("you have 50000 in your account")

def main():
    cardNum=int(input("Enter your card number: "))
    pinNum=int(input("Enter your pin number: "))
    num=int(input("Enter your choice(1 for cash withdrawl 2 for balance enquiry): "))
    account=Atm(cardNum,pinNum)
    if(num==1):
        account.cashWithDrawl()
    elif(num==2):
        account.balanceEnquiry()
    else:
        print("Wrong input")

main()

    

