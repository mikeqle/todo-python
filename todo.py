# main.py

import os
from task_manager import add_task, display_tasks, remove_task

def clear_screen():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS and Linux
        os.system("clear")

def main():
    last_message = ""

    while True:
        clear_screen()
        if last_message:
            print(last_message)
            last_message = ""

        print("\nTo-do List Manager")
        print("-------------------")
        display_tasks()

        try:
            user_input = input("Enter a new task, 'r' to remove a task, or 'q' to quit: ").strip()

            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 'r':
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    remove_task(task_number)
                    last_message = "Task removed successfully."
                except ValueError:
                    last_message = "Invalid input. Please enter a valid task number."
            else:
                add_task(user_input)
                last_message = "Task added successfully."
        except KeyboardInterrupt:
            last_message = "Interrupt detected. Restarting task input."
            continue

if __name__ == "__main__":
    main()
