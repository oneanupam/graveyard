given_list = [[1, 2], [1, 2, [4, [1, 9, 0]]], 4, 6, [2, [9, 3]]]


def flatten_list(given_list: list) -> list:
    result_list = []
    for item in given_list:
        if isinstance(item, list):
            result_list.extend(flatten_list(item))
        else:
            result_list.append(item)
    return result_list


if __name__ == "__main__":
    print(flatten_list(given_list))
