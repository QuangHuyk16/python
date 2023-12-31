class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

# Nhập thông tin của một danh sách thí sinh
danh_sach_ts = []
while True:
    slts = int(input('Nhập số lượng thí sinh: '))
    if slts > 0:
        break
    else:
        print("Vui long nhap so tu nhien lon hon 0")

for i in range(slts):
    ho_ten = input('Nhập họ tên của thí sinh {}: '.format(i+1))
    while True:
        diem_toan = float(input('Nhập điểm Toán của thí sinh {}: '.format(i+1)))
        if diem_toan > 10:
            print("Vui long nhap so diem be hon hoac bang 10")
            continue
        break

    while True:
        diem_ly = float(input('Nhập điểm Lý của thí sinh {}: '.format(i+1)))
        if diem_ly > 10:
            print("Vui long nhap so diem be hon hoac bang 10")
            continue
        break

    while True:
        diem_hoa = float(input('Nhập điểm Hóa của thí sinh {}: '.format(i+1)))
        if diem_hoa > 10:
            print("Vui long nhap so diem be hon hoac bang 10")
            continue
        break

    ts = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
    danh_sach_ts.append(ts)

# Hiển thị danh sách thí sinh trúng tuyển theo thứ tự điểm từ cao xuống thấp
diem_chuan = 20
danh_sach_trung_tuyen = []
for ts in danh_sach_ts:
    if ts.tinh_tong_diem() >= diem_chuan:
        danh_sach_trung_tuyen.append(ts)

if len(danh_sach_trung_tuyen) == 0:
    print('Không có thí sinh nào trúng tuyển.')
else:
    print('Danh sách các thí sinh trúng tuyển:')
    for ts in sorted(danh_sach_trung_tuyen, reverse=True):
        print('-  (Tổng điểm: )',ts.ho_ten, ts.tinh_tong_diem())



