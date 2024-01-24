# Works only with 2D lists
def unpack_list(ls):
    unpacked_list = []
    for i in range(0, len(ls)):
        for item in ls[i]:
            unpacked_list.append(item)

    return unpacked_list
