from datetime import datetime
from bisect import insort


class TaskManager:
    def __init__(self):
        self.task_dict = {}  # Dùng dict để tra cứu nhanh O(1)
        self.task_list = []  # Dùng list để duy trì thứ tự

    def add_task(self, task_name, due_time, priority):
        """Thêm công việc mới với kiểm tra ràng buộc."""
        if len(task_name) > 100:
            print("Task name too long (max 100 characters)")
            return self.task_list

        if task_name not in self.task_dict:
            try:
                due_time_obj = datetime.strptime(due_time, "%Y-%m-%d %H:%M")
                if due_time_obj <= datetime.now():
                    print("Invalid due time: Must be in the future")
                elif priority not in [1, 2, 3]:
                    print("Invalid priority: Must be 1, 2, or 3")
                elif not task_name or not due_time:
                    print("Task name and due time cannot be empty")
                else:
                    task = {'name': task_name, 'due': due_time_obj, 'priority': priority}
                    self.task_dict[task_name] = task
                    insort(self.task_list, task, key=lambda x: (-x['priority'], x['due']))
                    print("Task added successfully")
            except ValueError:
                print("Invalid time format. Use YYYY-MM-DD HH:MM (e.g., 2025-04-04 15:00)")
        else:
            print("Task already exists")
        return self.task_list

    def remove_task(self, task_name):
        """Xóa công việc theo tên."""
        if task_name in self.task_dict:
            task = self.task_dict.pop(task_name)
            self.task_list.remove(task)  # List đã có thứ tự, không cần sort lại
            print("Task removed successfully")
        else:
            print("Task not found")
        return self.task_list

    def display_tasks(self):
        """Hiển thị danh sách công việc đã sắp xếp."""
        if not self.task_list:
            print("No tasks available")
        else:
            print("\n--- Task List ---")
            for i, task in enumerate(self.task_list, 1):
                print(
                    f"{i}. Task: {task['name']}, Due: {task['due'].strftime('%Y-%m-%d %H:%M')}, Priority: {task['priority']}")
            print("-----------------\n")


def main():
    """Giao diện dòng lệnh để người dùng tương tác."""
    manager = TaskManager()
    while True:
        print("1. Add Task\n2. Remove Task\n3. Display Tasks\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter task name: ")
            due = input("Enter due time (YYYY-MM-DD HH:MM): ")
            try:
                priority = int(input("Enter priority (1-3): "))
                manager.add_task(name, due, priority)
            except ValueError:
                print("Priority must be a number between 1 and 3")

        elif choice == '2':
            name = input("Enter task name to remove: ")
            manager.remove_task(name)

        elif choice == '3':
            manager.display_tasks()

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()