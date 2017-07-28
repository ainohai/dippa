# -*- coding: utf-8 -*-
import re
import os
    

pat = '<h'
newFileStart = '''---
post_title: {title}
layout: page
published: true
---
'''
outfile = open('textBeforeHeader.txt', 'w')

with open('testi.html') as infile:
    for line in infile:
        if pat not in line:
            outfile.write(line)
        else:
            text = re.search(r'>(.+?)<', line, re.DOTALL).group()
            text= text[1:-1]
            text = text.lower()
            text = text.replace(" ", "-")
            text = text.replace("ä", "a")
            text = text.replace("ö", "o")
            my_file = '_pages/%s.md' % text
            print line

            if os.path.isfile(my_file):
                outfile2 = open(my_file, 'r')
                savedLines = ''
                i = 0
                for line2 in outfile2:
                    if "---" in line2:
                        i = i + 1
                    savedLines = savedLines + line2
                    if i > 1 :
                        break
                outfile2.close()
                outfile = open(my_file, 'w')
                print savedLines
                outfile.write(savedLines)
                outfile.write(line)
            else:
               print "create new file"
               outfile = open(my_file, 'w')
               start = newFileStart.format(title = text)
               outfile.write(start)
               outfile.write(line)
