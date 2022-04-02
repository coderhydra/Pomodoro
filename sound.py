import subprocess

class sound:
    def go3():
        subprocess.call(["afplay","sounds/go_go_go.wav"])

    def jf():
        subprocess.call(["afplay","sounds/job_finished.wav"])