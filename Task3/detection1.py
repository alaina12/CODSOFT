#Face detection 

#importing modules
import os 
import cv2

def detect(image_path, output_folder):
    #load the pre-trained Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    #Read the image
    image = cv2.imread(image_path)

    #convert the inage to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Perform face detection 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

     # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    # Draw rectangles around the detected faces
    for(x, y, w, h) in faces:
        aspect_ratio = w / h
        if 0.5 < aspect_ratio < 1.5:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

     # Save the result in the output folder
    result_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(result_path, image)


    #display the result you can also save the result
    cv2.imshow('detected Faces', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #parh to ypur testing images
    faces = r'C:\Users\ASUS\CODSoft\faces'
    #update this path

    # Output folder for saving the results
    output_folder = r'C:\Users\ASUS\CODSoft\output_faces'

    #iterate through images in the testing folder
    for image_file in os.listdir(faces):
        image_path = os.path.join(faces, image_file)

        # Perform face detection on each image and save the result
        detect(image_path, output_folder)

