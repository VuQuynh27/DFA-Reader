# chạy cmd này tại terminal để download thư viện beautifulsoup4: pip install beautifulsoup4
# chạy cmd này tại terminal để download lxml parser: pip install lxml

from ReadFile import *

print('Hãy nhập vào địa chỉ file chứa Automaton: ')
link = input()

Automat = readFile(link)
# Automat.__printAutomaton__()

print('Hãy nhập vào xâu nhị phân: ')
strA = input()
Automat.process(strA)


