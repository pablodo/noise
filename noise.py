import re
from collections import defaultdict

regex = re.compile("\d+\/\d+\/\d+, \d+:\d+ - (.*?): (.*)")
def main(input_file, count_type):
    users = defaultdict(int)
    for line in input_file:
        match = regex.search(line)
        if match:
            user, message = match.groups()
            if count_type == 'words':
                users[user] += len(message.split(' '))
            elif count_type == 'messages':
                users[user] += 1

    for user, count in users.iteritems():
        print "%s: %s" % (user, count)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('input_file', type=argparse.FileType('r'))
    ap.add_argument('--count_type', '-t', choices=['words', 'messages'], default='words')
    args = ap.parse_args()

    main(args.input_file, args.count_type)
