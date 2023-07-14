
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.webp" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">APIGNews</h3>

  <p align="center">
    <p align = "justify">
        In this project, we have created a news API using the Flask Python framework. The API allows us to access and manipulate news data through different endpoints.
    </p>
    <br />
    <a href="https://github.com/ThunderGer23/API-Gnews"><strong>Explore the docs ➡</strong></a>
    <br />
    <br /> 📂
    <a href="https://github.com/ThunderGer23/API-Gnews/activity">View Activity</a>
    ·
    <a href="https://github.com/ThunderGer23/API-Gnews/issues">Report Bug</a>
    💬
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#test">Test</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

##### **Used technology**
* Authentication and authorization: We implement a JWT token-based authentication and authorization system to protect News API endpoints.
* CRUD operations for news: We implement endpoints that allow us to create, read, update and delete news in the database.
* Data validation: We implement data validations to make sure that the data sent to the API is correct and consistent.
* Advanced queries: We implement endpoints that allow us to perform advanced queries, such as searching for news by category or filtering news by date.


<p align="right">(<a href="#about-the-project">back to top</a>)</p>



### Built With

* **_Python_**: We use Python as the primary programming language to develop our news API.
* **_Flask_**: We use the Flask framework to create our web application and define the API endpoints.
* **_JWT (JSON Web Tokens)_**: We use JWT to implement token-based authentication and authorization in our API.
* **_MySQL_**: We use MySQL as our database management system to store and retrieve news data.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Welcome to the News API! This guide will help you get started using and developing on top of the API quickly and easily.

### Prerequisites

Before you begin, make sure you have the following installed in your development environment:

* Python: Verify that you have Python installed on your system. You can download it from python.org.

* Docker: Verify that you have Docker installed on your system. You can download it from docker.com.

In case you have Linux you can use

* Your distro's package manager
  ```sh
  sudo apt-get install python3 docker
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [APIGNews](https://github.com/ThunderGer23/API-Gnews)
2. Clone the repository:

   ```shell
   git clone <repository_url>
3. Create a virtual environment and activate it:
   
   ```sh
    python3 -m venv venv
    source venv/bin/activate
4. Install the required packages:
   ```sh
    pip install -r requirements.txt

5. Set up the database:

* Execute the SQL script provided (database.sql) to create the necessary database tables and seed initial data.
6. Configure the environment variables:

* Modify the .env file and update the following variables according to your database setup:
   ```sh
    MYSQL_HOST=localhost
    MYSQL_USER=root
    MYSQL_PASSWORD=ThunderGer
    MYSQL_DB=apignews

7. Start the Flask server:
   ```sh
    python3 index.py
_This command will start the Flask development server, and the API will be accessible at http://localhost:5000._

<p align="right">(<a href="#about-the-project">back to top</a>)</p>

<!-- Test EXAMPLES -->
## Test

To run tests using pytest, follow these steps:

1. Open a terminal or command prompt and navigate to the root directory of your project where the tests are located.
2. Make sure you have `pytest` installed in your Python environment. If not, you can install it by running `pip install pytest`.
3. Run the following command to execute all the tests in the project:
   ```sh
    pytest
5. By default, `pytest` will automatically discover and run all the test files with names starting with `test_` or ending with `_test.py`.

By running `pytest`, you can easily execute your test suite and verify the functionality of your code. It helps in ensuring that your application behaves as expected and maintains its desired quality.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>
<!-- USAGE EXAMPLES -->
## Usage

Discover the various use cases and scenarios where you can leverage the News API to its fullest potential. From web and mobile applications to data analysis and automation, the API offers diverse possibilities for integrating news content into your projects. Explore the examples and find inspiration to incorporate the API into your next development.

![Image Description: Authenticated User with Token Return:](/images/CapturaAuth.PNG)

**Image Description: Authenticated User with Token Return:**

The image showcases the response from the API after successfully authenticating a user. The user submits a request with their login credentials and receives an access token in response. The token is an encrypted string that contains information about the user's identity and active session. By including the token with each subsequent request, the user can access protected resources and perform authorized actions within the application.

![Image Description: Articles Returned by the API:](/images/CapturaArticles.PNG)

**Image Description: Articles Returned by the API:**

The image displays a list of articles retrieved through a query to the News API. Each article is represented as an individual entry in the list and includes relevant information such as the title, description, and source. Articles can be filtered and sorted based on various criteria, allowing users to obtain specific and up-to-date information on topics of interest. This data can be utilized to display news in an application, perform analysis, or feed other automated processes.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#about-the-project">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#about-the-project">back to top</a>)</p>



<!-- CONTACT -->
## Contact

ThunderGer - [@ThunderGer](https://www.linkedin.com/in/thunderger/) - ThunderGer@outlook.com

<p align="right">(<a href="#about-the-project">back to top</a>)</p>
