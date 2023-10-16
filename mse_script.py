import cv2
import numpy as np

# Imagens carregadas
mapa_estatico = cv2.imread("mapa_estatico.png")
mapa_dinamico = cv2.imread("mapa_dinamico2.png")

# Redimensionamento das imagens
mapa_dinamico = cv2.resize(mapa_dinamico, (mapa_estatico.shape[1], mapa_estatico.shape[0]))

# Verificação das dimensões das imagens
assert mapa_estatico.shape == mapa_dinamico.shape, "Os mapas têm tamanhos diferentes!"

# Calculo do Mean Squared Error (MSE)
mse = np.mean((mapa_estatico - mapa_dinamico) ** 2)

# Valor do MSE
print(f"Mean Squared Error (MSE): {mse}")
