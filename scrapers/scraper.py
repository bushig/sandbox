import threading
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import time

#TODO: Rewrite to collect data from Amazon, keep it in db using SQLAlchemy and display in QT app

time_start = time.time()

ISBNREG = re.compile(r'<div class="isbn-item"><span class="isbn-number">(.+?)</span>')
REG = re.compile(r'<strong>List Price:</strong> \$([\d\.]+?)</p>')
AMZN = 'http://www.isbnsearch.org/isbn/'  # Amazon url

price_dict = dict()
threads = []
MAX_THREADS = 22


def get_isbn_list():
    page = urlopen('http://www.topshelfcomix.com/catalog/isbn-list')

    data = page.read().decode('utf-8')
    page.close()
    return [re.sub(r'\D', '', x) for x in ISBNREG.findall(data)]


def getPrice(isbn):
    global price_dict
    page = None
    while page is None:
        try:
            page = urlopen('{}{}'.format(AMZN, isbn))
        except HTTPError as err:
            if err.code == 404:
                price_dict[isbn] = None
                exit()
            elif err.code == 500:
                print('connection timedout for', isbn)
                pass

    data = page.read().decode('utf-8')
    page.close()
    try:
        result = float(REG.search(data).group(1))
    except AttributeError:
        print(isbn, 'not in db')
        price_dict[isbn] = None
        exit()
    print(result)
    price_dict[isbn] = result


def main():
    isbn_list = get_isbn_list()
    print('isbn count: {}, dublicates: {}'.format(len(isbn_list), len(isbn_list)-len(set(isbn_list))))
    for isbn in isbn_list:
        t = threading.Thread(target=getPrice, args=(isbn,), name=isbn)
        threads.append(t)
    print('threads:{}'.format(len(threads)))
    for t in threads:
        while threading.active_count() >= MAX_THREADS:
            pass
        t.start()

    # for t in threads:
    #     t.join()

    print(len(price_dict))
    print(price_dict)
    print('seconds since start: {}'.format(time.time() - time_start))


if __name__ == '__main__':
    main()
