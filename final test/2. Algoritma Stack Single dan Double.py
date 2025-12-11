# ======================================
# STACK SINGLE
# ======================================

class StackSingle:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.stack = [None] * kapasitas
        self.top = -1

    def push(self, data):
        if self.top >= self.kapasitas - 1:
            print("Stack penuh! Push dibatalkan.")
            return
        self.top += 1
        self.stack[self.top] = data
        print(f"Push: {data}")

    def pop(self):
        if self.top == -1:
            print("Stack kosong! Pop dibatalkan.")
            return None
        removed = self.stack[self.top]
        self.top -= 1
        print(f"Pop: {removed}")
        return removed

    def display(self):
        if self.top == -1:
            print("Stack kosong.")
        else:
            print("Isi Stack:", self.stack[:self.top + 1])


# ======================================
# DOUBLE STACK (Dua Stack dalam Satu Array)
# ======================================

class StackDouble:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.array = [None] * kapasitas
        self.top1 = -1                   # Stack 1 mulai dari kiri
        self.top2 = kapasitas            # Stack 2 mulai dari kanan

    def push1(self, data):
        if self.top1 + 1 == self.top2:   # bertabrakan
            print("Stack 1 penuh!")
            return
        self.top1 += 1
        self.array[self.top1] = data
        print(f"Push Stack 1: {data}")

    def push2(self, data):
        if self.top2 - 1 == self.top1:
            print("Stack 2 penuh!")
            return
        self.top2 -= 1
        self.array[self.top2] = data
        print(f"Push Stack 2: {data}")

    def pop1(self):
        if self.top1 == -1:
            print("Stack 1 kosong!")
            return None
        removed = self.array[self.top1]
        self.top1 -= 1
        print(f"Pop Stack 1: {removed}")
        return removed

    def pop2(self):
        if self.top2 == self.kapasitas:
            print("Stack 2 kosong!")
            return None
        removed = self.array[self.top2]
        self.top2 += 1
        print(f"Pop Stack 2: {removed}")
        return removed

    def display(self):
        print("\nIsi Array Gabungan:", self.array)
        print("Stack 1:", self.array[:self.top1 + 1])
        print("Stack 2:", self.array[self.top2:])
        print()


# ======================================
# DEMO PROGRAM
# ======================================

if __name__ == "__main__":
    print("=== STACK SINGLE ===")
    s1 = StackSingle(5)
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.display()
    s1.pop()
    s1.display()

    print("\n=== STACK DOUBLE ===")
    sd = StackDouble(10)
    sd.push1(1)
    sd.push1(2)
    sd.push2(100)
    sd.push2(200)
    sd.display()
    sd.pop1()
    sd.pop2()
    sd.display()
