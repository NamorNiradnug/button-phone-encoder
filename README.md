# button-phone-encoder
Utility that encodes strings to a button phone notation.
## About
Converts text to a sequence of keys that you need to press on a push-button telephone to type this text.

## Examples
To type symbol `a` you need to press key with number 2 once. So, `a` encodes as `2`

To type `e` you need to press key 3 twice, so it encodes as `33`.

Similarly `dog` encodes as `36664`. (`d` as `3`, `o` as `666`, `g` as `4`).

In case which nearby letters encodes with a same numbers inserts `+` between them. For example, `cat` encodes as `222+28`.

Space encodes as "1".

## Usage
### help
```shell
> python encoder.py -h
usage: encoder.py [-h] [-d] string

Utility that encodes strings to a button phone notation.

positional arguments:
  string

optional arguments:
  -h, --help    show this help message and exit
  -d, --decode  decoding mode (default is encoding)
```
### Encoding
```shell
> python encoder.py "phone"
744666+6633
```
### Decoding
```shell
> python encoder.py -d "744666+6633"
phone
```