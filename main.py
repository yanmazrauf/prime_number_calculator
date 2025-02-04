import tkinter as tk

def primes_in_range(start, end):
    limit = end
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = []
    for num in range(start, limit + 1):
        if is_prime[num]:
            primes.append(num)
    return primes

def calculate_primes():
    start = int(start_entry.get())
    end = int(end_entry.get())
    primes = primes_in_range(start, end)
    result_label.config(text=f"Total prime numbers: {len(primes)}\nFirst 10 primes: {primes[:10]}")

root = tk.Tk()
root.title("Prime Number Calculator")

tk.Label(root, text="Lower Limit:").grid(row=0, column=0, padx=5, pady=5)
start_entry = tk.Entry(root)
start_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Upper Limit:").grid(row=1, column=0, padx=5, pady=5)
end_entry = tk.Entry(root)
end_entry.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_primes)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

result_label = tk.Label(root, text="Results will be displayed here", justify="left")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

