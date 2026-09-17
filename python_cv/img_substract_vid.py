import cv2 

class substract_vid():
	def __init__(self,source_,constraint_l=20,constraint_u=255):
		
		self.constraint_l=constraint_l
		self.constraint_u=constraint_u

		self.source_=cv2.VideoCapture(source_)
		ret,self.p_frame=self.source_.read()

		if (self.source_.isOpened())!=1:
			print("Bad Source, yo!")
			self.source_.release()
			exit()

		if ret!=1:
			print("failed to read source!")
			self.source_.release()
			exit()

		else:
			self.p_frame=cv2.cvtColor(self.p_frame,cv2.COLOR_BGR2GRAY)


	def __process_frame(self):

		self.c_frame=cv2.cvtColor(self.c_frame,cv2.COLOR_BGR2GRAY)#transform_to_grayscale

		self.end_product=cv2.absdiff(self.c_frame,self.p_frame)

		self.end_product=cv2.GaussianBlur(self.end_product,(11,11),0)

		self.end_product=cv2.adaptiveThreshold(self.end_product,self.constraint_u,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,101,-15)
		



		kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

		#self.end_product=cv2.dilate(self.end_product, kernel,iterations=1)

		#self.end_product=cv2.morphologyEx(self.end_product, cv2.MORPH_CLOSE, kernel)

	def stream_out(self):
		
		while self.source_.isOpened():
			
			ret,self.c_frame=self.source_.read()
			if ret!=1:
				print("EOF reached!")
				break

			self.__process_frame()
			print(self.end_product)
			cv2.imshow("--!nice!--",self.end_product)
			
			if cv2.waitKey(30) & 0xFF == ord('q'):
				break


			self.p_frame=self.c_frame.copy()

		self.source_.release()
		cv2.destroyAllWindows()


dir_="./highhoep.mp4" #fo_cam_use_0


stream_=substract_vid(dir_,60)

stream_.stream_out()

