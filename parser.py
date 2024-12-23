# -*- encoding: utf-8 -*-
import re


def main(path, what_line):
    """
    Finds something in text file and printing in terminal
    :param path:
    :param what_line:
    :return:
    """
    data = []
    timer = []
    text = []
    structures_with_text_and_digital = []
    with open(path, "r", encoding="UTF-8") as f:
        res_line = ""
        big_string = f.read().split("\n")

    for line in big_string:
        # if finds some subline in line
        if re.search(rf"{what_line}", line.lower()):

            data = re.findall(r'\d\d\d\d-\d\d-\d\d', line)
            timer = re.findall(r'\d\d:\d\d:\d\d', line)
            text = re.findall(r'\w+', line)
            structures_with_text_and_digital = re.findall(r'[{[(][\w\s\d"-:]+[])}]', line)
            print(structures_with_text_and_digital)

    # if you need to save, result
    if data and timer and text and structures_with_text_and_digital:
        res_string = (" ".join(data) + " " + " ".join(timer) + " " + " ".join(text) +
                      " ".join(structures_with_text_and_digital))

        saver(res_string)


def saver(log):
    with open("res.txt", "a", encoding="utf-8") as f:
        f.write(log)


if __name__ == "__main__":
    what_line = "some text in line"
    path = "some_file.txt"
    main(path, what_line)
