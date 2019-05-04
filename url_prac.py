import urllib.request as req1
search_txt='India'
url='https://en.wikipedia.org/wiki/' +search_txt
print (url)
req_url  = req1.urlopen(url)
result =req_url.read()
'''
f =open('wiki_extract.txt','wb')
f.write(result)
f.close()
'''
cnt=0
for search_txt in result:
    cnt+=1
print(cnt)

##########################################################
import re
import urllib.request
from collections import Counter

URL = 'https://simple.wikipedia.org/wiki/India'

counter = Counter()

with urllib.request.urlopen(URL) as source:
    for line in source:
        words = re.split(r"[^A-Z]+", line.decode('utf-8'), flags=re.I)
        counter.update(words)

for word in ['India', 'Indian', 'Indians']:
    print('{}: {}'.format(word, counter[word]))