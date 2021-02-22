data="13456"
otp=""

for cdigit in data:
    if int(cdigit)%2==1:
        otp+=str(int(cdigit)*int(cdigit))
print(otp[:5])
