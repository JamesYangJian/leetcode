import numpy as np

def package_caculate(things, bag_size):
    """
    use dynamic programming for package problem
    :param things: a dict of things to be stolen
        {name:{'s': size, 'v': value}}
    :param bag_size: integer
    :return: (v, list) --- v: total value, list --- things to be stolen
    """

    nums = len(things)
    thing_name_list = list(things.keys())
    size_list = [i+1 for i in range(bag_size)]
    table = np.array([[0] * bag_size] * nums)

    for i in range(0, nums, 1):
        for j in range(0, bag_size, 1):
            name = thing_name_list[i]
            
            if i == 0:
                if (j+1) >= things[name]['s']:
                    table[i][j] = things[name]['v']
            else:
                cur_size = things[name]['s']
                cur_value = things[name]['v']

                left_size = size_list[j] - cur_size
                if left_size < 0:
                    table[i][j] = table[i-1][j]
                else:
                    if left_size == 0:
                        new_value = cur_value
                    else:
                        new_value = cur_value + table[i-1][left_size-1]
                    if new_value > table[i-1][j]:
                        table[i][j] = new_value
                    else:
                        table[i][j] = table[i-1][j]

    print(table)
    total_value = table[i][j]
    chosen_list = []

    while i > 0:
        if table[i][j] > table[i-1][j]:
            name = thing_name_list[i]
            chosen_list.append(name)
            j = j - things[name]['s']

        i = i - 1
        if i == 0 and j > 0:
            name = thing_name_list[0]
            chosen_list.append(name)

    return total_value, chosen_list

if __name__ == '__main__':
    things = {
        'laptop': {'s': 3, 'v': 2000},
        'guitar': {'s': 1, 'v':1500},
        'recorder': {'s': 4, 'v': 3000},
        'iphone': {'s': 1, 'v': 2000},
        'mp3': {'s': 1, 'v': 1000}
    }
    bag_size = 4

    print(things)

    v, l = package_caculate(things, bag_size)
    print(v)
    print(l)







