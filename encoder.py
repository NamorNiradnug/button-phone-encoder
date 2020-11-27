#!/usr/bin/python
"""Utility that encodes strings to a button phone notation."""

import argparse

DICT_PATH = ".encoder-dict.data"
encode_d = {" ": "1"}
decode_d = {"1": " "}
with open(DICT_PATH) as data:
    for line in data:
        s = line.split()
        encode_d[s[1]] = s[0]
        decode_d[s[0]] = s[1]


def encode(s):
    """Encode s."""
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


def decode(enc):
    """Decode enc."""
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
