#TASK 1
#TO DO LIST

import json
import os
from datetime import datetime


class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()

    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except:
                return []
        return []

    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as file:
            json.dump(self.todos, file, indent=2)

    def add_todo(self, task):
        """Add a new todo item"""
        todo = {
            'id': len(self.todos) + 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'completed_at': None
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✓ Task Added: {task}")

    def view_todos(self):
        """Display all todos"""
        if not self.todos:
            print("📭 No tasks in your to-do list!")
            return

        print("\n" + "=" * 50)
        print("📋 YOUR TO-DO LIST")
        print("=" * 50)

        for todo in self.todos:
            status = "✓" if todo['completed'] else "○"
            status_color = "\033[92m" if todo['completed'] else "\033[93m"  # Green/Yellow
            print(f"{status_color}{status}\033[0m [{todo['id']}] {todo['task']}")
            if todo['completed'] and todo['completed_at']:
                print(f"   Completed on: {todo['completed_at']}")
        print("=" * 50)
        print(f"Total: {len(self.todos)} | Completed: {sum(1 for t in self.todos if t['completed'])}")

    def mark_complete(self, todo_id):
        """Mark a todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                if not todo['completed']:
                    todo['completed'] = True
                    todo['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")
                    self.save_todos()
                    print(f"✓ Completed: {todo['task']}")
                else:
                    print(f"⚠ Already completed: {todo['task']}")
                return
        print("❌ Task not found!")

    def delete_todo(self, todo_id):
        """Delete a todo item"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                removed = self.todos.pop(i)
                # Reassign IDs
                for j, t in enumerate(self.todos, 1):
                    t['id'] = j
                self.save_todos()
                print(f"🗑 Removed: {removed['task']}")
                return
        print("❌ Task not found!")


def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 40)
    print("📝 TO-DO LIST MANAGER")
    print("=" * 40)
    print("1. ➕ Add new task")
    print("2. 👁 View all tasks")
    print("3. ✓ Mark task as complete")
    print("4. 🗑 Delete task")
    print("5. 🚪 Exit")
    print("=" * 40)


def main():
    todo_list = TodoList()

    while True:
        display_menu()

        try:
            choice = input("\nChoose option (1-5): ").strip()

            if choice == '1':
                task = input("Enter new task: ").strip()
                if task:
                    todo_list.add_todo(task)
                else:
                    print("❌ Task cannot be empty!")

            elif choice == '2':
                todo_list.view_todos()

            elif choice == '3':
                todo_list.view_todos()
                if todo_list.todos:
                    try:
                        todo_id = int(input("\nEnter task number to mark complete: "))
                        todo_list.mark_complete(todo_id)
                    except ValueError:
                        print("❌ Please enter a valid number!")

            elif choice == '4':
                todo_list.view_todos()
                if todo_list.todos:
                    try:
                        todo_id = int(input("\nEnter task number to delete: "))
                        todo_list.delete_todo(todo_id)
                    except ValueError:
                        print("❌ Please enter a valid number!")

            elif choice == '5':
                print("\n👋 Goodbye! Have a productive day!")
                break

            else:
                print("❌ Invalid choice! Please enter 1-5")

        except KeyboardInterrupt:
            print("\n\n👋 Exiting...")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":

    main()
