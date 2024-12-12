import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from employee import Employee, Language
from employee_json_handler import EmployeeJSONHandler

class EmployeeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Management")
        self.geometry("600x600")

        self.create_widgets()

    def create_widgets(self):
        # Create a notebook (tab container)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Create tabs
        self.search_tab = ttk.Frame(self.notebook)
        self.add_tab = ttk.Frame(self.notebook)
        self.update_tab = ttk.Frame(self.notebook)
        self.delete_tab = ttk.Frame(self.notebook)
        self.language_search_tab = ttk.Frame(self.notebook)



        # Add tabs to the notebook
        self.notebook.add(self.search_tab, text="Search")
        self.notebook.add(self.add_tab, text="Add Employee")
        self.notebook.add(self.update_tab, text="Update Employee")
        self.notebook.add(self.delete_tab, text="Delete Employee")
        self.notebook.add(self.language_search_tab, text="Search by Language")


        self.create_search_widgets()

        self.create_add_widgets()

        self.create_update_widgets()

        self.create_delete_widgets()

        self.create_language_search_widgets()


    def create_search_widgets(self):
        self.search_label = tk.Label(self.search_tab, text="Search by Employee ID or Designation:")
        self.search_label.pack(pady=10)

        self.search_entry = tk.Entry(self.search_tab)
        self.search_entry.pack(pady=5)

        self.search_button = tk.Button(self.search_tab, text="Search", command=self.search_employee)
        self.search_button.pack(pady=5)

        self.result_text = tk.Text(self.search_tab, height=10, width=50)
        self.result_text.pack(pady=10)

    def create_add_widgets(self):
        self.first_name_label = tk.Label(self.add_tab, text="First Name:")
        self.first_name_label.pack(pady=5)
        self.first_name_entry = tk.Entry(self.add_tab)
        self.first_name_entry.pack(pady=5)

        self.last_name_label = tk.Label(self.add_tab, text="Last Name:")
        self.last_name_label.pack(pady=5)
        self.last_name_entry = tk.Entry(self.add_tab)
        self.last_name_entry.pack(pady=5)

        self.employee_id_label = tk.Label(self.add_tab, text="Employee ID:")
        self.employee_id_label.pack(pady=5)
        self.employee_id_entry = tk.Entry(self.add_tab)
        self.employee_id_entry.pack(pady=5)

        self.designation_label = tk.Label(self.add_tab, text="Designation:")
        self.designation_label.pack(pady=5)
        self.designation_entry = tk.Entry(self.add_tab)
        self.designation_entry.pack(pady=5)

        self.language_label = tk.Label(self.add_tab, text="Languages (comma separated, e.g., Java:90, C#:80):")
        self.language_label.pack(pady=5)
        self.language_entry = tk.Entry(self.add_tab)
        self.language_entry.pack(pady=5)

        self.add_button = tk.Button(self.add_tab, text="Add New Employee", command=self.add_employee)
        self.add_button.pack(pady=5)

    def create_update_widgets(self):
        self.first_name_label = tk.Label(self.update_tab, text="First Name:")
        self.first_name_label.pack(pady=5)
        self.first_name_entry = tk.Entry(self.update_tab)
        self.first_name_entry.pack(pady=5)

        self.last_name_label = tk.Label(self.update_tab, text="Last Name:")
        self.last_name_label.pack(pady=5)
        self.last_name_entry = tk.Entry(self.update_tab)
        self.last_name_entry.pack(pady=5)

        self.employee_id_label = tk.Label(self.update_tab, text="Employee ID:")
        self.employee_id_label.pack(pady=5)
        self.employee_id_entry = tk.Entry(self.update_tab)
        self.employee_id_entry.pack(pady=5)

        self.designation_label = tk.Label(self.update_tab, text="Designation:")
        self.designation_label.pack(pady=5)
        self.designation_entry = tk.Entry(self.update_tab)
        self.designation_entry.pack(pady=5)

        self.language_label = tk.Label(self.update_tab, text="Languages (comma separated, e.g., Java:90, C#:80):")
        self.language_label.pack(pady=5)
        self.language_entry = tk.Entry(self.update_tab)
        self.language_entry.pack(pady=5)

        self.update_button = tk.Button(self.update_tab, text="Update Employee", command=self.update_employee)
        self.update_button.pack(pady=5)

    def create_delete_widgets(self):
        self.delete_label = tk.Label(self.delete_tab, text="Enter Employee ID to delete:")
        self.delete_label.pack(pady=10)

        self.delete_entry = tk.Entry(self.delete_tab)
        self.delete_entry.pack(pady=5)

        self.delete_button = tk.Button(self.delete_tab, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack(pady=5)

    def create_language_search_widgets(self):
        self.language_label = tk.Label(self.language_search_tab, text="Enter Language (e.g., Java):")
        self.language_label.pack(pady=10)

        self.language_entry = tk.Entry(self.language_search_tab)
        self.language_entry.pack(pady=5)

        self.score_label = tk.Label(self.language_search_tab, text="Enter Minimum Score (greater than 50):")
        self.score_label.pack(pady=5)

        self.score_entry = tk.Entry(self.language_search_tab)
        self.score_entry.pack(pady=5)

        self.search_button = tk.Button(self.language_search_tab, text="Search", command=self.search_by_language)
        self.search_button.pack(pady=5)

        self.language_result_text = tk.Text(self.language_search_tab, height=10, width=50)
        self.language_result_text.pack(pady=10)

    def search_by_language(self):
        language = self.language_entry.get().strip()
        min_score_str = self.score_entry.get().strip()

        if not language or not min_score_str:
            messagebox.showwarning("Input Error", "Please enter both language and minimum score.")
            return

        try:
            min_score = int(min_score_str)
            if min_score < 0:
                messagebox.showwarning("Invalid Score", "Score must be greater than 0.")
                return
            employees = EmployeeJSONHandler.read_employees()
            filtered_employees = []

            for emp in employees:
                if emp.get('KnownLanguages'):
                    for lang in emp['KnownLanguages']:
                        if lang['LanguageName'].lower() == language.lower() and lang['ScoreOutof100'] > min_score:
                            filtered_employees.append(emp)
                            break
            filtered_employees.sort(key=lambda emp: emp['EmployeeID'])

            # Display results in the result_text
            self.language_result_text.delete(1.0, tk.END)
            if filtered_employees:
                for emp in filtered_employees:
                    self.language_result_text.insert(tk.END,
                                                     f"ID: {emp['EmployeeID']}, Name: {emp['FirstName']} {emp['LastName']}, Designation: {emp['Designation']}\n")
                    for lang in emp['KnownLanguages']:
                        if lang['LanguageName'].lower() == language.lower():
                            self.language_result_text.insert(tk.END, f"  {lang['LanguageName']}: {lang['ScoreOutof100']}\n")
                    self.language_result_text.insert(tk.END, "\n")
            else:
                self.language_result_text.insert(tk.END, "No employees found with the given criteria.\n")

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for the score.")

    def search_employee(self):
        search_term = self.search_entry.get()
        if search_term:
            results = EmployeeJSONHandler.search_employee(search_term)
            self.result_text.delete(1.0, tk.END)
            if results:
                for emp in results:
                    self.result_text.insert(tk.END, f"ID: {emp['EmployeeID']}, Name: {emp['FirstName']} {emp['LastName']}, Designation: {emp['Designation']}\n")
                    if emp.get('KnownLanguages'):
                        self.result_text.insert(tk.END, "Languages: \n")
                        for lang in emp['KnownLanguages']:
                            self.result_text.insert(tk.END, f"  {lang['LanguageName']}: {lang['ScoreOutof100']}\n")
                    else:
                        self.result_text.insert(tk.END, "Languages: None\n")

                    self.result_text.insert(tk.END, "\n")  # Add a blank line between employees
            else:
                self.result_text.insert(tk.END, "No results found.\n")
        else:
            messagebox.showwarning("Input Error", "Please enter a search term.")

    def add_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        employee_id = self.employee_id_entry.get()
        designation = self.designation_entry.get()
        languages = self.language_entry.get().split(',')

        if first_name and last_name and employee_id and designation and languages:
            try:
                employee_id = int(employee_id)

                employees = EmployeeJSONHandler.read_employees()
                if any(emp['EmployeeID'] == employee_id for emp in employees):
                    messagebox.showwarning("Duplicate Employee ID", "An employee with this ID already exists.")
                    return

                language_objects = []
                for lang in languages:
                    lang_name, score = lang.split(':')
                    language_objects.append(Language(lang_name.strip(), int(score.strip())))

                new_employee = Employee(first_name, last_name, employee_id, designation, language_objects)
                EmployeeJSONHandler.add_employee(new_employee)
                messagebox.showinfo("Success", "New Employee Added")
            except ValueError:
                messagebox.showerror("Input Error", "Please ensure all fields are correct.")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields.")

    def delete_employee(self):
        employee_id = self.delete_entry.get()
        if employee_id:
            try:
                EmployeeJSONHandler.delete_employee(int(employee_id))
                messagebox.showinfo("Success", f"Employee with ID {employee_id} deleted.")
            except ValueError:
                messagebox.showerror("Input Error", "Invalid Employee ID")
        else:
            messagebox.showwarning("Input Error", "Please enter an Employee ID to delete.")

    def update_employee(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        employee_id = self.employee_id_entry.get()
        designation = self.designation_entry.get()
        languages = self.language_entry.get().split(',')

        if employee_id:
            try:
                employee_id = int(employee_id)
                language_objects = []
                for lang in languages:
                    if ':' in lang:
                        lang_name, score = lang.split(':')
                        language_objects.append(Language(lang_name.strip(), int(score.strip())))

                employees = EmployeeJSONHandler.read_employees()

                for emp in employees:
                    if emp['EmployeeID'] == employee_id:
                        if first_name:
                            emp['FirstName'] = first_name
                        if last_name:
                            emp['LastName'] = last_name
                        if designation:
                            emp['Designation'] = designation
                        if language_objects:
                            emp['KnownLanguages'] = [
                                {'LanguageName': lang.language_name, 'ScoreOutof100': lang.score_out_of_100} for lang in
                                language_objects]

                        EmployeeJSONHandler.save_employees(employees)
                        messagebox.showinfo("Success", "Employee Updated")
                        return

                messagebox.showwarning("Update Error", "Employee ID not found.")

            except ValueError:
                messagebox.showerror("Input Error", "Please ensure all fields are correct and in the correct format.")
        else:
            messagebox.showwarning("Input Error", "Please enter an Employee ID to update.")



app = EmployeeGUI()
app.mainloop()
