import subprocess
import time
import glob
import os
import sys

print("Starting robust headless learner...")
ANALYSES_DIR = "C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend/skills/frontend-taste-learner/knowledge-base/site-analyses"

# On Windows, we must force prompt_toolkit to use the dummy output.
# We do this by launching python with a one-liner that patches sys.stdout 
# before importing hermes.
run_script = """
import sys
import os

# Create a dummy object with a flush method to satisfy prompt_toolkit
class DummyConsole:
    def write(self, *args): pass
    def flush(self): pass
    def fileno(self): return -1

sys.stdout = DummyConsole()
sys.stderr = DummyConsole()
sys.stdin = open(os.devnull, 'r')

from hermes_cli.main import main
sys.argv = ['hermes', 'chat', '-q', 'run frontend-taste-learner', '-s', 'frontend-taste-learner', '--yolo']
try:
    main()
except Exception:
    pass
"""

SESSION_COMPLETED = 0

while True:
    print("Starting fresh iteration...")
    
    subprocess.run([sys.executable, "-c", run_script])
    
    queue_path = "C:/Users/dhruv/AppData/Local/hermes/skills/world-class-frontend/skills/frontend-taste-learner/knowledge-base/queue.md"
    
    with open(queue_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "[ ]" not in content:
        count = len(glob.glob(f"{ANALYSES_DIR}/*.md"))
        print(f"Queue is empty. Total sites: {count}")
        break
            
    SESSION_COMPLETED += 1
    
    if SESSION_COMPLETED % 10 == 0:
        count = len(glob.glob(f"{ANALYSES_DIR}/*.md"))
        print(f"Completed 10 sites! Total: {count}")
        subprocess.run(["hermes", "chat", "-q", f"Update: The background learner analyzed 10 more sites. Total: {count}", "--yolo"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print("Iteration complete. Pausing 15 seconds...")
    time.sleep(15)