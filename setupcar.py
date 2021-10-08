import argparse
from shutil import copyfile
import os


def main(sd_path):
    if not os.path.exists(os.path.join(sd_path, "etc/rc.local")):
        print("You probably entered the wrong SD path...")
        print("It probably looks like: /media/<username>/rootfs/")
        return

    copyfile(os.path.join("files", "test.py"), os.path.join(sd_path, "home/pi/test.py"))
    copyfile(os.path.join("files", "say_ip.py"), os.path.join(sd_path, "home/pi/say_ip.py")) 
    copyfile(os.path.join("files", "rc.local"), os.path.join(sd_path, "etc/rc.local")) 
    copyfile(os.path.join("files", "wpa_supplicant.conf"), os.path.join(sd_path, "etc/wpa_supplicant/wpa_supplicant.conf"))

    print("Finish copying files...")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sdpath", help="Path to SD card")
    args = parser.parse_args()
    main(args.sdpath)
