import argparse
import os
import sys


from livereload import Server


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-sd', '--site_dirpath',
                        type=check_site_dirpath,
                        required=True,
                        help='path to root of the site directory')
    return parser


def check_site_dirpath(dirpath):
    if not os.path.exists(dirpath):
        raise argparse.ArgumentTypeError("{} does not exists".format(dirpath))
    return dirpath


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    server = Server()
    server.serve(root=namespace.site_dirpath)
