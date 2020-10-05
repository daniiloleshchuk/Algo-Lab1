import datetime
import csv


class PromotionalProduct:
    def __init__(self, discount_percentage: float, product_name: str, initial_price: float, promotional_price: float):
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
            products.append(
                PromotionalProduct(product_name=line[0], initial_price=float(line[1]),
                                   discount_percentage=float(line[2]), promotional_price=float(line[3])))

    return products


def print_algo_conclusion(algo_name: str, work_time, comparison_operations_quantity: int, exchange_operations_quantity:int):
    print()
    print("{} Sort by initial price".format(algo_name))
    print("Working time: {}".format(work_time))
    print("Comparison operations quantity: {}".format(comparison_operations_quantity))
    print("Exchange operations quantity: {}".format(exchange_operations_quantity))
    print()


def bubble_sort_by_initial_price(products_to_sort: list, reverse: bool = False):
    start_time = datetime.datetime.now()


    comparison_operations_quantity = 0
    exchange_operations_quantity = 0
    is_list_sorted = False
    list_length = len(products_to_sort)

    while not is_list_sorted:
        is_list_sorted = True

        for i in range(list_length - 1):
            comparison_operations_quantity += 1

            if reverse is False:

                if products_to_sort[i].initial_price > products_to_sort[i + 1].initial_price:
                    exchange_operations_quantity += 1
                    is_list_sorted = False

                    products_to_sort[i].initial_price, products_to_sort[i + 1].initial_price = \
                        products_to_sort[i + 1].initial_price, products_to_sort[i].initial_price

            elif reverse is True:

                if products_to_sort[i].initial_price < products_to_sort[i + 1].initial_price:
                    exchange_operations_quantity += 1
                    is_list_sorted = False

                    products_to_sort[i].initial_price, products_to_sort[i + 1].initial_price = \
                        products_to_sort[i + 1].initial_price, products_to_sort[i].initial_price

    end_time = datetime.datetime.now()
    working_time = end_time - start_time

    print_algo_conclusion('Bubble', working_time, comparison_operations_quantity, exchange_operations_quantity)

    return products_to_sort


def sort_by_discount_percentage(products_to_sort: list, reverse: bool = False):
    def merge_sort_by_discount_percentage(products_to_sort, reverse: bool = False,
                                          comparison_operations_quantity=0, exchange_operations_quantity=0):
        if len(products_to_sort) > 1:
            m = len(products_to_sort) // 2
            left = products_to_sort[:m]
            right = products_to_sort[m:]

            left, left_comparison_operations_quantity, left_exchange_operations_quantity = \
                merge_sort_by_discount_percentage(left, reverse, comparison_operations_quantity,
                                                  exchange_operations_quantity)
            right, right_comparison_operations_quantity, right_exchange_operations_quantity = \
                merge_sort_by_discount_percentage(right, reverse, comparison_operations_quantity,
                                                  exchange_operations_quantity)

            comparison_operations_quantity += left_comparison_operations_quantity + right_comparison_operations_quantity
            exchange_operations_quantity += left_exchange_operations_quantity + right_exchange_operations_quantity

            products_to_sort = []

            while len(left) > 0 and len(right) > 0:
                comparison_operations_quantity += 1
                if not reverse:
                    if left[0].discount_percentage < right[0].discount_percentage:
                        exchange_operations_quantity += 1
                        products_to_sort.append(left[0])
                        left.pop(0)
                    else:
                        products_to_sort.append(right[0])
                        right.pop(0)
                elif reverse:
                    if left[0].discount_percentage > right[0].discount_percentage:
                        exchange_operations_quantity += 1
                        products_to_sort.append(left[0])
                        left.pop(0)
                    else:
                        products_to_sort.append(right[0])
                        right.pop(0)
            for i in left:
                products_to_sort.append(i)
            for i in right:
                products_to_sort.append(i)

        return products_to_sort, comparison_operations_quantity, exchange_operations_quantity

    start_time = datetime.datetime.now()

    sorted_products, comparison_operations_quantity, exchange_operations_quantity =\
        merge_sort_by_discount_percentage(products_to_sort, reverse)

    end_time = datetime.datetime.now()
    working_time = end_time - start_time

    print_algo_conclusion('Merge', working_time, comparison_operations_quantity, exchange_operations_quantity)

    return sorted_products


input_data = get_input_data_in_list('in_1.csv')
for el in input_data:
    print(el)

result = sort_by_discount_percentage(input_data, reverse=True)
#result = bubble_sort_by_initial_price(input_data)
for product in result:
    print(product.__str__())
