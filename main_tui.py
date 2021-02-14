from pathlib import Path

from hesiod import hmain

from module1 import func1
from module2 import func2


@hmain(base_cfg_dir=Path("cfg/base"), template_cfg_file=Path("cfg/template.yaml"))
def main():
    print("\n********************\n")
    func1()
    print("\n********************\n")
    func2()
    print("\n********************\n")


if __name__ == "__main__":
    main()
