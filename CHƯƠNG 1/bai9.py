class DaGiac:
    def __init__(self, so_canh):
        self.so_canh = so_canh

    def tinh_chu_vi(self):
        return 0

    def tinh_dien_tich(self):
        return 0

class HinhBinhHanh(DaGiac):
    def __init__(self, canh_a, canh_b):
        super().__init__(canh_a,canh_b)
        self.canh_a = canh_a
        self.canh_b = canh_b

    def tinh_chu_vi(self):
        return (self.canh_a + self.canh_b) * 2

    def tinh_dien_tich(self):
        return self.canh_a * self.canh_b

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(chieu_dai, chieu_rong)

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)



