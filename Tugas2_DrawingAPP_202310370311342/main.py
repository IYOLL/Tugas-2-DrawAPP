import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 CanvasArt Python Edition")
        self.root.geometry("900x600")
        self.root.configure(bg="#f0f0f0")

        self.color = "#000000"
        self.tool = "dot"
        self.start_x = None
        self.start_y = None

        self.create_ui()
        self.bind_events()

    def create_ui(self):
        # Title Label
        title = tk.Label(self.root, text="🖌️ CanvasArt - Aplikasi Menggambar Python", font=("Poppins", 16, "bold"), bg="#f0f0f0", fg="#333")
        title.pack(pady=10)

        # Toolbar
        self.toolbar = tk.Frame(self.root, bg="#dddddd", height=50, padx=10, pady=5)
        self.toolbar.pack(fill="x", padx=10, pady=(0, 10))

        self.create_toolbar_buttons()

        # Canvas
        self.canvas = tk.Canvas(self.root, bg="white", width=880, height=480, highlightthickness=1, highlightbackground="#ccc")
        self.canvas.pack(padx=10, pady=10)

    def create_toolbar_buttons(self):
        self.add_button("Titik", "dot")
        self.add_button("Garis", "line")
        self.add_button("Persegi", "rect")
        self.add_button("Lingkaran", "circle")
        self.add_button("🎨 Warna", "color")
        self.add_button("🧽 Hapus", "erase")
        self.add_button("🔄 Reset", "clear")

    def add_button(self, text, action):
        btn = tk.Button(self.toolbar, text=text, font=("Poppins", 10), bg="#ffffff", fg="#000000",
                        activebackground="#cce5ff", activeforeground="#000",
                        relief="ridge", borderwidth=1, width=10,
                        command=lambda: self.handle_action(action))
        btn.pack(side="left", padx=5)

    def handle_action(self, action):
        if action == "color":
            picked = colorchooser.askcolor(title="Pilih Warna")
            if picked[1]:
                self.color = picked[1]
        elif action == "erase":
            self.color = "white"
        elif action == "clear":
            self.canvas.delete("all")
        else:
            self.tool = action

    def bind_events(self):
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def start_draw(self, event):
        self.start_x, self.start_y = event.x, event.y
        if self.tool == "dot":
            self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill=self.color, outline=self.color)

    def draw(self, event):
        if self.tool == "dot":
            self.canvas.create_oval(event.x-2, event.y-2, event.x+2, event.y+2, fill=self.color, outline=self.color)

    def end_draw(self, event):
        if self.tool == "line":
            self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill=self.color, width=2)
        elif self.tool == "rect":
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline=self.color, width=2)
        elif self.tool == "circle":
            radius = ((event.x - self.start_x)**2 + (event.y - self.start_y)**2) ** 0.5
            self.canvas.create_oval(self.start_x - radius, self.start_y - radius,
                                    self.start_x + radius, self.start_y + radius,
                                    outline=self.color, width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
