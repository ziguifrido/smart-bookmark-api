![GitHub](https://img.shields.io/github/license/ziguifrido/smart-bookmark-api)
![GitHub top language](https://img.shields.io/github/languages/top/ziguifrido/smart-bookmark-api)
![GitHub last commit](https://img.shields.io/github/last-commit/ziguifrido/smart-bookmark-api)

# Smart Bookmark API

The Smart Bookmark API is a Python-based RESTful API that allows users to manage, categorize, and recommend bookmarks intelligently based on various tags and metadata. This API is designed to help users store and organize their favorite links, with additional features like auto-suggestions, search, and personalized bookmark recommendations.

## Features
* **Bookmark Management**: Add, update, and delete bookmarks.
* **Categorization**: Organize bookmarks into categories for better management.
* **Search**: Search through bookmarks using titles, descriptions, or tags.
* **Recommendations**: Personalized bookmark recommendations based on user preferences and behaviors.
* **Tagging**: Add tags to bookmarks for easy filtering and organization.
* **RESTful API**: Easily integrate with any web or mobile application.

## Getting Started
To use the Smart Bookmark API, follow the steps below to set it up and start making requests.

### Prerequisites
* Python 3.7+
* pip (Python package manager)
* A virtual environment (venv)
* FastAPI (RESTful Python framework)

### Installation

1. Clone the repository:

```bash

  git clone https://github.com/ziguifrido/smart-bookmark-api.git
  cd smart-bookmark-api

```

2. Create a virtual environment

```bash

  python3 -m venv venv
  source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

```

3. Install the denpendencies

```bash

  pip install -r requirements.txt

```

4. Set up your environment variables

    4.1. Copy the `.env` file to a local one
    ```bash

      cp .env .env.local

    ```
    4.2. Fill the `.env.local` file with your own values

5. Set up your database

```bash

  python manage.py migrate # TODO

```

6. Start the API server

    6.1. Locally   

    ```bash

      fastapi dev main.py

    ```
    6.2. Docker
    ```bash

        docker-compose up -d
    
    ```

The API will now be running at `http://127.0.0.1:8000`.


## Technologies Used

* Python 3.7+
* FastAPI (RESTful Python framework)

## Author

Marcos Oliveira
