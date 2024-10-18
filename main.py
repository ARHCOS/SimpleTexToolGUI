import customtkinter as ctk
import os
import subprocess
from tkinterdnd2 import DND_FILES, TkinterDnD

def update_variable(button_name, button_value):
    global selected_variable
    selected_variable = button_value
    variable_label.configure(text=f"Selected Conversion: {button_name}")

def drop(event):
    file_path = event.data
    if os.path.isfile(file_path):
        global selected_file_path
        selected_file_path = file_path
        file_path_label.configure(text=f"Dropped file: {file_path}")

def run_other_script():
    if selected_variable and selected_file_path:
        print(f"Running with {selected_variable} and {selected_file_path}")
        
        file_name_with_ext = os.path.basename(selected_file_path)
        file_name = os.path.splitext(file_name_with_ext)[0]
        file_extension = os.path.splitext(selected_file_path)[1]
        path = os.path.dirname(selected_file_path)
        
        print(f"Full File Path: {selected_file_path}")
        print(f"File Path: {path}")
        print(f"File Name: {file_name}")
        print(f"Selected Conversion: {selected_variable}")

        script_directory = os.path.join(os.path.dirname(__file__), "scripts")
        script_path = os.path.join(script_directory, 'conversion.py')

        result = subprocess.run(['python', script_path, selected_file_path, path, file_name, selected_variable])
        
        if result.returncode == 0:
            print("Script executed")
        else:
            print(f"Error running script: {result.returncode}")
    else:
        print("Make sure a conversion method and a file are selected.")

root = TkinterDnD.Tk()
root.title("SimpleTexTool GUI")

root.geometry("800x600")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

main_frame = ctk.CTkFrame(root)
main_frame.pack(fill="both", padx=10, pady=10, expand=True)

left_frame = ctk.CTkFrame(main_frame)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

button1 = ctk.CTkButton(left_frame, text="ktx2png", command=lambda: update_variable("ktx2png", ".png"))
button1.pack(pady=(10, 5))

button2 = ctk.CTkButton(left_frame, text="pvr2png", command=lambda: update_variable("pvr2png", ".png"))
button2.pack(pady=(10, 5))

button3 = ctk.CTkButton(left_frame, text="png2ktx", command=lambda: update_variable("png2ktx", ".ktx"))
button3.pack(pady=(10, 20))

execute_button = ctk.CTkButton(left_frame, text="Convert", command=run_other_script)
execute_button.pack(side="bottom", pady=10)

right_frame = ctk.CTkFrame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

variable_label = ctk.CTkLabel(right_frame, text="Selected Conversion: ")
variable_label.pack(pady=10)

drop_area = ctk.CTkFrame(right_frame, fg_color="gray30")
drop_area.pack(pady=20, padx=10, fill="both", expand=True)

drop_label = ctk.CTkLabel(drop_area, text="Drag and drop a file here", bg_color="gray30")
drop_label.pack(expand=True)

drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', drop)

file_path_label = ctk.CTkLabel(right_frame, text="")
file_path_label.pack(pady=10)

selected_variable = ""
selected_file_path = ""

root.mainloop()
