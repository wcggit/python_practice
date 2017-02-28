from pattern.web import URL, plaintext

if __name__ == '__main__':
    s = URL('http://data.10jqka.com.cn/rank/lxsz/field/lxts/order/desc/page/2/ajax/1/').download()
s = plaintext(s, keep={'h1': [], 'h2': [], 'strong': [], 'a': ['href']})
print s
