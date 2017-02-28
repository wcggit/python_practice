import json
from httplib import HTTPConnection

from numpy import array

import Order
from com.wcg.mahineLearning import Kmean


def object_decoder(obj):
    return Order(obj['id'], obj['sid'], obj['userId'], obj['totalPrice'], obj['createDate'], obj['completeDate'],
                 obj['version'])


def helloWord():
    print "hellos"


def hello(time):
    print time


if __name__ == '__main__':
    helloWord()
    print (100 + 1)
    # name = raw_input();
    # print name;
    # name = round(1.1133, 3)
    # print name * 10 + 1.2e9
    # print floor(1.51)
    # print int(ceil(11.1))
    # print 11 + 11.1;
    # print '''ll...2...2'''
    # print True
    # print False
    # def a():
    #     print  1;
    # a();
    # a1 = 1
    # print  time.time()
    # hello( time.localtime(time.time()))
    # print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    a = [1, 2, 3]
    a = map(lambda x: x + 1, a)
    print a
    a = filter(lambda x: x < 0, a)
    print a
    print range(0, 5)
    conn = HTTPConnection("101.201.37.58")
    conn.request("GET", "/pay/order/1");
    res = conn.getresponse()
    body = res.read();
    order = json.loads(body, object_hook=object_decoder)
    print  order.id, order.completeDate, order.createDate
    print Kmean.kmeanOf([2, 0], array([[1, 1], [1, 2], [2, 0], [2, 1], [1, 0]]), ['a', 'a', 'b', 'b', 'a'], 1)
