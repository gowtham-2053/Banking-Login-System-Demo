class account:
    username=""
    password=""
    bal=0
    def createAccount(self,username,password):
        self.username=username
        self.password=password
    def Banking(self):
        username=input("Enter your username : ")
        password=input("Enter your password : ")
        if(self.username==username and self.password==password):
            print("\n1). Deposit")
            print("\n2). Withdrawl")
            print("\n3). Balance Enquiry")
            print("\n4). Exit")
            n=0
            while(True):
                n=int(input("Enter your operation : "))
                if(n==1):
                    amnt=int(input("Enter your deposit amount : "))
                    self.deposit(amnt)
                elif(n==2):
                    amnt=int(input("Enter your amount for Withdrawl : "))
                    self.withdrawl(amnt)
                elif(n==3):
                    self.balEnquiry()
                else:
                    break
            print("\n Thank You for using our Banking System")
            print("\nPlease contact our customer care in case of any InConvience Ph:1234567890")
        else:
            print("Unauthorized Entry")
    def deposit(self,n):
        self.bal+=n
    def withdrawl(self,n):
        if(self.bal>n):
            self.bal-=n
            print("Requested amount debited ",n)
            print("\nBalance Available :",self.bal)
        else:
            print("Bank balance insufficient")
    def balEnquiry(self):
        print("Amount Rs.{} Available".format(self.bal))
           
jemsath=account()
jemsath.createAccount("Jemsath","Fathima")
jemsath.Banking()
