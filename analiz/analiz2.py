import os
import yime

def monitor_directory(directory):
    before = dict([(f, None) for f in os.listdir(directory)])
    while True:
        time.sleep(5)
        after = dict([(f, None) for f in os.listdir(directory)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added:
            print("added: ", ", ".join(added))
        if removed:
            print("removed: ", ", ".join(removed))
        before = after

if __name__ = "__main__":
    monitor_directory("/path/to/monitor")
