
class Car:
    """自動車を表すシンプルな実装例"""

    def __init__(self, make, model, year):
        """自動車の特徴となる属性を初期化する"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """フォーマットされた名前を返す"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """自動車の走行距離を出力する"""
        print(f"走行距離は{self.odometer_reading}kmです。")

    def update_odometer(self, km):
        """
        指定された値に走行距離を更新します。
        走行距離を減らそうとする処理は拒否します。
        """
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("走行距離は減らせません！")

    def increment_odometer(self, km):
        """指定された距離を走行距離に追加する"""
        self.odometer_reading += km


class ElectricCar(Car):
    """電気自動車に特有の情報を表すクラス"""

    def __init__(self, make, model, year):
        """親クラスの属性を初期化する"""
        super().__init__(make, model, year)


if __name__ == '__main__':
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())



