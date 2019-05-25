import json
import argparse
import fire
import readchar
from pathlib import Path
from datetime import datetime

class PomPom:
    def start(self):
        config_path = Path.home() / ".config" 
        poms_file = config_path / "Pomodoro.json"
        print(f"config_path: {config_path} poms_file: {poms_file}")
        Pomodoros = []

        try:
            with open(poms_file,'r') as pfile:
                Pomodoros = json.load(pfile)
        except OSError:
            print("No previously stored Pomodoros! Welcome!")

        start_time = datetime.now()
        Pom={}
        Pom['start_time'] = str(start_time)

        print("Pomodoro timer starting! Hit any key when done. Hit 'i' to log an interrupt.")

        # We should do something with this, eh? Like log an interrupt. But that would
        # requjire that it be non blocking.
        readchar.readchar()

        end_time = datetime.now()

        elapsed = end_time - start_time
        pom_seconds = elapsed.seconds
        finished_poms = (pom_seconds / 60) // 25
        print(f"Pom seconds: {pom_seconds} Finished poms: {finished_poms}")

        Pom['end_time'] = str(end_time)
        Pom['elapsed'] = str(elapsed)
        Pom['completed'] = finished_poms

        Pomodoros.append(Pom)
        with open(poms_file,'w') as pfile:
            json.dump(Pomodoros, pfile)

        

if __name__ == '__main__':
    fire.Fire(PomPom)
