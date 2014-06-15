import re
#m = re.search("(<a.*?>.*?</a>)","<a href='https://post.craigslist.org/c/sng?lang=en'>post</a>")
#print m.group(1)
m = re.search("href='(.*?)'","<a href='https://post.craigslist.org/c/sng?lang=en'>post</a>")
#print m
print m.group(1)