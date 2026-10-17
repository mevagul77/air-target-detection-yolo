import cv2
import numpy as np

def simulate_air_detection():
    # Sentetik bir hava/gökyüzü sahnesi oluştur
    img = np.ones((600, 800, 3), dtype=np.uint8) * 210  # Açık mavi gökyüzü
    
    # Temsili bir hava hedefi çiz (silüet)
    pts = np.array([[380, 290], [420, 290], [400, 320]], np.int32)
    cv2.fillPoly(img, [pts], (60, 60, 60))
    cv2.line(img, (350, 305), (450, 305), (60, 60, 60), 4)
    
    # Bounding Box (Tespit Kutusu)
    cv2.rectangle(img, (340, 280), (460, 335), (0, 255, 0), 2)
    label = "Target: UAV (Conf: 0.94)"
    cv2.putText(img, label, (340, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)
    
    cv2.imwrite("detection_output.png", img)
    print("Görsel 'detection_output.png' olarak kaydedildi.")

if __name__ == "__main__":
    simulate_air_detection()
