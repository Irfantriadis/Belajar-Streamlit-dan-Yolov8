from ultralytics import YOLO
import csv

def save_to_csv(predictions, csv_file):
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if predictions.boxes is not None and len(predictions.boxes) > 0:
            for pred in predictions.boxes[0]:
                class_index = int(pred.cls[0])
                class_name = model.names[class_index]
                writer.writerow([class_name])

csv_file = 'detected_objects.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['label'])

model = YOLO('model/best.pt')

for frame in model.predict(source=0, show=True, conf=0.5, stream=True):
    save_to_csv(frame, csv_file)
