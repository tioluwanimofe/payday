import time
import tkinter as tk


def format_time(elapsed_time):
    # Convert elapsed time to hours, minutes, seconds, milliseconds
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)
    milliseconds = int((elapsed_time * 1000) % 1000)

    # Format time string with leading zeros
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"


class ElapsedTimeGUI:
    def __init__(self, master):
        self.money_earned_label = None
        self.master = master
        master.title("Elapsed Time Calculator")

        # Define variables to store start time
        self.start_time = None
        self.elapsed_hours = 0
        self.hourly_rate = 18  # Replace with your desired hourly rate

        # Create labels and buttons
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack(pady=10)

        self.elapsed_time_label = tk.Label(master, text="Elapsed Time: 00:00:00.000")
        self.elapsed_time_label.pack()

        self.money_made_label = tk.Label(master, text="Money Earned: $0.00")
        self.money_made_label.pack()

    def start_timer(self):
        # Get the current time as starting point
        self.start_time = time.time()

        # Enable stop button and disable start button
        self.stop_button.config(state="normal")
        self.start_button.config(state="disabled")

        # Update elapsed time every 100 milliseconds
        self.update_elapsed_time()

    def stop_timer(self):
        # Get the current time and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - self.start_time

        # Format elapsed time and update label
        self.elapsed_time_label.config(text=f"Elapsed Time: {format_time(elapsed_time)}")

        # Calculate total elapsed hours and money earned
        self.elapsed_hours = int(elapsed_time // 3600)
        money_earned = self.elapsed_hours * self.hourly_rate

        # Update money earned label
        self.money_earned_label.config(text=f"Money Earned: ${money_earned:.2f}")

        # Disable stop button and enable start button
        self.stop_button.config(state="disabled")
        self.start_button.config(state="normal")
        self.start_time = None  # Reset start time

    def update_elapsed_time(self):
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            self.elapsed_time_label.config(text=f"Elapsed Time: {format_time(elapsed_time)}")
            # Update elapsed hours and money earned every hour
            if int(elapsed_time // 3600) > self.elapsed_hours:
                self.elapsed_hours = int(elapsed_time // 3600)
                money_earned = self.elapsed_hours * self.hourly_rate
                self.money_earned_label.config(text=f"Money Earned: ${money_earned:.2f}")

            self.master.after(100, self.update_elapsed_time)  # Update every 100 milliseconds


if __name__ == "__main__":
    root = tk.Tk()
    gui = ElapsedTimeGUI(root)
    root.mainloop()
