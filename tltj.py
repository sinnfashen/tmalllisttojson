import json
ans = []
with open('tmall_list', 'r') as f:
    lines = f.readlines()
    x = 0
    while x < lines.__len__():
        if lines[x][0]=='-':
            name = lines[x][4:-5]
            paras = ''
            while (x+1 < lines.__len__()) and (lines[x+1][0] != '-'):
                x += 1
                paras = '{}&{}'.format(paras, lines[x][0:-1])
            x += 1
            ans.append(
                {'url': 'https://list.tmall.com/m/search_items.htm?{}&page_no=1&*name*{}'.format(paras[1:], name)})
            ans.append(
                {'url': 'https://list.tmall.com/m/search_items.htm?{}&page_no=2&*name*{}'.format(paras[1:], name)})
            ans.append(
                {'url': 'https://list.tmall.com/m/search_items.htm?{}&page_no=3&*name*{}'.format(paras[1:], name)})
result = json.dumps({'ans':ans})
with open('listoflist', 'w') as f:
    f.write(result)
with open('listoflist', 'r') as f:
    result = f.read()
js = json.loads(result)
print(js['ans'][0]['url'].split('&')[2])