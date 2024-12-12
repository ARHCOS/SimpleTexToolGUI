import subprocess
import sys
import os

def install_modules(modules):
    for module in modules:
        print(f"Installing : {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

def run_script(script_path):
    print(f"Running {script_path} ...")
    subprocess.run([sys.executable, script_path])

modules_to_install = ['requests', 'customtkinter', 'tkinterdnd2', 'mega.py', 'Pillow', 'pylzham', 'texture2ddecoder', 'zstandard']

current_folder = os.path.dirname(os.path.abspath(__file__))
script_folder = os.path.join(current_folder, 'scripts')

script_to_run = os.path.join(script_folder, 'fetching.py')

if not os.path.exists(script_folder):
    print(f"The 'script' folder does not exist : {script_folder}")
else:
    install_modules(modules_to_install)

    run_script(script_to_run)
