from tkinter import *


class SegundoGrau:

  def __init__(self, a, b, c):  #atributos
    self.a = a
    self.b = b
    self.c = c

  def main(self):

    def puxando_dados():
      
      self.a = int(entrada01.get())
      self.b = int(entrada02.get())
      self.c = int(entrada03.get())

      #delta
      delta = self.b**2 - 4 * self.a * self.c

      print(f'O valor para delta dos numeros informados é {delta}')
     
      #analise_delta
      if delta > 0:
        x1 = (-self.b - delta**0.5) / (2 * self.a)
        x2 = (-self.b + delta**0.5) / (2 * self.a)

        print(f'a função f(a) tem duas raizes reais:\nx1 = {x1}\nx2 = {x2}')
        envio = (f'a função f(a) tem duas raizes reais:\nx1 = {x1}\nx2 = {x2}')
        
      elif delta == 0:
        x = -self.c / self.b
        print(f'A função tem duas raizes reais e iguais, x1 e x2 = {x} \n')
        envio = print(
          f'A função tem duas raizes reais e iguais, x1 e x2 = {x} \n')

      else:
        z_re = self.b / (2 * self.a)
        z_im = ((-delta)**0.5) / (2 * self.a)
        print(
          f'A função f(a) tem duas raizes complexas, z1 = {z_re} + {z_im} *i e z2 = {z_re} - {z_im} *i \n'
        )
        envio = (
          f'A função f(a) tem duas raizes complexas, z1 = {z_re} + {z_im} *i e z2 = {z_re} - {z_im} *i \n'
        )

    tela = Tk()
    tela.geometry('600x600')
    tela.title('segundo grau')
    tela.config(bg='blue')

    texto01 = Label(tela, text='informe os valores', font='times 12', padx=60)
    texto01.grid(row=0, column=0)

    texto02 = Label(tela, text='digite o valor para A: ')
    texto02.grid(row=1, column=0)
    entrada01 = Entry(tela)
    entrada01.grid(row=1, column=1)

    texto03 = Label(tela, text='digite o valor para b: ')
    texto03.grid(row=2, column=0)
    entrada02 = Entry(tela)
    entrada02.grid(row=2, column=1)

    texto04 = Label(tela, text='digite o valor para c: ')
    texto04.grid(row=3, column=0)
    entrada03 = Entry(tela)
    entrada03.grid(row=3, column=1)

    b1 = Button(tela, text='envio', command=puxando_dados)
    b1.grid(row=4, column=0)

    #o erro está nessa linha onde o campo text do label não está reconhecendo a variavel envio dos if acima na def puxando_dados
    texto05 = Label(tela, text ='erro na linha 75')
    texto05.grid(row=5, column=0)

    tela.mainloop()


entrada = SegundoGrau('', '', '')
entrada.main()
