# Note App

This is a simple note-taking application built using FastAPI to provide a RESTful API interface and MongoDB for database storage.

## Features

- **RESTful API**: Utilizes FastAPI to create a web API for managing notes.
- **MongoDB Integration**: Stores notes in a MongoDB database.
- **Simple and Efficient**: Designed to be lightweight and easy to use.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sayan14banerjee/Note_App.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Note_App
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up MongoDB:
   - Ensure you have MongoDB installed and running locally or provide connection details in the configuration file.

5. Run the application:
   ```bash
   uvicorn index:app --reload
   ```

## Directory Structure

- **`__pycache__`**: Python bytecode cache directory.
- **`config`**: Configuration files.
- **`models`**: Data models for the application.
- **`routes`**: API route definitions.
- **`schemas`**: Pydantic models for request/response validation.
- **`static`**: Static files.
- **`templates`**: HTML templates.
- **`venv`**: Virtual environment directory.
- **`index.py`**: Entry point of the application.

## Usage

1. Once the application is running, you can interact with the API endpoints using tools like cURL, Postman, or through a web browser.
2. Use the provided endpoints to manage your notes, including creating, reading, updating, and deleting them.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
