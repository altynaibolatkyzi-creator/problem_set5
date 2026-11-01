fin=open('mailbox.txt','r')
fout=open('output.txt','w')
lines=fin.readlines()
i=False
c=0
s=[]
for line in lines:
    if line.strip()=="Log:":
        i=True
        c=0
        continue
    if "This automatic notification" in line:
        if i:
            s.append(c)
        i=False
        continue
    if i:
        c=c+1
for number in s:
    fout.write(str(number) + '\n')
fin.close()
fout.close()