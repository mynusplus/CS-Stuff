import os

print(os.path.dirname(os.path.abspath(__file__)))

print(os.path.abspath(__file__))
'''
location = '\\southw-sfps-01.business.mpls.k12.mn.us\Students_A-L\tlin2001\Desktop\PageRank Pages'


htmlPages = []
for file in os.listdir(location):
    if file.endswith('.html'):
        htmlPages.append(file)

print(htmlPages)
'''