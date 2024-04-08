from bus_getter import BusGetter
from parser import Parser


if __name__ == '__main__':
    to_home = Parser('https://tagiltram.ru/bus-58-2').parse_time()
    print(BusGetter.get_next_three_bus(to_home))


