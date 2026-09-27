# 🔐 Python Login System with Tkinter

A simple and user-friendly **Login System** developed with **Python** and **Tkinter**.

This project provides a graphical login interface where users can enter their username and password. The application searches for the entered credentials in an **Excel file** and verifies the user's identity.

The system also includes a **CAPTCHA verification mechanism** to add an additional layer of protection to the login process.

---

## ✨ Features

* 🔑 Username and password authentication
* 📊 Search and verify user credentials from an Excel file
* 🛡️ CAPTCHA verification
* ❌ Error messages for invalid login information
* ✅ Successful login confirmation
* 🖥️ Graphical User Interface (GUI) using Tkinter
* 📁 Excel-based user data storage
* 🔍 User credential validation
* 🎨 Simple and user-friendly interface

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** – GUI development
* **OpenPyXL** – Reading and searching Excel files
* **Pandas** – Data processing (if used in the project)
* **Random** – CAPTCHA generation
* **Microsoft Excel** – User data storage

---

## 📂 Project Structure

```text
Login-System/
│
├── login.py
├── users.xlsx
├── README.md
└── images/
    └── login.png
```

> You can modify the file names according to your actual project structure.

---

## 🚀 How to Run

### 1. Install Python

Make sure that Python is installed on your computer.

You can check the installed version by running:

```bash
python --version
```

---

### 2. Install Required Libraries

If the project uses `OpenPyXL`, install it with:

```bash
pip install openpyxl
```

If `Pandas` is also used:

```bash
pip install pandas openpyxl
```

`Tkinter` is usually included with standard Python installations.

---

### 3. Run the Application

Navigate to the project directory and run:

```bash
python login.py
```

The Login System window should then open.

---

## 📊 Excel User Database

User credentials are stored in an Excel file.

For example:

| Username | Password |
| -------- | -------- |
| admin    | 1234     |
| user1    | 12345    |
| test     | abc123   |

When the user attempts to log in, the application searches the Excel file and compares the entered username and password with the stored credentials.

---

## 🛡️ CAPTCHA Verification

The application includes a CAPTCHA verification system.

A random CAPTCHA code is generated and displayed to the user. The user must enter the correct CAPTCHA code before the login process can continue.

This provides an additional verification step in the authentication process.

---

## 🖥️ User Interface

The graphical user interface is developed using **Tkinter**.

The main components include:

* Username input field
* Password input field
* CAPTCHA display
* CAPTCHA input field
* Login button
* Error and success messages

---

## 📸 Screenshot

Add a screenshot of the application to the `images` folder and display it here:

```markdown
![Python Login System](images/login.png)
```

---

## 🎯 Project Goals

This project was created to practice and demonstrate several Python programming concepts, including:

* GUI development with Tkinter
* Working with Excel files
* Reading and searching data
* User authentication
* Input validation
* Error handling
* CAPTCHA generation
* File-based data management

---

## 🔮 Future Improvements

The project can be extended with additional features such as:

* 👤 User registration
* 🔄 Password change functionality
* 🔐 Password hashing
* ⏳ Login attempt limitation
* 🗄️ SQLite, MySQL, or SQL Server database integration
* 📧 Password recovery
* 👥 Role-based access control
* 📝 Login history and activity logging
* 🎨 Improved and modern GUI design

---

## ⚠️ Security Note

This project is intended primarily for **educational and demonstration purposes**.

Storing passwords as plain text in an Excel file is **not recommended for real-world applications**.

For production systems, passwords should be securely hashed using appropriate password-hashing algorithms such as **bcrypt**, rather than being stored as plain text.

For larger applications, a proper database such as **SQLite, MySQL, or SQL Server** is also recommended instead of using Excel as the primary data store.

---

## 👩‍💻 Author

**Dr. Hadis Massoudi**

University Lecturer | Python Developer

---

## ⭐ Support

If you find this project useful, feel free to give it a ⭐ on GitHub.

You can also **Fork** the project and improve it by adding new features.

---

## 📄 License

This project was created for **educational and learning purposes**.
