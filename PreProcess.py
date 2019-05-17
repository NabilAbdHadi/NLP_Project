import re

z = open("Tweets_Project.txt", "r")
y = r"    \"text\" : |\"|\n|\\|@[^ ]* "
x = "\"_id\"|/\* . \*/|/\* .. \*/|/\* ... \*/|/\* .... \*/|\{|\}"
w = list(filter(None, (re.sub(y, "", a) for a in z if not re.search(x, a))))  # Find tweets

for x in range(1000):  # Check tweets for URL
    result = re.sub(r"http\S+", "", w[x])
    w[x] = ""
    w[x] = result

for x in range(1000):  # Check for username
    result = re.sub('@[^\s]+', '', w[x])
    w[x] = ""
    w[x] = result

TextArray = dict((a + 1, w[a]) for a in range(1000))

[print(a, "\t: ", TextArray[a]) for a in TextArray]
with open("new file2", "w+") as f:
    # f.write('\n'.join('{}\t: {}'.format(x,TextArray[x]) for x in TextArray))
    f.writelines("\n".join((TextArray[a]) for a in TextArray))
