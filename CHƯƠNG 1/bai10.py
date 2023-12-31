class Diem:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, x, y, ban_truc_ngang, ban_truc_doc):
        super().__init__(x, y)
        self.ban_truc_ngang = ban_truc_ngang
        self.ban_truc_doc = ban_truc_doc

    def tinh_dien_tich(self):
        return 3.14 * self.ban_truc_ngang * self.ban_truc_doc

class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)
