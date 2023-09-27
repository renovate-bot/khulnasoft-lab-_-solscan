import argparse

from solscan.tools.kspec_coverage.analysis import run_analysis
from solscan import Solscan


def kspec_coverage(args: argparse.Namespace) -> None:

    contract = args.contract
    kspec = args.kspec

    solscan = Solscan(contract, **vars(args))

    compilation_units = solscan.compilation_units
    if len(compilation_units) != 1:
        print("Only single compilation unit supported")
        return
    # Run the analysis on the Klab specs
    run_analysis(args, compilation_units[0], kspec)
