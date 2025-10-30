import argparse
from .interactive import interactive_peano

def main():
    parser = argparse.ArgumentParser(
        prog="peano-viewer",
        description="Interactive Peano–Morton curve viewer"
    )
    parser.add_argument(
        "--base", type=int, default=3,
        help="Base for Morton/Peano interleave (default: 3)"
    )
    parser.add_argument(
        "--order", type=int, default=6,
        help="Maximum order (default: 6)"
    )
    parser.add_argument(
        "--interval", type=int, default=10,
        help="Animation interval in ms (default: 10)"
    )

    args = parser.parse_args()

    interactive_peano(base=args.base, max_order=args.order, interval=args.interval)

if __name__ == "__main__":
    main()
