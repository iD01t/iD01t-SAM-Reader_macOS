import subprocess
import tkinter as tk
from PIL import ImageTk, Image

# Function to execute shell commands and get output
def execute_command(command):
    print(f"Executing command: {command}")
    try:
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode('utf-8') + stderr.decode('utf-8')
        return output.strip()
    except FileNotFoundError:
        return "Command not found. Ensure the command is installed and in your PATH."
    except Exception as e:
        return str(e)

# Function to detect device and gather information
def detect_device():
    # Gather device information
    commands = {
        "Brand": "adb shell getprop ro.product.brand",
        "Name": "adb shell getprop ro.product.model",
        "Hardware": "adb shell getprop ro.hardware",
        "Software": "adb shell getprop ro.build.version.release",
        "FRP Lock State": "adb shell getprop ro.security.vpndialogs",
        "Knox Lock State": "adb shell getprop ro.secure",
        "IMEI": "adb shell service call iphonesubinfo 1",
        "Network Type": "adb shell getprop gsm.network.type",
    }

    results = {}
    for key, command in commands.items():
        results[key] = execute_command(command)

    # Format the output
    device_info = "\n".join([f"{key}: {value}" for key, value in results.items()])

    # Update the text widget
    device_info_text.delete(1.0, tk.END)
    device_info_text.insert(tk.END, device_info)

# Define the recovery function to execute the shell script
def recovery():
    command = "bash iD01t_recovery.sh"
    output = execute_command(command)
    
    # Log the output of the shell script (if needed)
    print(output)
    
    # Add confirmation message in the text widget
    device_info_text.insert(tk.END, "\nDevice sent into Recovery Mode successfully.")

# Create the main application window
root = tk.Tk()
root.title('iD01t SAM Reader 1.0')
root.configure(background='black')

frame = tk.Frame(root, width="788", height="444", background="black")
frame.pack(fill=tk.BOTH, expand=True)

bg_image = Image.open("background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(frame, width="788", height="444", image=bg_photo, bg="black")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Button to read device information
read_button = tk.Button(
    frame,
    text="Read Device Information",
    command=detect_device,
    background="#333333",
    foreground="black",
    font=('Helvetica', 12, 'bold'),
    relief=tk.RAISED,
    padx=10,
    pady=5
)
read_button.place(x=400, y=310)

# Button to execute recovery mode
send_button = tk.Button(
    frame,
    text="         Recovery Mode        ",
    command=recovery,
    background="#333333",
    foreground="black",
    font=('Helvetica', 12, 'bold'),
    relief=tk.RAISED,
    padx=10,
    pady=5
)
send_button.place(x=400, y=380)

# Text widget to display device information
device_info_text = tk.Text(
    frame,
    width=59,
    height=14,
    background="black",
    foreground="white",
    font=('Helvetica', 12)
)
device_info_text.place(x=294, y=80)

root.geometry("788x444")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')
root.iconphoto(False, tk.PhotoImage(file='bootlogo (1).png'))

root.mainloop()
