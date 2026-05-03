import json

# Creating a class to store circuits as objects
class Circuit:
    def __init__(self, name, terminal_voltage, led_fwd_voltage, current, resistance, question, hint):
        self.name = name
        self.terminal_voltage = terminal_voltage
        self.led_fwd_voltage = led_fwd_voltage
        self.current = current
        self.resistance = resistance
        self.question = question
        self.hint = hint

    # Determining the voltage across the reisistor
    def voltage_resistor(self):
        return (self.terminal_voltage - self.led_fwd_voltage)

    # Calculating the circuit's forward current if resistance is given
    def calculate_current(self):
        return (self.voltage_resistor() / self.resistance)

    # Calculating the resistor's resistance if forward current is given
    def calculate_resistance(self):
        return (self.voltage_resistor() / self.current)

    # Determining the correct answer depending which value was unknown
    def answer(self):
        if self.current == "x":
            return self.calculate_current()
        else:
            return self.calculate_resistance()

    # Reading the question to the user
    def read_question(self):
            print(f"Terminal voltage: {self.terminal_voltage}")
            print(f"LED forward voltage: {self.led_fwd_voltage}")
            if self.current == "x":
                print(f"Resistance: {self.resistance}")
            else:
                print(f"Current: {self.current}")
            print(self.question)
            
    # Reading the hint if users request it
    def read_hint(self):
        print(self.hint)

# Unpacking data from the JSON file with circuit information
def load_circuits(file):
    with open(file, "r") as f:
        data = json.load(f)

    circuits = []
    for item in data:
        circuit = Circuit(
            item["name"],
            item["terminal_voltage"],
            item["led_fwd_voltage"],
            item["current"],
            item["resistance"],
            item["question"],
            item["hint"]
        )
        circuits.append(circuit)

    return circuits

# Running the main quiz, TESTING POINT: CHANGE ans FROM int TO float
def run_quiz(circuits):
    for circuit in circuits:
        print(circuit.name)
        circuit.read_question()
        while True:
            try:
                ans = float(input("Enter your answer (units not required)\n> "))
                if ans == circuit.answer():
                    print("Congratulations, your answer is correct!")
                    print("Press any key to continue, or 0 to exit the program.")
                    decision = input("> ")
                    break
                else:
                    print("Your answer is incorrect.")
                    print("press any key to coninue, h for a hint, or 0 to exit the program.")
                    decision = input("> ").lower()
                    if decision == "h":
                        circuit.read_hint()
                    else:
                        break
            except ValueError:
                print("You did not enter a number, please try again.")
        if decision == "0":
            break
        else:
            pass
        
if __name__ == "__main__":
    circuits = load_circuits("datavalues.json")
    run_quiz(circuits)
