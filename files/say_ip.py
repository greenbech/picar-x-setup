#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')
from ezblock import __reset_mcu__
from ezblock import TTS
import time
import subprocess
import socket
__reset_mcu__()
time.sleep(0.01)


from ezblock import TTS

tts = TTS()

def check_if_user_logged_in():
        number_of_ssh_processes = len(subprocess.check_output(["pgrep", "ssh"]).decode().strip().split("\n"))
        number_of_logged_in_users = len([x for x in subprocess.check_output(["who"]).decode().strip().split("\n") if x])
        if number_of_ssh_processes > 1 or number_of_logged_in_users > 0:
            sys.exit(0)

def run():
    while True:
        check_if_user_logged_in()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("google.no", 80))
            ip = s.getsockname()[0]
            tts.say("ssh")
            check_if_user_logged_in()
            tts.say("pi")
            check_if_user_logged_in()
            tts.say("@")
            check_if_user_logged_in()
            parts = ip.split(".")
            for i, part in enumerate(parts):
                tts.say(part)
                if i < 3:
                    check_if_user_logged_in()
                    tts.say("dot")
            check_if_user_logged_in()
            time.sleep(0.5)
            check_if_user_logged_in()
            tts.say(f"password raspberry")
            s.close()
            time.sleep(3)
        except Exception as e:
            tts.say(str(e))
            tts.say("Trying to connect to wireless network with SSID cognitehackathon password cognite123")
            time.sleep(3)


if __name__ == "__main__":
    run()  