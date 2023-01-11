class Container :
	def __init__(self , name :str , volume : int , current_volume : int , pour_out : int = 100 ) -> None:
		self.__name = name 
		self.__volume = volume
		self.current_volume = current_volume
		self.pour_out = pour_out
	
	def pour_out_liqud(self) -> int :
		if self.current_volume > 0 :
			self.current_volume -= self.pour_out
			return self.pour_out
		else:
			print(f'{self.__name} я пустой')
			return 0

	def pour_liqud(self , volume : int ) -> None :
		if self.current_volume + volume <= self.__volume :
			self.current_volume += volume
		elif self.current_volume >= self.__volume :
			print(f'{self.__name} я полный')
	
	def __str__(self) -> str:
		return f'{self.__name} = {self.current_volume}'

def main():
	chainik = Container(name = 'chainik', volume = 700 , current_volume = 700   )
	krychka = Container(name = 'Krychka', volume = 200, current_volume = 0 , pour_out = 50  )

	for _ in range(0, 10):
		print(chainik)
		print(krychka)
		krychka.pour_liqud(chainik.pour_out_liqud())


if __name__ == '__main__':
	main()
