from BE_account import user

class Withdraw_money(user):
    def Deduct_money(self): #ถอนเงิน
            Withdraw = int(input("จำนวนเงินที่ต้องการถอน: "))
            self.money = self.money - Withdraw
            if self.money >= 500:
                print("========================================")
                print(f"ยอดเงินคงเหลือ: {self.money} บาท")
                print("========================================")
            if self.money < 500:
                print("========================================")
                print("⚠️ไม่สามารถถอนเงินได้เนื่องจากบัญชีของคุณมีน้อยกว่า 0 บาท")
                print(f"ยอดเงินคงเหลือ: {self.money} บาท")
                print("========================================")

    def Deposit_Money(self): #ฝากเงิน
            Withdraw = int(input("จำนวนเงินที่ต้องการฝาก: "))
            self.money = self.money + Withdraw
            print("========================================")
            print(f"ยอดเงินคงเหลือ: {self.money} บาท")
            print("========================================")
           