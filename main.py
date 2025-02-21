import customtkinter as ctk
import os
import subprocess  # For running external scripts
from tkinterdnd2 import DND_FILES, TkinterDnD

# Function to update the variable based on the pressed button
def update_variable(button_name, button_value):
    global selected_variable
    selected_variable = button_value
    variable_label.configure(text=f"Selected Conversion: {button_name}")

# Function to handle file drop
def drop(event):
    file_path = event.data
    if os.path.isfile(file_path):
        global selected_file_path
        selected_file_path = file_path
        file_path_label.configure(text=f"Dropped file: {file_path}")

# Function to run the external script with the selected variables
def run_other_script():
    if selected_variable and selected_file_path:
        print(f"[INFO] Running with {selected_variable} and {selected_file_path}")
        
        # Split the file path into name, extension, and path
        file_name_with_ext = os.path.basename(selected_file_path)  # Get the full file name with extension
        file_name = os.path.splitext(file_name_with_ext)[0]  # Get the file name without extension
        file_extension = os.path.splitext(selected_file_path)[1]  # Get the file extension
        path = os.path.dirname(selected_file_path)  # Get the directory path

        # Define the script path in the 'scripts' folder
        
        if file_extension == ".sctx":
            script_directory = os.path.join(os.path.dirname(__file__), "scripts")
            script_path = os.path.join(script_directory, 'SctxConverter.exe')
            command = f'{script_path} decode {selected_file_path}'
            if json_export == False:
                command += ' -t'
            print(command)
            try:
                result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(result.stdout.decode())
                if result.stderr:
                    print(result.stderr.decode())
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Something went wrong : {e}")
                
        elif selected_variable == ".sctx" and sctx_compression == False :
            script_directory = os.path.join(os.path.dirname(__file__), "scripts")
            script_path = os.path.join(script_directory, 'SctxConverter.exe')
            selected_file_path_without_extension = os.path.splitext(selected_file_path)[0]
            command = f'{script_path} encode {selected_file_path_without_extension}.json'
            if sctx_compression == True:
                command += ' -c'
            try:
                result = subprocess.run(command, check=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(result.stdout.decode())
                if result.stderr:
                    print(result.stderr.decode())
            except subprocess.CalledProcessError as e:
                print(f"[ERROR] Something went wrong : {e}")

        else:
            script_directory = os.path.join(os.path.dirname(__file__), "scripts")
            script_path = os.path.join(script_directory, 'conversion.py')

        result = subprocess.run([script_path, selected_file_path, path, file_name, selected_variable])

        if result.returncode == 0:
            print("[INFO] Script executed")
        else:
            print(f"[ERROR] Error running script: {result.returncode}")
    else:
        print("[INFO] Make sure a conversion method and a file are selected.")

# Function to handle the checkbox state change
def update_checkbox_state():
    global sctx_compression
    sctx_compression = bool(checkbox_var.get())
    #print(f"sc_compression state: {sctx_compression}")

def update_checkbox_state2():
    global json_export
    json_export = bool(checkbox_var2.get())
    #print(f"json_export state: {json_export}")

# Create the main window with DnD
root = TkinterDnD.Tk()
root.title("SimpleTexTool GUI")

# Set the initial window size (width x height)
root.geometry("1080x720")

# Apply dark theme and blue accents
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main container for the two top sections
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", padx=0, pady=0, expand=True)

# Left area for the buttons
left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="y", padx=10, pady=0)

# Buttons with more spacing
button1 = ctk.CTkButton(left_frame, text="ktx2png", command=lambda: update_variable("ktx2png", ".png"))
button1.pack(pady=(10, 5))

button2 = ctk.CTkButton(left_frame, text="pvr2png", command=lambda: update_variable("pvr2png", ".png"))
button2.pack(pady=(10, 5))

button3 = ctk.CTkButton(left_frame, text="png2ktx", command=lambda: update_variable("png2ktx", ".ktx"))
button3.pack(pady=(10, 5))

button4 = ctk.CTkButton(left_frame, text="sctx2png", command=lambda: update_variable("sctx2png", ".png"))
button4.pack(pady=(10, 5))

button5 = ctk.CTkButton(left_frame, text="png2sctx", command=lambda: update_variable("png2sctx", ".sctx"))
button5.pack(pady=(10, 20))

# Button to run the other script, placed at the bottom of the same container as the other buttons
execute_button = ctk.CTkButton(left_frame, text="Convert", command=run_other_script)
execute_button.pack(side="bottom", pady=10)

# Right area for file drop
right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

# Label to display the selected variable
variable_label = ctk.CTkLabel(right_frame, text="Selected Conversion: ")
variable_label.pack(pady=10)

# File drop area
drop_area = ctk.CTkFrame(right_frame, fg_color="gray30")
drop_area.pack(pady=10, padx=10, fill="both", expand=True)

# Label to indicate file drop in the drop area
drop_label = ctk.CTkLabel(drop_area, text="Drag and drop a file here", bg_color="gray30")
drop_label.pack(expand=True)

# Bind the file drop to the area
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', drop)

# Label to display the dropped file
file_path_label = ctk.CTkLabel(right_frame, text="")
file_path_label.pack(pady=10)

# Add the checkboxes
checkbox_var = ctk.IntVar()  # Variable to track the state of the checkbox
checkbox = ctk.CTkCheckBox(right_frame, text="Compress Data (png2sctx only)", variable=checkbox_var, command=update_checkbox_state)
checkbox.pack(anchor="e", padx=14)

checkbox_var2 = ctk.IntVar()  # Variable to track the state of the checkbox
checkbox2 = ctk.CTkCheckBox(right_frame, text="Export JSON file (sctx2png only)", variable=checkbox_var2, command=update_checkbox_state2)
checkbox2.pack(anchor="e", pady=10, padx=10)

# Global variables to store the selection
selected_variable = ""
selected_file_path = ""
sctx_compression = False  # Initialize the checkbox variable
json_export = False

# Start the main loop
root.mainloop()
