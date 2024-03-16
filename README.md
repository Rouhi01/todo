# Django ToDo APP

<a href="https://ibb.co/MB4p9RP"><img src="https://i.ibb.co/GHLkFVC/Screenshot-from-2024-03-11-17-13-53.png" alt="Screenshot-from-2024-03-11-17-13-53" border="0"></a>

## Introduction

Welcome to ToDo App,This todo app was built by using the Django web framework, which has the ability to insert, update and delete the task.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rouhi01/todo.git
   cd todo
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to [http://localhost:8000](http://localhost:8000) to access the application.

## Configuration

- Customize the `settings.py` file to suit your project's specific needs, such as database configuration, static files, and more.

## Contributing

We welcome contributions! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
