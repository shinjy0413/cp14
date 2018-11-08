import requests
url='http://www.vox.com/2018/9/25/17901082/trump-un-2018-speech-full-text'
r=requests.get(url)
r.encoding='utf8'
data=str(r.text)
begin=data.find("One year ago,")
end=data.rfind('Thank you very much. Thank you. (Applause.)')+len('Thank you very much. Thank you. (Applause.)')

data=data[begin:end]
data=data.replace('<p',' ')
data=data.replace('</p>',' ')

words=data.split()

mydict={}

for w in words:
    if w in mydict:
        mydict[w]+=1
    else:
        mydict[w]=1

def keyfunction(k):
    return mydict[k]

for key in sorted(mydict,key=keyfunction, reverse=True)[:20]:
    print("%s:%i"%(key, mydict[key]))
