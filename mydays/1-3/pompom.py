import json
import argparse
import fire
import time
import readchar
from pathlib import Path
from datetime import datetime

class PomPom:

    def back_to_work():
        print("Back to work!")
        print('\a')
        print('\a')


    def start(self, mini_break_time = 3, long_break_time = 15):
        config_path = Path.home() / ".config" 
        poms_file = config_path / "Pomodoro.json"
        print(f"config_path: {config_path} poms_file: {poms_file}")
        Pomodoros = []
        # A single Pomodoro is 25 minutes long.
        pomodoro_seconds = 60 * 25
        completed_poms = 0

        try:
            with open(poms_file,'r') as pfile:
                Pomodoros = json.load(pfile)
        except OSError:
            print("No previously stored Pomodoros! Welcome!")

        start_time = datetime.now()
        Pom={}
        Pom['start_time'] = str(start_time)

        try:
            print("Pomodoro timer starting! Hit any key when done. Hit 'Ctrl-c' to log an interrupt.")
            while True:
                print(f"Starting next Pomodoro at: {str(datetime.now())}")
                time.sleep(pomodoro_seconds)
                completed_poms = completed_poms + 1
                print(f"{completed_poms} pomodoros complete!")
                print('\a')
                if (completed_poms / 4) == 0:
                    print(f"Yay you earned a long break of {long_break_time} minutes!")
                    time.sleep(long_break_time)
                else:
                    print(f"Mini break time! Get back to work in {mini_break_time} minutes!")
                    time.sleep(mini_break_time)

                back_to_work()

        except KeyboardInterrupt:
            end_time = datetime.now()

            elapsed = end_time - start_time
            pom_seconds = elapsed.seconds

            print("Ending session. Hit 'i' if this was an interrupt. Anything else to count this pom.")
            interrupt_prompt = readchar.readchar()
            if interrupt_prompt.lower() is not 'i':
                completed_poms = completed_poms + 1

            print(f"Pom seconds: {pom_seconds} Finished poms: {completed_poms}")

            Pom['end_time'] = str(end_time)
            Pom['elapsed'] = str(elapsed)
            Pom['completed'] = completed_poms

            Pomodoros.append(Pom)
            with open(poms_file,'w') as pfile:
                json.dump(Pomodoros, pfile)

        

if __name__ == '__main__':
    fire.Fire(PomPom)
