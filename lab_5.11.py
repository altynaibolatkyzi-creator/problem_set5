f=open('mailbox.txt','r')
fout=open('output.txt','w')
a=[]
lines=f.readlines()
for line in lines:
    if 'Cyrus' in line:
        name=line.split("Cyrus")[1].split()[0]
        a.append(name)
a.sort()
for name in a:
    fout.write(name+"\n")
f.close()
fout.close()