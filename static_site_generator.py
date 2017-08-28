import argparse
import os
import sys


from staticjinja import make_site


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
                        '-t', '--templates_dirpath',
                        type=check_dirpath,
                        default='templates/',
                        help='path to the root of templates to be generated'
                        )
    parser.add_argument(
                        '-g', '--generated_site',
                        type=check_dirpath,
                        default='src/',
                        help='path to the root of the generated site'
                        )
    parser.add_argument(
                        '-s', '--static_pathes',
                        nargs='*',
                        default=None,
                        help='list of pathes to the static files relative \
                              to the templates dirpath'
                        )
    return parser


def check_dirpath(dirpath):
    if not os.path.exists(dirpath):
        raise argparse.ArgumentTypeError("{} does not exists".format(dirpath))
    return dirpath


def check_static_relativness_to_templates(templates_dirpath, static_pathes):
    for path in static_pathes:
        static_path = os.path.join(templates_dirpath, path)
        if not os.path.exists(static_path):
            raise argparse.ArgumentTypeError(
                "{} does not exists or is not relative to {}"
                .format(static_path, templates_dirpath)
                )


def obtain_args():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.static_pathes:
        check_static_relativness_to_templates(
            namespace.templates_dirpath,
            namespace.static_pathes,
            )
    return namespace


if __name__ == "__main__":
    namespace = obtain_args()
    site = make_site(
        searchpath=namespace.templates_dirpath,
        outpath=namespace.generated_site,
        staticpaths=namespace.static_pathes,
    )
    site.render(use_reloader=True)
