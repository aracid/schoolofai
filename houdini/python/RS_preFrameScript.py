#PREPARE FILE WITH HEADER
import hou
f= open(hou.parm('labels_train_file').eval(),"w+")
f.write('frame,xmin,xmax,ymin,ymax,class_id\n')
f.close()
