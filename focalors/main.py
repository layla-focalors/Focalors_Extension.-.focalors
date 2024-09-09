import argparse
from focalors.decompress import decompress_file
from focalors.compress import compress_file

def mainParser():
    parser = argparse.ArgumentParser(description='Focalors Command Line Tool')
    subparsers = parser.add_subparsers(dest='command')
    
    decompress_parser = subparsers.add_parser('decompress', help='Decompress a file')
    decompress_parser.add_argument('file', type=str, help='The file to decompress')
    decompress_parser.add_argument('--output', type=str, default='output.txt', help='The output file')
    
    compress_parser = subparsers.add_parser('compress', help='Compress a file')
    compress_parser.add_argument('file', type=str, help='The file to compress')
    compress_parser.add_argument('--output', type=str, default='output.txt', help='The output file')
    
    args = parser.parse_args()

    if args.command == 'decompress':
        decompress_file(args.file, args.output)
    elif args.command == 'compress':
        compress_file(args.file, args.output)
    else:
        print("Unknown command")

if __name__ == '__main__':
    mainParser()
