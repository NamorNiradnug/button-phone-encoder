#!/usr/bin/python
"""Utility that encodes strings to a button phone notation."""

import argparse

decode_d = {
    "1": " ",
    "2": "a",
    "22": "b",
    "222": "c",
    "3": "d",
    "33": "e",
    "333": "f",
    "4": "g",
    "44": "h",
    "444": "i",
    "5": "j",
    "55": "k",
    "555": "l",
    "6": "m",
    "66": "n"
    "666": "o",
    "7": "p",
    "77": "q",
    "777": "r",
    "7777": "s",
    "8": "t",
    "88": "u",
    "888": "v",
    "9": "w",
    "99": "x",
    "999": "y",
    "9999": "z"
}

encode_d = {decode_d[k]: k for k in decode_d}


def encode(s: str) -> str:
    """Encodes s."""
    if not s:
        return ""
    enc_list = []
    for ch in s:
        if ch.isnumeric():
            enc_list.append("#" + ch)
        else:
            enc_list.append(encode_d[ch])
    enc = ""
    for i in range(len(enc_list) - 1):
        enc += enc_list[i]
        if enc_list[i][0] == enc_list[i + 1][0] != "#":
            enc += "+"
    return enc + enc_list[-1]


def decode(enc: str) -> str:
    """Decodes enc."""
    s = ""
    cur = ""
    i = 0
    while i < len(enc):
        ch = enc[i]
        if ch == "+":
            s += decode_d[cur]
            cur = ""
        elif ch == "#":
            if cur:
                s += decode_d[cur]
                cur = ""
            s += enc[i + 1]
            i += 1
        elif cur == "" or ch == cur[0]:
            cur += ch
        else:
            s += decode_d[cur]
            cur = ch
        i += 1
    if cur:
        s += decode_d[cur]
    return s


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-d", "--decode", dest="decode", required=False,
                        action="store_true", help="decoding mode (default is encoding)")
    parser.add_argument("string", type=str)
    args = parser.parse_args()
    if args.decode:
        print(decode(args.string))
    else:
        print(encode(args.string))
