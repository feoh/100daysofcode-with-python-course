import json
import argparse
import fire
import time
import readchar
from pathlib import Path
from datetime import datetime

def back_to_work():
    print("Back to work!")
    print('\a')
    print('\a')


def restore_from_saved_poms(poms_file):
    config_path = Path.home() / ".config" 
    poms_file = config_path / "Pomodoro.json"
    print(f"config_path: {config_path} poms_file: {poms_file}")

    try:
        with open(poms_file,'r') as pfile:
            print(f"Reloading saved Pomodoros from {poms_file}")
            return(json.load(pfile))
    except OSError:
        print("No previously stored Pomodoros! Welcome!")
        return {}

def check_break_time(completed_poms, mini_break_time, long_break_time):
    if (completed_poms / 4) == 0:
        return(long_break_time, "long")
    else:
        return(mini_break_time, "short")


def start(mini_break_time, long_break_time):
    # A single Pomodoro is 25 minutes long.
    pomodoro_seconds = 60 * 25
    completed_poms = 0

    Pomodoros = restore_from_saved_poms(poms_file)

    start_time = datetime.now()
    Pom={}
    Pom['start_time'] = str(start_time)
    Pom['interrupts'] = 0

    try:
        print("Pomodoro timer starting! Hit any key when done. Hit 'Ctrl-c' to log an interrupt.")
        while True:
            print(f"Starting next Pomodoro at: {str(datetime.now())}")
            time.sleep(pomodoro_seconds)
            completed_poms = completed_poms + 1
            print(f"{completed_poms} pomodoros complete!")
            print('\a')
            (length, description) = check_break_time(completed_poms, long_break_time, mini_break_time)
            back_to_work()

    except KeyboardInterrupt:
        end_time = datetime.now()

        elapsed = end_time - start_time
        pom_seconds = elapsed.seconds

        print("Ending session. Hit 'i' if this was an interrupt. 'q' to end session.")
        interrupt_prompt = readchar.readchar()

        if interrupt_prompt == 'i':
            Pom['interrupts'] = pom['interrupts'] + 1
            print("Press any key when ready to resume.")
            _=readchar.readchar()
            continue
        elif interrupt_prompt == 'q':
            break
        else:
            raise(KeyboardInterrupt)


        print(f"Pom seconds: {pom_seconds} Finished poms: {completed_poms}")

        Pom['end_time'] = str(end_time)
        Pom['elapsed'] = str(elapsed)
        Pom['completed'] = completed_poms

        Pomodoros.append(Pom)
        with open(poms_file,'w') as pfile:
            json.dump(Pomodoros, pfile)

        

if __name__ == '__main__':
    fire.Fire(start)
