import cv2 as cv
from pathlib import Path

image_path = Path(__file__).resolve().parent / "rose.png"
img = cv.imread(str(image_path))

if img is None:
    raise SystemExit(f"이미지 파일을 확인하세요:\n{image_path}")

drawing = False      
start_x, start_y = 0, 0


def mouse_event(event, x, y, flags, param):
    global drawing, start_x, start_y

    x = max(0, min(x, img.shape[1] - 1))
    y = max(0, min(y, img.shape[0] - 1))

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y

    elif event == cv.EVENT_MOUSEMOVE and drawing:
        preview = img.copy()

        cv.rectangle(
            preview,
            (start_x, start_y),
            (x, y),
            (255, 0, 0),
            2
        )

        cv.imshow("Original", preview)

    elif event == cv.EVENT_LBUTTONUP and drawing:
        drawing = False

        x1, x2 = sorted([start_x, x])
        y1, y2 = sorted([start_y, y])

  
        if x1 == x2 or y1 == y2:
            cv.imshow("Original", img)
            return

        patch = img[y1:y2 + 1, x1:x2 + 1].copy()

      
        preview = img.copy()
        cv.rectangle(
            preview, (x1, y1), (x2, y2), (255, 0, 0), 2
        )
        cv.imshow("Original", preview)

       
        patch1 = cv.resize(
            patch, None, fx=5, fy=5,
            interpolation=cv.INTER_NEAREST
        )
        patch2 = cv.resize(
            patch, None, fx=5, fy=5,
            interpolation=cv.INTER_LINEAR
        )
        patch3 = cv.resize(
            patch, None, fx=5, fy=5,
            interpolation=cv.INTER_CUBIC
        )

        cv.imshow("Resize nearest", patch1)
        cv.imshow("Resize bilinear", patch2)
        cv.imshow("Resize bicubic", patch3)


cv.namedWindow("Original")
cv.setMouseCallback("Original", mouse_event)
cv.imshow("Original", img)

while True:
    if cv.waitKey(20) & 0xFF == 27:
        break
    if cv.getWindowProperty("Original", cv.WND_PROP_VISIBLE) < 1:
        break

cv.destroyAllWindows()