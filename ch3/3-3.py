import cv2 as cv
import sys
from pathlib import Path

image_path = Path(__file__).resolve().parent / "soccer.jpg"
img = cv.imread(str(image_path))

if img is None:
    sys.exit(f"이미지를 읽을 수 없습니다:\n{image_path}")

t, bin_img = cv.threshold(
    img[:, :, 2],
    0,
    255,
    cv.THRESH_BINARY + cv.THRESH_OTSU
)

print("오츠 알고리즘이 찾은 최적 임곗값:", t)

cv.imshow("R channel", img[:, :, 2])
cv.imshow("R channel binarization", bin_img)

cv.waitKey(0)
cv.destroyAllWindows()