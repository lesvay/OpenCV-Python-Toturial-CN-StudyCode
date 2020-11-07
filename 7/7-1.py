'''
查看鼠标被支持事件
'''
'''
import cv2
events=[i for i in dir(cv2) if 'EVENT'in i]
print(events)
'''
from cv2 import cv2
import numpy as np
#mouse callback function
#可以应用在物体跟踪、图像分割等领域
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    # 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    #27
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()


'''
字母和数字键的键码值(keyCode)
A	65	J	74	S	83	1	49
B	66	K	75	T	84	2	50
C	67	L	76	U	85	3	51
D	68	M	77	V	86	4	52
E	69	N	78	W	87	5	53
F	70	O	79	X	88	6	54
G	71	P	80	Y	89	7	55
H	72	Q	81	Z	90	8	56
I	73	R	82	0	48	9	57
数字键盘上的键的键码值(keyCode)	功能键键码值(keyCode)
0	96	8	104	F1	112	F7	118
1	97	9	105	F2	113	F8	119
2	98	*	106	F3	114	F9	120
3	99	+	107	F4	115	F10	121
4	100	Enter	108	F5	116	F11	122
5	101	–	109	F6	117	F12	123
6	102	.	110	 	 	 	 
7	103	/	111	 	 	 	 
控制键键码值(keyCode)
BackSpace	8	Esc	27	Right Arrow	39	-_	189
Tab	9	Spacebar	32	Dw Arrow	40	.>	190
Clear	12	Page Up	33	Insert	45	/?	191
Enter	13	Page Down	34	Delete	46	`~	192
Shift	16	End	35	Num Lock	144	[{	219
Control	17	Home	36	;:	186	/|	220
Alt	18	Left Arrow	37	=+	187	]}	221
Cape Lock	20	Up Arrow	38	,<	188	‘”	222
多媒体键码值(keyCode)
音量加	175	 	 	 	 	 	 
音量减	174	 	 	 	 	 	 
停止	179	 	 	 	 	 	 
静音	173	 	 	 	 	 	 
浏览器	172	 	 	 	 	 	 
邮件	180	 	 	 	 	 	 
搜索	170	 	 	 	 	 	 
收藏	171	 	 	 	 	 	 
'''