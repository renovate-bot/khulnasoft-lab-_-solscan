import argparse
import logging
import sys

from crytic_compile import cryticparser

from solscan.tools.doctor.utils import report_section
from solscan.tools.doctor.checks import ALL_CHECKS


def parse_args() -> argparse.Namespace:
    """
    Parse the underlying arguments for the program.
    :return: Returns the arguments for the program.
    """
    parser = argparse.ArgumentParser(
        description="Troubleshoot running Solscan on your project",
        usage="solscan-doctor project",
    )

    parser.add_argument("project", help="The codebase to be tested.")

    # Add default arguments from crytic-compile
    cryticparser.init(parser)

    return parser.parse_args()


def main() -> None:
    # log on stdout to keep output in order
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, force=True)

    args = parse_args()
    kwargs = vars(args)

    for check in ALL_CHECKS:
        with report_section(check.title):
            check.function(**kwargs)


if __name__ == "__main__":
    main()
