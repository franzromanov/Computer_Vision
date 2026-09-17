import cv2

dir_=["./mov1.png","./mov2.png"]

class substract_constructor():
	img_obj=[]
	cam_obj=0
	bin_img=[]

	def __init__(self,dir_,img_format):
		self.dir_=dir_
		self.img_format=img_format
		
		for i in range(len(self.dir_)):
			self.img_obj.append(cv2.imread(self.dir_[i],self.img_format))


	def to_bin(self,constraint_l=[170,170],constraint_u=[255,255],enum_=[0,0]):
		

		for i in range(len(self.dir_)):
			
			ret,dump=cv2.threshold(self.img_obj[i],constraint_l[i],constraint_u[i],enum_[i])
			self.bin_img.append(dump)


	def subs_image(self):
		self.subs_img=cv2.absdiff(self.bin_img[0],self.bin_img[1])



img_=substract_constructor(dir_,cv2.IMREAD_GRAYSCALE)
img_.to_bin([50,50])
img_.subs_image()

for i in range(len(dir_)):
	cv2.imwrite(f"./testing.png[{i}]",img_.bin_img[i])

cv2.imwrite("substract.png",img_.subs_img)