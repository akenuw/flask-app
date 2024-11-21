import qrcode
import os

# Flask server base URL
base_url = "http://127.0.0.1:5000/scan"

# Directory to save QR codes
output_dir = "employee_qrcodes"
os.makedirs(output_dir, exist_ok=True)

# Employee list (ID and Name)
employees = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"},
    {"id": 3, "name": "Alice Johnson"},
    {"id": 4, "name": "Bob Brown"},
    {"id": 5, "name": "Charlie Davis"},
    {"id": 6, "name": "Dana White"},
    {"id": 7, "name": "Eva Green"},
    {"id": 8, "name": "Frank Black"},
    {"id": 9, "name": "Grace Blue"},
    {"id": 10, "name": "Henry Gold"},
    {"id": 11, "name": "Ivy Purple"},
    {"id": 12, "name": "Jack Silver"},
    {"id": 13, "name": "Karen Pink"},
    {"id": 14, "name": "Leo Orange"},
    {"id": 15, "name": "Mia Red"},
]

# Generate QR codes for each employee
for employee in employees:
    employee_url = f"{base_url}/{employee['id']}"  # Unique link for each employee
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(employee_url)
    qr.make(fit=True)

    # Save QR Code as image
    img = qr.make_image(fill='black', back_color='white')
    file_name = f"{employee['id']}_{employee['name'].replace(' ', '_')}.png"
    img.save(os.path.join(output_dir, file_name))

print(f"QR codes generated and saved in '{output_dir}' directory.")
