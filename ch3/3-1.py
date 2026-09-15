import cv2 as cv
from pathlib import Path

print("실행 중인 파일:", Path(__file__).resolve())

image_path = Path(__file__).resolve().parent / "soccer.jpg"

print("이미지 경로:", image_path)
print("파일 존재 여부:", image_path.is_file())

img = cv.imread(str(image_path))

if img is None:
    raise SystemExit("이미지 로딩 실패: 위에 출력된 경로를 확인하세요.")

cv.imshow("Title", img)

half_img = img[:img.shape[0] // 2, :img.shape[1] // 2]

cv.imshow("Red channel", half_img[:, :, 2])
cv.imshow("Green channel", half_img[:, :, 1])
cv.imshow("Blue channel", half_img[:, :, 0])

cv.waitKey(0)
cv.destroyAllWindows()