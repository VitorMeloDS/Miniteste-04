
class SenhaInvalida(Exception):
  pass

class PilhaArray:

  def __init__(self):
    self.senha = []
    self.maiusculo = []
    self.minusculo = []
      
  def __len__(self):
    return len(self.senha)

  def push(self, e):
    self.senha.append(e)

  def valida_senha(self, i = 0):
    if len(self.senha) == i:    
      if len(self.maiusculo) != len(self.minusculo) or len(self.senha) == 0:
        raise SenhaInvalida('senha inválida')
      else:
        self.count = 0
        for j,k in zip(self.maiusculo, self.minusculo):
          if j.lower() == k:
            self.count +=1  
        return 'Senha válida'
    elif self.senha[i] == self.senha[i].upper():
      self.maiusculo.append(self.senha[i])
      return self.valida_senha(i+1)
    elif self.senha[i] == self.senha[i].lower():
      self.minusculo.append(self.senha[i])
      return self.valida_senha(i+1)
        
              
if __name__ == '__main__':
  try:
    s = PilhaArray()
    s.push('A')
    s.push('B')
    s.push('C')
    s.push('c')
    s.push('D')
    s.push('E')
    s.push('e')
    s.push('d')
    s.push('b')
    s.push('a')
    print(s.valida_senha())
  except:
    print('Senha inválida')