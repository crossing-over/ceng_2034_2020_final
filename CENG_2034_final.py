#Cansel Hatice Küçükyılmaz / 170709049

#!/usr/bin/python3
import requests
import os
import hashlib
import sys
from multiprocessing import Pool



urls = [
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
 "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"​https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg​",
 "​http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg​",
"​https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg​"]

#1
pid = os.fork()
if (pid >0):
    print("Parent pid is:",os.getpid())
if(pid == 0):
    print("Child process pid is:", os.getpid())
if (pid < 0):
    print("The operation couldn't be completed!")


#2

def download_file(url, file_name = None):

    file_name = None
    r = requests.get(url, allow_redirects = True)
    
    file = str(uuid.uuid4())
    open(file, 'wb').write(r.content)
    print("The file is downloaded",i)

if (pid == 0):
    for i in urls:
        download_file(i)
        


#3
if (pid == 0):
    print("Terminated by child process")
    sys.exit()
os.wait()
    
#4

#def check_duplicate(filepath):
    #with open(filepath,"rb") as file:
        #return md5(file.read()).hexdigest())
    
    #directory = os.getcwd()
    #file_list= os.listdir()
    #print(len(file_list))
           #duplicates = []
    #for i, filename in enumare(directory):
        #if os.path.isfile(filename):
            #with open(filepath, "rb") as file:,
            #file_hash = md5(f.read()).hexdigest()
            #duplicates.append(index,hash_keys[file_hash])
  

#with pool(4) as p:
    #for i in urls:
        #print(p.map(check_duplicate,i)
