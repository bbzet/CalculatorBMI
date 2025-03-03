from ui_5 import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox

class BMIApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bmiButton.clicked.connect(self.calculate_bmi)
        self.statusframe = self.status_frame
        self.actionClear.triggered.connect(self.clear_fields)
        self.actionExti.triggered.connect(self.close)
        self.actionHow_to_Use.triggered.connect(self.how_to_use)

    def calculate_bmi(self):
        try:
            height = float(self.heightEdit.text())
            weight = float(self.weightEdit.text())
            height /= 100
            if height <= 0 or weight <= 0:
                self.result.setText("Invalid Input")
                self.update_status_frame("none")
                return

            bmi = round((weight / (height ** 2)), 1)
            status, color = self.get_bmi_status(bmi)

            self.result.setText(f'{bmi} - {status}')
            self.update_status_frame(color)

        except ValueError:
            self.result.setText("Invalid Input")
            self.update_status_frame("none")

    def get_bmi_status(self, bmi):
        if bmi < 18.5:
            return "Underweight", "yellow"
        elif 18.5 <= bmi < 25:
            return "Normal", "green"
        elif 25 <= bmi < 30:
            return "Overweight", "orange"
        else:
            return "Obese", "red"

    def update_status_frame(self, color):
        self.result.setStyleSheet(f"background-color: {color}; border-radius: 10px;")

    def clear_fields(self):
        self.heightEdit.clear()
        self.weightEdit.clear()
        self.result.clear()
        self.update_status_frame("none")

    def how_to_use(self):
        QMessageBox.information(self, "How to Use", "Enter your weight (kg) and height (m), then click 'Calculate BMI'.")
