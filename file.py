class File:
    def __init__(self):
        self.values = []
    
    def stack(self, value):
        self.values.insert(0, value)
    
    def remove(self):
        if (self.values):
            return self.values.pop()

    def get_size(self):
        return len(self.values)
    
    def get_all_values(self):
        return self.values

f = File()
f.stack(9)
f.stack(5)
f.stack(2)

f.remove()
f.stack(7)

print(f.get_size())

print(f.get_all_values())