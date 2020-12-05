from pathlib import Path

from hesiod import hmain
from npyscreen.wgwidget import NotEnoughSpaceForWidget

from module1 import func1
from module2 import func2


@hmain(base_cfg_dir=Path("cfg/base"), run_cfg_file=Path("cfg/run.yaml"))
def main():
    print("\n********************\n")
    func1()
    print("\n********************\n")
    func2()
    print("\n********************\n")


if __name__ == "__main__":
    try:
        main()
    except NotEnoughSpaceForWidget:
        print("Please, make your terminal window bigger and try again :)")
