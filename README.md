# BMI Calculator

## Description
This is a simple BMI (Body Mass Index) Calculator built using PyQt. The application allows users to enter their weight and height, select metric or imperial units, and calculate their BMI. The result includes the BMI value and the corresponding health status based on guidelines from the Department of Health and Human Services/National Institutes of Health.

## Features
- User-friendly PyQt interface
- Accepts input in metric (kg, cm) or imperial (lbs, in) units
- Computes BMI using the formula:
  
  ```
  BMI = Weight(kg) / (Height(m))²
  ```
  or for imperial:
  ```
  BMI = (Weight(lbs) / (Height(in)²)) * 703
  ```
- Displays BMI result and status:
  - Underweight (< 18.5)
  - Normal weight (18.5 - 25)
  - Overweight (25 - 30)
  - Obese (> 30)
- Menu Bar:
  - **File**: Exit the application or clear input fields
  - **Help**: Displays usage instructions

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/bbzet/CalculatorBMI
   cd BMI-Calculator
   ```
2. Install dependencies:
   ```bash
   pip install pyqt6
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Enter your **weight** and **height**.
2. Click **Calculate BMI** to see your result.
3. View your BMI status.
4. Use **File > Clear** to reset inputs or **File > Exit** to close the application.

## Screenshots
![](https://raw.githubusercontent.com/bbzet/CalculatorBMI/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-03%20132536.png)
![](https://raw.githubusercontent.com/bbzet/CalculatorBMI/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-03%20132559.png)
![](https://raw.githubusercontent.com/bbzet/CalculatorBMI/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-03%20132611.png)
![](https://raw.githubusercontent.com/bbzet/CalculatorBMI/refs/heads/main/screenshots/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202025-03-03%20132623.png)

## Sample Input/Output
### Input:
- Weight: 80 kg
- Height: 190 cm

### Output:
- BMI: 22.2
- Status: Normal Weight (Green Background)

## Repository Structure
```
BMI-Calculator/
│── main.py  # Main application file
│── bmi_calculator.ui  # UI file created using PyQt Designer
│── ui_5.py  # Py file created taked from pyqt6-tools designer
│── README.md  # Project documentation
│── screenshots/  # Folder containing example screenshots
```


