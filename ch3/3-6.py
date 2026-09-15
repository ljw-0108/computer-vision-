import sys
print("실행 중인 파이썬:", sys.executable)
import cv2 as cv
import matplotlib.pyplot as plt
from pathlib import Path

image_path = Path(__file__).resolve().parent / "mistyroad.jpg"
img = cv.imread(str(image_path))

# 이미지 로딩 확인
if img is None:
    raise SystemExit(f"이미지 파일을 확인하세요:\n{image_path}")

# 명암 영상으로 변환하고 출력
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.imshow(gray, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()

# 원본 명암 영상의 히스토그램
h = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.plot(h, color="r", linewidth=1)
plt.show()

# 히스토그램 평활화 후 출력
equal = cv.equalizeHist(gray)

plt.imshow(equal, cmap="gray")
plt.xticks([])
plt.yticks([])
plt.show()

# 평활화한 영상의 히스토그램
h = cv.calcHist([equal], [0], None, [256], [0, 256])

plt.plot(h, color="r", linewidth=1)
plt.show()