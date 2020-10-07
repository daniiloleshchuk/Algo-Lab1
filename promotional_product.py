import datetime
import csv


class PromotionalProduct:

    def __init__(self, product_name: str, initial_price: float, discount_percentage: float, promotional_price: float):
        self.product_name = product_name
        self.initial_price = initial_price
        self.discount_percentage = discount_percentage
        self.promotional_price = promotional_price

    def __str__(self):
        return 'Product name: {}, Initial price: {}, Discount percentage: {}, Promotional price: {}'\
            .format(self.product_name, self.initial_price, self.discount_percentage, self.promotional_price)


def get_input_data_in_list(file_name: str):
    products = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            products.append(PromotionalProduct(line[0], float(line[1]), float(line[2]), float(line[3])))

    return products


def print_algo_conclusion(algo_name: str, sort_by: str, work_time, comparisons: int, exchanges: int):
    print()
    print("{} Sort by {}".format(algo_name, sort_by))
    print("Working time: {}".format(work_time))
    print("Comparison operations quantity: {}".format(comparisons))
    print("Exchange operations quantity: {}".format(exchanges))
    print()


def comparator(val1, val2, reverse: bool = False):
    """

    This function returns bool value, depends on values you passed in

    :param val1: First value to compare
    :param val2: Second value to compare
    :param reverse: False by default. Pass 'True' to sort in descending order,
     or pass 'False' to sort in ascending order.
    :return: Bool value, that means val1 is more val2 or not

    """
    if reverse:
        return val1 > val2
    else:
        return val1 < val2


def merge_sort(list_to_sort: list, key, reverse: bool = False, comparisons=0, exchanges=0):
    """

    This function sorts the list in merge sort manner

    :param list_to_sort: List that will be sorted
    :param key: lambda to define by which key to sort
    :param reverse: False by default. Pass 'True' to sort in descending order,
     or pass 'False' to sort in ascending order.
    :param comparisons: Quantity of comparison operations
    :param exchanges: Quantity of exchange operations
    :return: Quantity of comparison operations and quantity of exchange operations
    """

    if len(list_to_sort) > 1:
        middle = len(list_to_sort) // 2
        left_half = list_to_sort[:middle]
        right_half = list_to_sort[middle:]

        merge_sort(left_half, key, reverse)
        merge_sort(right_half, key, reverse)

        left_half_iterator = right_half_iterator = main_list_iterator = 0

        while left_half_iterator < len(left_half) and right_half_iterator < len(right_half):
            comparisons += 1

            if comparator(key(left_half[left_half_iterator]), key(right_half[right_half_iterator]), reverse):
                exchanges += 1
                list_to_sort[main_list_iterator] = left_half[left_half_iterator]
                left_half_iterator += 1

            else:
                list_to_sort[main_list_iterator] = right_half[right_half_iterator]
                right_half_iterator += 1

            main_list_iterator += 1

        while left_half_iterator < len(left_half):
            list_to_sort[main_list_iterator] = left_half[left_half_iterator]
            left_half_iterator += 1
            main_list_iterator += 1

        while right_half_iterator < len(right_half):
            list_to_sort[main_list_iterator] = right_half[right_half_iterator]
            right_half_iterator += 1
            main_list_iterator += 1

        return comparisons, exchanges


def merge_sort_by_discount_percentage(products_to_sort: list, reverse: bool = False):

    start_time = datetime.datetime.now()

    comparisons, exchanges = merge_sort(products_to_sort, key=lambda x: x.discount_percentage, reverse=reverse)

    end_time = datetime.datetime.now()
    working_time = end_time - start_time

    print_algo_conclusion('Merge', 'discount percentage', working_time, comparisons, exchanges)


def bubble_sort(list_to_sort: list, key, reverse: bool = False, comparisons=0, exchanges=0):
    """

    This function sorts the list in bubble sort manner

    :param list_to_sort: List that will be sorted
    :param key: lambda to define by which key to sort
    :param reverse: False by default. Pass 'True' to sort in descending order,
     or pass 'False' to sort in ascending order.
    :param comparisons: Quantity of comparison operations
    :param exchanges: Quantity of exchange operations
    :return: Quantity of comparison operations and quantity of exchange operations
    """
    is_list_sorted = False
    list_length = len(list_to_sort)
    while not is_list_sorted:
        is_list_sorted = True

        for i in range(list_length - 1):
            comparisons += 1

            if comparator(key(list_to_sort[i]), key(list_to_sort[i + 1]), reverse):
                exchanges += 1
                is_list_sorted = False

                list_to_sort[i], list_to_sort[i+1] = list_to_sort[i+1], list_to_sort[i]

    return comparisons, exchanges


def bubble_sort_by_initial_price(products_to_sort: list, reverse: bool = False):
    start_time = datetime.datetime.now()

    comparisons, exchanges = bubble_sort(products_to_sort, key=lambda x: x.initial_price, reverse=reverse)

    end_time = datetime.datetime.now()
    working_time = end_time - start_time

    print_algo_conclusion('Bubble', 'initial price',
                          working_time, comparisons, exchanges)


print()

input_data = get_input_data_in_list('in_1.csv')

for el in input_data:
    print(el.__str__())

print()

# merge_sort_by_discount_percentage(input_data, reverse=True)
bubble_sort_by_initial_price(input_data, reverse=False)

print()

for el in input_data:
    print(el.__str__())

print()
