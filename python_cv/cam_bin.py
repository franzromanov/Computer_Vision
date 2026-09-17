import cv2 as lol

#dir_="/home/neocrackers/Downloads"
#img_=lol.imread(f"{dir_}/gue.png",lol.IMREAD_GRAYSCALE)

cam_me= lol.VideoCapture(0)

while 1:
	ret,frame=cam_me.read()

	if not ret:
		print("no camera yo!")
		break

	img_=lol.cvtColor(frame,lol.COLOR_BGR2GRAY)

	thres_=lol.adaptiveThreshold(img_,255,lol.ADAPTIVE_THRESH_MEAN_C,lol.THRESH_BINARY,11,2)

	lol.imshow(f"adalah_gue",thres_)


	if lol.waitKey(1) & 0xFF ==ord('q'):
		break


cam_me.release()

lol.destroyAllWindows()


cam_me = lol.VideoCapture(0)

while 1:
    ret, frame = cam_me.read()

    if not ret:
        print("no camera yo!")
        break

    img_ = lol.cvtColor(frame, lol.COLOR_BGR2GRAY)

    # Gaussian blur
    img_ = lol.GaussianBlur(img_, (11, 11), 0)

    # Adaptive threshold
    thres_ = lol.adaptiveThreshold(
        img_,
        255,
        lol.ADAPTIVE_THRESH_GAUSSIAN_C,
        lol.THRESH_BINARY,
        11,
        2
    )

    lol.imshow("adalah_gue", thres_)

    if lol.waitKey(1) & 0xFF == ord('q'):
        break

cam_me.release()
lol.destroyAllWindows()