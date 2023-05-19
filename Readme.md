## Flask IP Location Lookup

This is a Flask application that allows you to perform IP location lookups using the ipapi module. It provides a simple web interface where you can enter an IP address and retrieve its corresponding location information.

### Prerequisites

Make sure you have the following installed before running the application:

- Python 3.x
- Flask
- ipapi

### Installation

1. Clone this repository or download the source code.
2. Open a terminal and navigate to the project directory.
3. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Run the Flask application by executing the following command in the terminal:
   ```
   python app.py
   ```
   The application will start running locally at `http://127.0.0.1:5000`.

2. Open a web browser and navigate to `http://127.0.0.1:5000`.

3. Enter an IP address in the search field and click the "Search" button.

4. The application will retrieve the location information for the provided IP address and display it on the page.

### Project Structure

- `app.py`: This is the main Python script that contains the Flask application code.
- `templates/index.html`: This HTML template file defines the structure of the web interface.
- `requirements.txt`: This file lists the required Python dependencies.

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

### License

This project is licensed under the [MIT License](LICENSE).

### Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [ipapi](https://github.com/ipapi-co/ipapi-python)

### Disclaimer

This application relies on external services for IP location lookup. Please refer to the documentation and terms of use of the ipapi module for more information on their services and usage limits.

