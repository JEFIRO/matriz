import numpy as np

def get_reacao(Des):
  K_restrito = np.array([
    [0, 0],
    [0, -1],
    [-0.36, -0.48],
    [-0.48, -0.64]
  ])

  D = Des
  
  multiplicacao = np.dot(K_restrito,D)

  print("Resultado da multiplicação[K] * {D}:")
                         
  print(multiplicacao)
  return multiplicacao

def get_deslocamento():
  
  A = np.array([[0.36, 0.48], 
              [0.48, 1.64]])
  b = np.array([2, 0])

# Calcular a inversa de A
  A_inv = np.linalg.inv(A)

  result = np.dot(A_inv, b)
  
  print("\nVetor deslocamento (D):")
  print(result)
  return result
  
reasults = get_reacao(get_deslocamento())
