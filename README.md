<a name="readme-top"></a>

<h1 align="center">Final task of selenium course on stepik.org</h1>

<!-- ABOUT THE PROJECT -->
## About The Project

Project structure:

- base_page.py - here we store methods that are applied throughout the project.
- locators.py - store locators as constants. The locators of each individual page are wrapped in a different class.
- main_page.py - store methods for a specific page(main_page). MainPage inherited from the BasePage class so that we can use the methods described in base_page.py
- test_main_page - store the test cases themselves, which we will run using pytest.

To run tests you can use command
   ```sh
   pytest -v --tb=line --language=en test_main_page.py
   ```

### Built With

* [![python-shield]][python-url]
* [![selenium-shield]][selenium-url]

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/GoodGuyNoone/final_task_selenium_stepik.git
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Run tests
    ```sh
    pytest -v --tb=line --language=en test_main_page.py
    ```

<!-- CONTACT -->
## Contact

Aleksandr Churakov [![telegram][telegram-shield]][telegram-url] [![gmail][gmail-shield]][gmail-url] [![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/GoodGuyNoone/final_task_selenium_stepik](https://github.com/GoodGuyNoone/final_task_selenium_stepik)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/aleksandr-churakov/
[python-shield]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[python-url]: https://www.python.org/
[selenium-shield]: https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white
[selenium-url]: https://www.selenium.dev/
[telegram-shield]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://t.me/NOOOON3
[gmail-shield]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:churakovaleksandrqa@gmail.com
[pytest-shield]:
[pytest-url]:
