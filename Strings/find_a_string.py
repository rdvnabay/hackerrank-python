import re


def count_substring(string, sub_string):
    result = re.findall(sub_string, string)
    return len(result)


output = count_substring("ABCDCDC", "CDC")
print(output)
