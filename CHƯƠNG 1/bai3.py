class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        self.tu_so = int(input('Nhập tử số: '))
        self.mau_so = int(input('Nhập mẫu số: '))

    def in_phan_so(self):
        print(f'{self.tu_so}/{self.mau_so}')

# Sử dụng lớp PhanSo
ps = PhanSo("self.tu_so","self.mau_so")
ps.nhap_phan_so()
ps.in_phan_so()
