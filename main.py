from parser import Parser


if __name__ == '__main__':
    to_home = Parser('https://tagiltram.ru/bus-58-1').parse_time()
    print(to_home)

