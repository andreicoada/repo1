def create_phone_number(n):
 list1 = []
for num in n:
        list1.append("".join(str(num)))
    # print(list1)
    ph_str = list1
    # print(ph_str)
    # print("".join(ph_str))
ac = "".join(ph_str[0:3])
prefix = "".join(ph_str[3:6])
suffix = "".join(ph_str[6:10])
    # print(ac)
    # print(prefix)
    # print(suffix)

print("({}) {}-{}".format(ac, prefix, suffix))


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])