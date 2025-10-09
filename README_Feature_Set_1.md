# README: Feature Set 1

## Project Overview
This feature set is part of a Django-based blog application that includes authentication, CRUD functionality, and advanced features like live search and inline edits.

## Features
- **Authentication:** Login/logout functionality using Django’s built-in views.
- **CRUD:** Full create, read, update, and delete operations for blog posts and categories.
- **HTMX Integration:** Inline edits and live search for dynamic interactions.
- **Accessibility:** WCAG 2.2 compliance for inclusivity.
- **CI/CD Pipeline:** Automated testing using GitHub Actions.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Ckane1776/CIDM6325_Cooper-Kane.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CIDM6325_Cooper-Kane
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage Guide
- **Blog Posts:**
  - Navigate to the blog view to see all posts.
  - Use the search bar for live search.
  - Edit or delete posts inline.
- **Categories:**
  - Navigate to the categories view to manage categories.
  - Create, edit, or delete categories.

## Accessibility Notes
- All templates are designed to meet WCAG 2.2 standards.
- ARIA roles and attributes are used for better screen reader support.
- Keyboard navigation is fully supported.

## CI/CD Pipeline
- The project includes a GitHub Actions workflow for automated testing.
- Tests are run on every push and pull request to the `main` branch.

## Contribution Guide
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "feat: Add new feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License.