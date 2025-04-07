import os
import subprocess
import time

# Terminal colors
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
CYAN = '\033[1;36m'
MAGENTA = '\033[1;35m'
RESET = '\033[0m'

TOOL_DIR = "/storage/emulated/0/Fake"

def header():
    os.system("clear" if os.name == "posix" else "cls")
    print(f"{MAGENTA}=================================================={RESET}")
    print(f"{YELLOW}                Made By: {GREEN}HACKER TF{RESET}")
    print(f"{MAGENTA}=================================================={RESET}\n")

def list_py_files():
    return [f for f in os.listdir(TOOL_DIR) if f.endswith(".py")]

def show_menu(tools):
    header()
    print(f"{CYAN}Select a tool to run:\n{RESET}")
    for i, tool in enumerate(tools, 1):
        print(f"{YELLOW}[{str(i).zfill(2)}] {GREEN}{tool}{RESET}")
    print(f"\n{RED}[00] Exit{RESET}")

def run_tool(tool):
    full_path = os.path.join(TOOL_DIR, tool)
    print(f"\n{CYAN}Launching: {YELLOW}{tool}{RESET}\n")
    time.sleep(1)
    subprocess.run(["python", full_path])

def main():
    while True:
        tools = list_py_files()
        show_menu(tools)
        try:
            choice = input(f"\n{CYAN}Enter choice: {RESET}")
            if choice == "00":
                print(f"{RED}Exiting...{RESET}")
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(tools):
                run_tool(tools[int(choice) - 1])
                input(f"\n{YELLOW}Press Enter to return to menu...{RESET}")
            else:
                print(f"{RED}Invalid selection!{RESET}")
                time.sleep(1)
        except ValueError:
            print(f"{RED}Enter a valid number!{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()