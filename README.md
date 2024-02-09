# Electric Bill Calculator

A simple web application built with Flask that allows users to calculate the cost of electricity based on selected electrical equipment and the number of hours of usage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Author](#author)
- [Contact](#contact)

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Install Flask using the following command:

    ```bash
    pip install

2. Clone or download this repository.

3. Navigate to the project directory.

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. Select the electrical equipment from the dropdown menu.

2. Enter the number of hours of usage.

3. Click the "Calculate" button.

4. View the calculated total cost on the result page.

## Customization

- You can customize the rates for each electrical equipment by modifying the `equipment_rates` dictionary in the `app.py` file.

```python
equipment_rates = {
    'bulb': 0.05,   # Rate per hour for each equipment
    'fan': 0.10,
    # Add more equipment and rates as needed
}
