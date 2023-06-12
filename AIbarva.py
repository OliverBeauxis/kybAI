import cv2
import numpy as np

# Seznam známých barev a jejich příslušné RGB hodnoty
colors = {
    'modrá': (255, 0, 0),
    'zelená': (0, 255, 0),
    'červená': (0, 0, 255),
    'žlutá': (255, 255, 0),
    'fialová': (255, 0, 255),
    'oranžová': (255, 165, 0),
}

def find_color(image_path):
    # Načtení obrázku
    image = cv2.imread(image_path)

    # Změna barevného prostoru z BGR na RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Příprava dat pro algoritmus K-means
    pixels = image_rgb.reshape(-1, 3).astype(np.float32)

    # Určení počtu shluků (barev) pro K-means
    num_colors = len(colors)

    # Použití algoritmu K-means pro rozdělení pixelů do shluků
    _, labels, centers = cv2.kmeans(pixels, num_colors, None, criteria=10, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

    # Výpočet histogramu shluků
    _, counts = np.unique(labels, return_counts=True)

    # Získání indexu shluku s největším počtem pixelů
    dominant_color_index = np.argmax(counts)

    # Získání příslušné barvy
    dominant_color = centers[dominant_color_index]

    # Hledání nejbližší známé barvy
    color_name = None
    min_distance = float('inf')
    for name, rgb in colors.items():
        distance = np.linalg.norm(dominant_color - rgb)
        if distance < min_distance:
            min_distance = distance
            color_name = name

    return color_name

# Testování programu
image_path = 'test.jpg'
result = find_color(image_path)
print('Rozpoznaná barva:', result)
