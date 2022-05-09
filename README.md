<div id="top"></div>

<br />
<div align="center">
  <a href="https://github.com/NYJustice/URL-Shortener-API">
  </a>

<h3 align="center">URL-Shortener-API</h3>

  <p align="center">
    Django REST API with two endpoints, one to decode a URL and another to decode short URL's generated by the API.
    <br />
    <a href="https://github.com/NYJustice/URL-Shortener-API"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NYJustice/URL-Shortener-API">View Demo</a>
    ·
    <a href="https://github.com/NYJustice/URL-Shortener-API/issues">Report Bug</a>
    ·
    <a href="https://github.com/NYJustice/URL-Shortener-API/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Simple URL sahortener API built with Django.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Django](https://www.djangoproject.com/)
* [Django_Rest_Framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This project requires PostgreSQL. To install follow these instructions.
* Ubuntu/Linux
  ```sh
  apt-get install postgresql-12
  ```
* Mac w/ Homebrew
  ```sh
  brew install postgresql
  ```
* Windows
  ```sh
  winget install -e --id PostgreSQL.PostgreSQL
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/NYJustice/URL-Shortener-API.git
   ```
2. Create virtual environment
   ```sh
   python3 -m venv .venv
   ```
3. Activate virtual environment 
   ```sh
   source .venv/bin/activate
   ```
4. Install python packages
   ```sh
   pip install -r requirements.txt
   ```
5. Create database with postgreSQL
   ```sh
   createdb urlShortener
   ```
6. Make migrations and then apply them
   ```sh
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
7. Start server
   ```sh
   python3 manage.py runserver
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

To use this API you can access the default django browsable API by navigating to <a href="https://localhost:8000/">this url</a> followed by "encode/" or "decode/" or by sending a request to the same URL's in your preferred client. Note that all CORS is set to allow all origins by default and the user will need to disable this manually.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Justice Caban - justice.a.caban@gmail.com

Project Link: [https://github.com/NYJustice/URL-Shortener-API/](https://github.com/NYJustice/URL-Shortener-API/)

<p align="right">(<a href="#top">back to top</a>)</p>
