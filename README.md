# Django Countries App

This Django app retrieves and displays information about countries using the [Restcountries API](https://restcountries.com/v3.1/all).

<img width="950" alt="image" src="https://github.com/iammromar/restcountries-django/assets/69416566/7b7fca32-62f7-492d-9702-f96744144f52">


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/iammromar/restcountries-django.git
    ```

2. Navigate to the project directory:

    ```bash
    cd restcountries-django
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    .\env\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source env/bin/activate
    ```

5. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to view the app.

## Usage

- Visit the homepage to see a list of countries with basic information.
- Click on a country to view more details.

## Contributing

If you'd like to contribute to this project, follow these steps:

1. Fork the repository on GitHub.
2. Clone your fork locally.
3. Create a new branch for your work.
4. Make changes and push to your fork.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
