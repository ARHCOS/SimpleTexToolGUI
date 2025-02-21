import sys
import subprocess
import os

def main():
    
    # Récupérer les arguments passés
    full_file_path = sys.argv[1]
    file_path = sys.argv[2]
    file_name = sys.argv[3]
    selected_variable = sys.argv[4]
    o_d = " -d "
    noout = ""
    
    if selected_variable == ".png":
        end = " -noout -ics sRGB"
        o_d = " -d "
    else:
        end = " -ics lRGB -f ETC1,SS,lRGB -q etcnormal"
        o_d = " -o "

    command = "PVRTexToolCLI.exe -i " + full_file_path + o_d + file_path + "/" + file_name + selected_variable + end
    
    #print(f"Running command: {command}")
    
    try:
        # Exécuter la commande
        result = subprocess.run(command, check=True)
        print("Command executed successfully with return code:", result.returncode)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
    except FileNotFoundError:
        print("PVRTexToolCLI.exe not found. Please ensure it is in the PATH.")

if __name__ == "__main__":
    main()
