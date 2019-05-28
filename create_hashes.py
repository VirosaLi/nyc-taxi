from hashlib import md5
import pandas as pd

numerals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# make hashes
def base_n(num, b):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b).lstrip(numerals[0]) + numerals[num % b])


# string to upper case md5 hash
def string_to_md5_upper(str_in):
    return md5(str_in.encode()).hexdigest().upper()


# create checksum map
def build_checksum_map():

    checksum_map = {}

    for i in range(1000):
        for j in range(26 ** 3):
            i_str = str(i)
            alpha_string = base_n(j, 26)
            if len(alpha_string) == 1:
                target_string = i_str[0] + alpha_string + i_str[1:]
            else:
                target_string = alpha_string + i_str

            target_string_hash = string_to_md5_upper(target_string)

            checksum_map[target_string_hash] = target_string

    for i in range(int(6e6)):
        s = '%0.6d' % i
        target_string_hash = string_to_md5_upper(s)
        checksum_map[target_string_hash] = str(i)

    for i in range(5000000, 5900000):
        s = '%0.7d' % i
        target_string_hash = string_to_md5_upper(s)
        checksum_map[target_string_hash] = str(i)

    return checksum_map


def main():

    checksum_map = build_checksum_map()

    print(checksum_map.items())

    # df = pd.Series(checksum_map).to_frame()

    df = pd.DataFrame(checksum_map, index=[0], columns=['hash', 'string'])

    print(df)

    # df.to_csv("rainbow.csv", columns=['hash', 'string'])


if __name__ == '__main__':
    main()
