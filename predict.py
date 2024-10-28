from ultralytics import YOLOv10
 
# Load a pretrained YOLOv10n model
model = YOLOv10(r"C:\Users\86152\yolov10\runs\detect\train4\weights\best.pt")
 
# Perform object detection on an image
# results = model("test1.jpg")#图片检测并保存。
results = model.predict(r"C:\Users\86152\Documents\WeChat Files\wxid_ytyrt7a58voa22\FileStorage\Video\2024-07\26cd8a10e865d905a05a994f6867fa5f.mp4", save=True)#视频的检测并保存
#results.show()#直接内存里展示并不会存在硬盘。
 
