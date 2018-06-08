import time, os

postdir = "C:/Users/Hyun/TKimhyun.github.io/_posts/" #Include trailing slash!
vim = os.path.normpath("C:/Atom/atom.exe")
d = time.strftime('%Y-%m-%d')
print(d)
title = input("Post Title: ").title()
cats = input("[Categories]: ").lower()
tags = input("[Tags]: ").lower()
ts = title.replace(" ", "-").lower()
fname = d + "-" + ts + ".md"
f = os.path.normpath(postdir + fname)
head = "---"
head += "\ntype: post"
head += "\ntitle: %s" % title
if cats: head += "\ncategories: %s" % cats
if tags: head += "\ntags: %s" % tags
head += "\n---\n"

print(f)
print(head)

#with open(f, 'w') as postfile:
#    postfile.write(head)
#command='"%s" -c "set spell spelllang=en_us" -c "setf markdown" + "%s"' % (vim, f)
#print(command)
#os.system('"' + command + '"')
