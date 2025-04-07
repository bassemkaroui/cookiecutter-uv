import sys

try:
    from ._version import version
except ImportError:  # pragma: no cover
    print(f"{__name__} version is unknown (package is not installed)")
    sys.exit(1)

__version__ = version
