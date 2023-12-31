class hcn:
    def __init__(self,dai,rong):
        self.dai = dai
        self.rong = rong

    def chuvi (self):
        return (self.dai + self.rong ) * 2
    
    def dientich (self):
        return (self.dai * self.rong ) 
    
    def thongtin (self):
        print("Độ dài hai cạnh của hình chữ nhật là: ",self.dai, self.rong)
        print("chu vi của hình chữ nhật là: ",self.chuvi())
        print("diện tích của hình chữ nhật là: ",self.dientich())

#chiều dài và chiều rộng của hình chữ nhật
dai = float(input("nhập chiều dài của hình chữ nhật: "))
rong = float(input("nhập chiều rộng của hình chữ nhật: "))

hcnn = hcn(dai,rong)
hcnn.thongtin()

