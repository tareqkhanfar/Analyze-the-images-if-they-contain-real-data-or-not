from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox
from PyQt6.QtGui import QPixmap
import cv2
from main import *
class ImageChecker(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize variables
        self.image_path = None
        self.contains_data = None
        self.percentage = None

        # Set window properties
        self.setWindowTitle("Image Checker")
        self.setGeometry(100, 100, 800, 600)

        # Create UI elements
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.setGeometry(50, 50, 100, 30)
        self.upload_button.clicked.connect(self.upload_image)

        self.check_button = QPushButton("Check for data", self)
        self.check_button.setGeometry(170, 50, 150, 30)
        self.check_button.clicked.connect(self.check_for_data)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(50, 100, 700, 400)
        self.image_label.setStyleSheet("border: 2px solid black")

        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 520, 700, 30)
        self.result_label.setStyleSheet("font-weight: bold")

    def upload_image(self):
        # Open a file dialog to select an image
        file_path, _ = QFileDialog.getOpenFileName(self, "Open image", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image_path = file_path
            self.show_image()

    def show_image(self):
        # Load the image and display it in the interface
        pixmap = QPixmap(self.image_path)
        self.image_label.setPixmap(pixmap)
        self.result_label.setText("")

    def check_for_data(self):
        # Check if an image has been uploaded
        if self.image_path is None:
            QMessageBox.critical(self, "Error", "No image uploaded")
            return

        # Load the image
        img = cv2.imread(self.image_path)
        print ("TEST 0 ")
        DATA_FROM_DUMY=""
        DATA_FROM_IMAGE =""
        with open('DumyData.txt', 'r', encoding='utf-8') as file:
          utf8_string = file.read()
          DATA_FROM_DUMY = utf8_string.encode('ascii', 'ignore').decode('ascii')


        DataFromImage = self.getData(img)

        output = open("dataput.txt" , "w")
        DATA_TEMP = DataFromImage.encode('utf-8') # Encode the text using the utf-8 codec
        output.write(str(DATA_TEMP))
        output.close()


        with open('dataput.txt', 'r', encoding='utf-8') as file:
            utf8_string = file.read()
            DATA_FROM_IMAGE = utf8_string.encode('ascii', 'ignore').decode('ascii')



    # Read the file contents as a string


        # Check if the image contains data
        PERCENTAGE = Model.jaccardAlgorithm(DATA_FROM_IMAGE,DATA_FROM_DUMY )

        if (PERCENTAGE >=30):
            print(PERCENTAGE)
            print ("data is dumy ...")
            self.result_label.setStyleSheet("color: red; font-weight: bold")
            self.result_label.setText(f"Dummy data detected! Percentage: {PERCENTAGE}%")
        else :   
            word, percentage = Model.Data_IS_REAL(DataFromImage)
            print ("TEST 2 ")



            # Display a green alert and the percentage of data found if the image contains data
            if percentage > 50:
                print ("TEST 3 ")

                self.result_label.setStyleSheet("color: green; font-weight: bold")
                self.result_label.setText(f"Data found! the Data From Image is = {DATA_FROM_IMAGE} \n Percentage: {percentage}% with WORD = {word}")
            # Display a red alert if the image does not contain data
            else:
                self.result_label.setStyleSheet("color: red; font-weight: bold")
                self.result_label.setText(f"Dummy data detected! Percentage: {percentage}%")


    def getData(self, img):
        print ("TEST 1 ")
        return Model.showData(img)
         

app = QApplication([])
ex = ImageChecker()
ex.show()
app.exec()
