import tkinter as tk

def hasil_prediksi():
    hasil.config(text="Hasil Prediksi: Teknologi Informasi", bg="pink")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.configure(bg="pink")
tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14, "bold")).pack(pady=15)

entries = []
for i in range(10):
    tk.Label(root, text=f"Nilai {i+1}:").pack()
    e = tk.Entry(root, width=10)
    e.pack()
    entries.append(e)

tk.Button(root, text="Hasil Prediksi", bg="purple", command=hasil_prediksi).pack(pady=15)
hasil = tk.Label(root, text="Hasil Prediksi: -", font=("Arial", 12, "bold"))
hasil.pack()

root.mainloop()