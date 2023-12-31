class TamGiac:
    def __init__(self, canh_a, canh_b, canh_c):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c

class TamGiacVuong(TamGiac):
    def __init__(self, canh_a, canh_b, canh_c):
        super().__init__(canh_a, canh_b, canh_c)

class TamGiacCan(TamGiac):
    def __init__(self, canh_a, canh_b, canh_c):
        super().__init__(canh_a, canh_b, canh_c)

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh_a):
        super().__init__(canh_a, canh_a, canh_a)
