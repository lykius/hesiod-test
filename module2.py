from pprint import pprint

from hesiod import hcfg


def func2():
    print("Let's get some values from the config:\n")

    keys = ["optimizer", "dataset.name", "net.ckpt_path", "params.p3", "params.p3.asfloat"]
    for key in keys:
        print("Key:", key)
        pprint(hcfg(key))
        print("")

    print("If you know the type of a config, you can use it to help your linter.")
    value = hcfg("params.p2", int)
    print(f'For instance, if I run hcfg("params.p2", int), I get {value}, of type {type(value)}.')
