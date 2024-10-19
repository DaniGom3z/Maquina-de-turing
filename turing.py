import tkinter as tk
from tkinter import messagebox

class TuringMachine:
    def __init__(self, tape, blank_symbol='_'):
        self.tape = list(tape) + [blank_symbol]
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.state = 'q0'
        self.transitions = {
            ('q0', 'a'): ('q1', 'a', 'R'),
            ('q1', 'b'): ('q2', 'b', 'R'),
            ('q2', 'b'): ('q4', 'b', 'R'),
            ('q4', 'a'): ('q1', 'a', 'R'),
            ('q4', '_'): ('q_accept', '_', 'R'), 
        }


    def step(self):
        if self.head_position >= len(self.tape):
            self.tape.append(self.blank_symbol)

        current_symbol = self.tape[self.head_position]
        action = self.transitions.get((self.state, current_symbol))

        if action:
            new_state, write_symbol, direction = action
            self.tape[self.head_position] = write_symbol
            self.state = new_state
            if direction == 'R':
                self.head_position += 1
            elif direction == 'L' and self.head_position > 0:  
                self.head_position -= 1
        else:
            self.state = 'q_reject'

    def run(self):
        while self.state not in {'q_accept', 'q_reject'}:
            self.step()

        return self.state == 'q_accept'


class TuringMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Turing Machine Simulator")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="Ingrese la cadena a procesar (ej. abb):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.run_button = tk.Button(root, text="Ejecutar Máquina de Turing", command=self.run_turing_machine)
        self.run_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def run_turing_machine(self):
        tape = self.entry.get()

        if not tape:
            messagebox.showerror("Error", "Por favor, ingrese una cadena.")
            return

        tm = TuringMachine(tape)

        if tm.run():
            self.result_label.config(text="Cadena válida: Aceptada", fg="green")
        else:
            self.result_label.config(text="Cadena inválida: Rechazada", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = TuringMachineApp(root)
    root.mainloop()
