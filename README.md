# Wiki Encyclopedia

This simple Django-based web application allows users to create, view, and search for entries in an encyclopedia-style platform. The application supports features like creating pages, searching entries, and displaying content in a user-friendly format. Markdown content is supported, and each entry page renders its Markdown content as HTML.

## Features

- **Home Page**: Displays a list of all available entries in the encyclopedia.
- **Create Page**: Allows users to create a new entry by providing a title and content in Markdown format.
- **Search**: Users can search for specific entries. Partial matches (case-insensitive) are supported.
- **Random Page**: Users can view a random entry from the encyclopedia.
- **Markdown to HTML**: Converts Markdown content into HTML for proper rendering.
  
## Technologies Used

- **Django**: Web framework for building the application.
- **Python**: Programming language used for backend development.
- **HTML/CSS**: For front-end design and structure.
- **JavaScript (optional)**: For potential interactive features.
- **Markdown**: Content format for entries.
- **markdown2**: (Optional) Used for Markdown to HTML conversion.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Python 3.x
- Django (Installation instructions below)
- `markdown2` library (Optional, for Markdown conversion)

## Installation

1. **Clone the repository** to your local machine:

   ```bash
   git clone https://github.com/your-username/wiki-encyclopedia.git
   cd wiki-encyclopedia
