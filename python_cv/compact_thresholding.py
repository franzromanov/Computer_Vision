import cv2
dir_= "./inisih_gue.png"



########################################################



class cv_class():

	img_obj=tuple()
	img_trans=tuple()

	def __init__(self,dir_,read_format_):

		self.dir_=dir_
		self.read_format_=read_format_

	def __read(self):
		self.img_obj=cv2.imread(self.dir_,self.read_format_)

		return self.img_obj

	def img_mat(self):
		print(self.__read())

	def to_binary(self,constraint_l,constraint_u=[255,255,255,255,255]):
		
		"""

		--opencv_thresholding_enum--

		cv2.THRESH_BINARY=0
		cv2.THRESH_BINARY_INV=1
		cv2.THRESH_TRUNC=2
		cv2.THRESH_TOZERO=3
		cv2.THRESH_TOZERO_INV=4

		"""


		threshold_enum=[]
		thresh_name=["binary","binary_inv","trunc","tozero","tozero_inv"]

		for i in range(5):
			ret,self.img_trans=cv2.threshold(self.__read(),constraint_l[i],constraint_u[i],i)
			threshold_enum.append(self.img_trans)

			cv2.imwrite(f"./gueh_banget_{thresh_name[i]}.png",self.img_trans)

		return threshold_enum

		
		def live_thresh(self):
			self.cam_capture=cv2.VideoCapture(0)

			#streaming_in_loop_cuh

			while 1:

				ret,self.frame=self.cam_capture.read() #get_frame_from_cam_dawg

				self.img_from_stream=cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
				self.blurredWGauss=cv2.GaussianBlur(self.img_from_stream,(11,11),0)
				self.adp_thresholding=cv2.adaptiveThreshold(self.blurredWGauss,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
				cv2.imshow("stream_out",self.adp_thresholding)

				if cv2.waitKey(1) & 0xFF == ord('q'):
					break


			self.cam_capture.release()
			cv2.destroyAllWindows()



########################################################



literally_me=cv_class(dir_,cv2.IMREAD_GRAYSCALE)

img_mat=literally_me.to_binary([170,170,170,170,170])

cv2.imshow("inisih_gue",img_mat[1])

cv2.waitKey(0)
