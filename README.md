**PATTERNS:**

Some syntax:

1) r"\W" - spec chars without '_' | r"\w" - alphabetic chars or digital or '\_'
2) r"\d" - digital | r"\D" - not digital
3) r"\s" - space | r"\S" - not space
4) r"." - any char
5) r"\b" - word boundary
6) r"\B" - not word boundary

If you need to find the desired special char in text, you need to escape it using '\'

example: r'\[\]\{\}' - finds: []{}

Special syntax. Use after an expression.:

1) \+ -  Involves 1 or more inclusions | r'\w+' - 1 or more alphanet chars
2) \? - zero or 1 inclusions | r'\w?'
3) \* - zero or more inclusions | r'\w*'
4) ^ - implies the beginning of a line | r'^\w+'
5) $ - implies end of line | r'\w+$'
6) ^ in [] - not | r'\[^\d]' - some not digital

Quantifiers:

1) {n} - exactly 'n' times | r'\w{4}' - finds words with 4 chars
2) {n, m} - from 'm' to 'n' inclusive | r'\w{1, 4}'  - finds words with 1, 2, 3 or 4 chars
3) {n,} - not less than 'n' | r'\w{1,}' - finds words with 1 or more chars
4) {,m} - not more than 'm' | r'\w{,4}'


If you need to find some data in "{...}":

>r"\{.*\}"

If you need some structure, for example coordinates in (x, y, z):

>r'\{"\w+": [-\d]+, "\w+": [-\d]+, "\w+": [-\d]+\}'


Data for YYYY-DD-MM:

>r"(?:\d{4})-(?:\d{2})-(?:\d{2})"

>r"[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"

>r"\d\d\d\d-\d\d-\d\d"

Time HH:MM:SS:

>r"(?:\d{2}):(?:\d{2}):(?:\d{2})"

>r"[0-9][0-9]-[0-9][0-9]-[0-9][0-9]"

>r"\d\d-\d\d-\d\d"

Capitalize text with spaces in quotes:

>r'"[А-ЯA-Z][\w\s]+"*'

lower text with spaces in quotes:

>r'"[а-яa-z][\w\s]+"*'

Text or (text + space + numbers) in quotes:

>r'"[a-zA-Zа-яА-Я]+"|"[a-zA-Zа-яА-Я]+ \d+"'

Numbers in quotes:

>r'"[0-9]+"'

For more information:

Eng doc: [Python regex](https://docs.python.org/3/howto/regex.html)

Rus: [Регулярные выражения (regexp) — основы](https://habr.com/ru/articles/545150/)