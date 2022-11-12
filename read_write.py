import cv2

# 画像を取得
# print(cv2.__version__)
# カラーを白黒にする
# img = cv2.imread("image/cat.jpg", cv2.IMREAD_GRAYSCALE)
# img = cv2.imread("image/cat.jpg", )

# cv2.imshow("Image", img)

# cv2.waitKey(5000)
# 画像に文字を書き込む
# cv2.putText(
#     img,
#     text="cat.jpg",  # 表示したい文字(日本語は別途フォントの用意が必要)
#     org=(100, 250),  # テキストの左下の座標
#     fontFace=cv2.FONT_HERSHEY_SIMPLEX,  # フォント
#     fontScale=5,  # フォントサイズ
#     color=(255, 255, 0),  # 色のタプル(R, G, B)
#     thickness=3,
# )


img = cv2.imread(
    "image/cat.jpg",
)
print(img.shape)

resize_img = cv2.resize(img, dsize=(767 // 2, 432 // 2))
cv2.waitKey(5000)
cv2.imwrite("image/new_cat.jpg", resize_img)
