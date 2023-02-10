# button-phone-encoder
Utility that encodes strings to a button phone notation.
## About
Converts text into a sequence of keys that you press on a push-button telephone to type that text.
## Examples
To type symbol `a` you press key with number 2 once. So, `a` is encoded as `2`

To type `e` you press key 3 twice, so it's encoded as `33`.

Similarly `dog` encodes as `36664`. (`d` as `3`, `o` as `666`, `g` as `4`).

If adjacent letters are encoded with a same digits, a `+` is inserted between them. For example, `cat` is encoded as `222+28`.

Space is encoded as `1`.

To encode numbers symbol `#` is inserted in front of them. For example, `345` is encoded as `#3#4#5`
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
> python encoder.py "my phone is 1234"
69991744666+6633144477771#1#2#3#4
```
### Decoding
```shell
> python encoder.py -d "69991744666+6633144477771#1#2#3#4"
my phone is 1234
```
