fin=open('mailbox.txt','r')
fout=open('output.txt','w')
lines=fin.readlines()
ei=[]
for line in lines:
    if "ESMTP id" in line:
        e=line.strip().split('ESMTP id')[1].split()[0]
        if e not in ei:
            ei.append(e)
se=sorted(ei)
for e in se:
    fout.write(e+"\n")
fin.close()
fout.close()