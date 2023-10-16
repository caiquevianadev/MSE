import cv2
import numpy as np

# Carregue a imagem do mapa estático e do mapa dinâmico
mapa_estatico = cv2.imread("mapa_estatico.png")
mapa_dinamico = cv2.imread("mapa_dinamico2.png")

# Redimensione a imagem do mapa dinâmico para ter as mesmas dimensões do mapa estático
mapa_dinamico = cv2.resize(mapa_dinamico, (mapa_estatico.shape[1], mapa_estatico.shape[0]))

# Verifique se as imagens têm as mesmas dimensões
assert mapa_estatico.shape == mapa_dinamico.shape, "Os mapas têm tamanhos diferentes!"

# Calcule o Mean Squared Error (MSE)
mse = np.mean((mapa_estatico - mapa_dinamico) ** 2)

# Exiba o valor do MSE
print(f"Mean Squared Error (MSE): {mse}")
