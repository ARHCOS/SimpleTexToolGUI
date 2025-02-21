import subprocess
import sys
import os

def install_modules(modules):
    """Installe les modules pip listés."""
    for module in modules:
        print(f"Installing : {module}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# Liste des modules à installer
modules_to_install = ['customtkinter', 'tkinterdnd2']  # Remplacer par vos modules

current_folder = os.path.dirname(os.path.abspath(__file__))
script_folder = os.path.join(current_folder, 'scripts')

# Vérifie si le dossier "scripts" existe
if not os.path.exists(script_folder):
    print(f"The 'script' folder does not exist : {script_folder}")
else:
    # Installer les modules
    install_modules(modules_to_install)