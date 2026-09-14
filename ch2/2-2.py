import cv2 as cv
import sys
from pathlib import Path

image_path = Path(__file__).resolve().parent / "girl_laughing.jpg"
img = cv.imread(str(image_path))

if img is None:
    sys.exit(f"이미지를 읽을 수 없습니다: {image_path}")


# 마우스 이벤트 처리 함수
def draw_shape(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # 왼쪽 클릭: 초록색 직사각형 (너비 100, 높이 60)
        cv.rectangle(
            img, (x - 50, y - 30), (x + 50, y + 30),
            (0, 255, 0), 2
        )

    elif event == cv.EVENT_RBUTTONDOWN:
        # 오른쪽 클릭: 빨간색 원 (반지름 30)
        cv.circle(img, (x, y), 30, (0, 0, 255), 2)

    cv.imshow("Display window", img)


cv.imshow("Display window", img)
cv.setMouseCallback("Display window", draw_shape)

cv.waitKey(0)  # 이미지 창에서 아무 키나 누르면 종료
cv.destroyAllWindows()