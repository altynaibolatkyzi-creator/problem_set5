f = open("mailbox.txt", "r")
fout=open("output.txt", "w")
lines=f.readlines()
a=[]
log=''
inside=False
for line in lines:
    if line.startswith("Log:"):
        inside=True
        log=''
    elif inside and line.startswith("----------------------"):
        a.append(log.strip())
        inside=False
    elif inside:
        log=log+line
a.sort()
for name in a:
    fout.write(name+'\n\n')
f.close()
fout.close()