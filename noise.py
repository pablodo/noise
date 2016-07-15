import re
from collections import defaultdict

regex = re.compile("\d+\/\d+\/\d+, \d+:\d+ - (.*?): (.*)")
def main(input_file, count_type, separator):
    users = defaultdict(int)
    for line in input_file:
        match = regex.search(line)
        if match:
            user, message = match.groups()
            if count_type == 'words':
                users[user] += len(message.split(' '))
            elif count_type == 'messages':
                users[user] += 1
            elif count_type == 'chars':
                users[user] += sum([len(x) for x in message.split(' ')])

    for user, count in users.iteritems():
        print "%s%s%s" % (user, separator, count)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('input_file', type=argparse.FileType('r'))
    ap.add_argument('--count_type', '-t', choices=['words', 'messages', 'chars'], default='words')
    ap.add_argument('--separator', '-s', default=',')
    args = ap.parse_args()

    main(args.input_file, args.count_type, args.separator)
