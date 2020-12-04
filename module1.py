from pprint import pprint

from hesiod import get_cfg_copy, get_out_dir


def func1():
    cfg = get_cfg_copy()
    print("This is the global config for this run (if you need it):")
    pprint(cfg)

    print("\n")

    out_dir = get_out_dir()
    print("Instead, this is the output dir for the current run:")
    print("-->", str(out_dir))
