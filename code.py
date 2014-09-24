#!/usr/bin/python
#Author : Paranandi Roopesh
#Entry No: 2014JTM2264

def mood(arr):				#Writing a method to return the mood of the particular user
    max=arr[0]
    j=0
    for i in range(1,6):
        if (arr[i]>max):
            max=arr[i]
            j=i
    if j==0:
        return "Happy"
    if j==1:
        return "Sad"
    if j==2:
        return "Sarcastic"
    if j==3:
        return "Surprised"
    if j==4:
        return "Crook"
    if j==5:
        return "Neutral"
    if j==6:
        return "Angry"
    

a=[0,0,0,0,0,0,0]			#arrays to store the moods of the each user
b=[0,0,0,0,0,0,0]
e=[0,0,0,0,0,0,0]
g=[0,0,0,0,0,0,0]
c=[0,0,0,0,0,0,0]
percentage=[0,0,0,0,0,0,0]
for line in open('/home/paranandi/Assignment9/content.txt','r'):
    user = line[0];			#updating the information about the moods of the user through reading from a file
    if (user=="A"):
        for word in line.split():
            if ((word==":)") or (word==":D")):
                a[0]=a[0]+1
            if ((word==":(") or (word==":'(")):
                a[1]=a[1]+1
            if ((word==":P") or (word==";)")):
                a[2]=a[2]+1
            if ((word==":-o") or (word=="O_O")):
                a[3]=a[3]+1
            if ((word=="B-)") or (word==";)")):
                a[4]=a[4]+1
            if ((word==":-/") or (word=="=_=")):
                a[5]=a[5]+1
            if ((word=="x-(") or (word==">_<")):
                a[6]=a[6]+1
    if (user=="B"):			#reading the contents of the file line by line and then word by word
       for word in line.split():
            if ((word==":)") or (word==":D")):
                b[0]=b[0]+1
            if ((word==":(") or (word==":'(")):
                b[1]=b[1]+1
            if ((word==":P") or (word==";)")):
                b[2]=b[2]+1
            if ((word==":-o") or (word=="O_O")):
                b[3]=b[3]+1
            if ((word=="B-)") or (word==";)")):
                b[4]=b[4]+1
            if ((word==":-/") or (word=="=_=")):
                b[5]=b[5]+1
            if ((word=="x-(") or (word==">_<")):
                b[6]=b[6]+1
    if (user=="E"):
        for word in line.split():
            if ((word==":)") or (word==":D")):
               e[0]=e[0]+1
            if ((word==":(") or (word==":'(")):
               e[1]=e[1]+1
            if ((word==":P") or (word==";)")):
               e[2]=e[2]+1
            if ((word==":-o") or (word=="O_O")):
               e[3]=e[3]+1
            if ((word=="B-)") or (word==";)")):
               e[4]=e[4]+1
            if ((word==":-/") or (word=="=_=")):
               e[5]=e[5]+1
            if ((word=="x-(") or (word==">_<")):
               e[6]=e[6]+1
    if (user=="G"):
        for word in line.split():
            if ((word==":)") or (word==":D")):
               g[0]=g[0]+1
            if ((word==":(") or (word==":'(")):
               g[1]=g[1]+1
            if ((word==":P") or (word==";)")):
               g[2]=g[2]+1
            if ((word==":-o") or (word=="O_O")):
               g[3]=g[3]+1
            if ((word=="B-)") or (word==";)")):
               g[4]=g[4]+1
            if ((word==":-/") or (word=="=_=")):
               g[5]=g[5]+1
            if ((word=="x-(") or (word==">_<")):
               g[6]=g[6]+1
    if (user=="C"):
        for word in line.split():
            if ((word==":)") or (word==":D")):
                c[0]=c[0]+1
            if ((word==":(") or (word==":'(")):
                c[1]=c[1]+1
            if ((word==":P") or (word==";)")):
                c[2]=c[2]+1
            if ((word==":-o") or (word=="O_O")):
                c[3]=c[3]+1
            if ((word=="B-)") or (word==";)")):
                c[4]=c[4]+1
            if ((word==":-/") or (word=="=_=")):
                c[5]=c[5]+1
            if ((word=="x-(") or (word==">_<")):
                c[6]=c[6]+1
mooda=mood(a)				#storing the moods of each user
moodb=mood(b)
moode=mood(e)
moodg=mood(g)
moodc=mood(c)
total=0.0
    
for i in range(0,6):			#calculating the percentage of the mood among all the users
    percentage[i]=a[i]+b[i]+e[i]+g[i]+c[i]
    total=total+percentage[i]
for i in range(0,6):
    percentage[i]=percentage[i]/total	
        
f=open('/home/paranandi/Assignment9/output.txt','w')	#Writing the output of the information into a file
f.write("A : "+mooda+" \n"+"B : "+moodb+" \n"+"E : "+moode+" \n"+"G : "+moodg+" \n"+"C : "+moodc+" \n"+"----------------------------"+"\n")
f.write("Happy \t\t:\t"+str(percentage[0]*100)+"%\n"+"Sad \t\t:\t"+str(percentage[1]*100)+"%\n"+"Sarcastic \t:\t"+str(percentage[2]*100)+"%\n"+"Surprised \t:\t"+str(percentage[3]*100)+"%\n"+"Crook \t\t:\t"+str(percentage[4]*100)+"%\n"+"Neutral \t:\t"+str(percentage[5]*100)+"%\n"+"Angry \t\t:\t"+str(percentage[6]*100)+"%\n")

