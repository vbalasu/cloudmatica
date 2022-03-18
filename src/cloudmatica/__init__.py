import argparse
parser = argparse.ArgumentParser(description='Cloudmatica CLI')
subparsers = parser.add_subparsers(dest='command', help='sub-command help')
parser_shorten = subparsers.add_parser('shorten',
                                       help='Create a link by shortening a long url',
                                       epilog='EXAMPLE: shorten https://example.com/my-very-long-url myshort')
parser_shorten.add_argument('url', type=str, help='The url to shorten')
parser_shorten.add_argument('short', type=str, help='The short name')
args = parser.parse_args()


def shorten(args):
    result = f'https://go.cloudmatica.com/{args.short}'
    print(result)
    return result


def main():
    import sys
    if not len(sys.argv) > 1:
        parser.print_help()
    if args.command == 'shorten':
        shorten(args)


if __name__ == '__main__':
    main()
