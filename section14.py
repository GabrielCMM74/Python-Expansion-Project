import re
# REGEX

string = 'search inside here'
print(re.search('search', string))
# pattern search findall, full match.
# regex playground
pw = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")

# Debugging
# Linting helps to make sure were not making a mistake
