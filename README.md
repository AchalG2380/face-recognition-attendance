# Face Recognition Attendance System

A real-time face recognition system for managing employee attendance using Python, Flask, and OpenCV.

## Features

- Real-time face detection and recognition
- Employee registration with face encoding
- Attendance tracking with timestamp
- Visitor entry management
- Admin authentication
- Real-time notifications using WebSocket
- MySQL database integration

## Prerequisites

- Python 3.8+
- MySQL Server
- Webcam
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up MySQL database:
- Create a database named `face_recognition`
- Update database credentials in `app.py` if needed

5. Create required tables:
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    face_vector LONGBLOB,
    image_url VARCHAR(255),
    emp_id VARCHAR(50) UNIQUE
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    name VARCHAR(255),
    entry_time DATETIME,
    FOREIGN KEY (emp_id) REFERENCES employees(id)
);
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Access the web interface at `http://localhost:5000`

3. Login credentials:
- Admin password: 123456

## Project Structure

- `/static` - Contains static files (CSS, JS, images)
- `/templates` - HTML templates
- `/static/employees` - Stored employee images
- `/static/visitors` - Stored visitor images
- `app.py` - Main application file

## Security Notes

- Change the default admin password in production
- Secure the MySQL connection
- Use environment variables for sensitive data
- Enable HTTPS in production

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
 
