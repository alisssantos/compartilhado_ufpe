from tkinter import*
from tkinter import ttk

class SegundoGrau:

	def __init__(self,a,b,c ): #atributos
		self.a = a
		self.b = b
		self.c = c
		



	def delta(self,): #funcionalidades

		return self.b**2  - 4*self.a*self.c 

 
	def analise_delta(self):
		delta = self.delta()
		
		if delta > 0:

			x1 = (-self.b + delta**0.5)/(2*self.a)
			x2 = (-self.b - delta**0.5)/(2*self.a)
			print('a função f(a) = duas raizes, x1 = ', x1 , 'x2 = ' , x2)
		
		elif delta == 0:
		
			x = (-self.c / self.b)
			print('a função tem duas raizes, x1 = x2 = ', x)
			
		else:
			
			z_real = self.b/(2*self.a) 
			z_imag = ((-delta)**0.5)/(2*self.a)
			print(f'a função tem duas raizes complexas, x1 = {z_real:.2f} + {z_imag:.3f} *i e x2 = {z_real:.2f}-{z_imag:.3f} *i')
			
	def puxando_dados(self):
	#para a equação 1
		
		aa = b1.get()
		bb = b2.get()
		cc = b3.get()

		#para equação 2
		dd = b4.get()
		ee = b5.get()
		ff = b6.get()

		#para equação 3

		gg = b7.get()
		hh = b8.get()
		ii = b9.get()

		equacao1 = SegundoGrau(aa, bb, cc)
		equacao1.analise_delta()

		equacao2 = SegundoGrau(dd, ee, ff)
		equacao2.analise_delta()

		equacao3 = SegundoGrau(gg,hh,ii)
		equacao3.analise_delta()	



#para a equação 1
#aa = int(input('digite um valor para a: '))
#bb = int(input('digite um valor para b: '))
#cc = int(input('digite um valor para c: '))

#para equação 2
#dd = int(input('digite um valor para a: '))
#ee = int(input('digite um valor para b: '))
#ff = int(input('digite um valor para c: '))

#para equação 3

#gg = int(input('digite um valor para a: '))
#hh = int(input('digite um valor para b: '))
#ii = int(input('digite um valor para c: '))






tela = Tk()
tela.geometry('600x600')
#______________________________________________________________________________________
lab0 = Label(tela, text= 'EQUAÇÂO 2')
lab0.grid(row = 0, column = 0)
#______________________________________________________________________________________

texto_1 = Label(tela, text = 'EQUAÇÂO 1: digite um valor para a: ')
texto_1.grid(row = 1, column = 0)

texto_2 = Label(tela, text = 'EQUAÇÂO 1: digite um valor para b: ')
texto_2.grid(row = 2, column = 0)

texto_3 = Label(tela, text = 'EQUAÇÂO 1: digite um valor para c: ')

texto_3.grid(row = 3, column = 0)
#_____________________________________________________________________________________
b1 = Entry(tela, )
b1.grid(row = 1, column =1)

b2 = Entry(tela, )
b2.grid(row = 2, column =1)

b3 = Entry(tela,)
b3.grid(row = 3, column =1)

#_____________________________________________________________________________________
lab = Label(tela, text= 'EQUAÇÂO 2')
lab.grid(row = 4, column = 0)
#______________________________________________________________________________________

texto_1 = Label(tela, text = 'EQUAÇÂO 2: digite um valor para a: ')
texto_1.grid(row = 5, column = 0)

texto_2 = Label(tela, text = 'EQUAÇÂO 2: digite um valor para b: ')
texto_2.grid(row = 6, column = 0)

texto_3 = Label(tela, text = 'EQUAÇÂO 2: digite um valor para c: ')

texto_3.grid(row = 7, column = 0)
#______________________________________________________________________________________

b4 = Entry(tela,)
b4.grid(row = 5, column =1)

b5 = Entry(tela,)
b5.grid(row = 6, column =1)

b6= Entry(tela,)
b6.grid(row = 7, column =1)
#______________________________________________________________________________________
lab2 = Label(tela, text= 'EQUAÇÂO 3')
lab2.grid(row = 8, column = 0)
#_______________________________________________________________________________________

texto_1 = Label(tela, text = 'EQUAÇÂO 3: digite um valor para a: ')
texto_1.grid(row = 9, column = 0)

texto_2 = Label(tela, text = 'EQUAÇÂO 3: digite um valor para b: ')
texto_2.grid(row = 10, column = 0)

texto_3 = Label(tela, text = 'EQUAÇÂO 3: digite um valor para c: ')

texto_3.grid(row = 11, column = 0)

#________________________________________________________________________________________

b7 = Entry(tela,)
b7.grid(row = 9, column =1)

b8 = Entry(tela,)
b8.grid(row = 10, column =1)

b9= Entry(tela,)
b9.grid(row = 11, column =1)


b_puxar = Button(tela, text = 'ok', command = puxando_dados())
b_puxar.grid(row = 12, column = 1)



tela.mainloop()