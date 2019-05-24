import json
import argparse
from pathlib import Path
from datetime import datetime

class PomPom:
    def start(self):
        config_path = Path.home() / ".config" 
        poms_file = config_path / "Pomodoro.json"
        print(f"config_path: {config_path} poms_file: {poms_file}")
        Pomodoros = []

        start_time = str(datetime.now())
        Pom={}
        Pom['start_time'] = start_time
        Pomodoros.append(Pom)
        with open(poms_file,'w') as pfile:
            json.dump(Pomodoros, pfile)

if __name__ == '__main__':
    p = PomPom()
    p.start()
