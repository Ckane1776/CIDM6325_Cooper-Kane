# BRIEF: Build blog feature set 1 slice

## Goal

- Implement blog feature set 1 addressing PRD §blog-feature-set-1.

## Scope (single PR)

- **Files to touch:** 
  - `myblog/models.py`: Add `BlogPost` and `Category` models with relationships.
  - `myblog/views.py`: Implement class-based views for authentication and CRUD.
  - `myblog/forms.py`: Add forms for `BlogPost` and `Category`.
  - `myblog/urls.py`: Add routes for login/logout, blog post CRUD, and category CRUD.
  - `myblog/templates/myblog/*.html`: Create templates for blog and category CRUD, including `blog_form.html`, `blog_confirm_delete.html`, `category_list.html`, etc.
  - `myblog/static/`: Add Bootstrap and custom styles if needed.
  - `myblog/tests.py`: Add unit tests for authentication, CRUD, and permissions.
  - `settings.py`: Configure `LOGIN_URL` and `LOGIN_REDIRECT_URL`.
  - `.github/workflows/`: Add CI/CD pipeline for automated testing.

- **Non-goals:** 
  - Third-party blog packages.
  - Non-essential admin customizations.

## Standards

- **Commits:** Use conventional style (feat/fix/docs/refactor/chore).
- **Environment:** No secrets; use environment variables via `settings.py`.
- **Testing:** Use Django’s `unittest` framework (`TestCase`).
- **Accessibility:** Ensure templates and interactions comply with WCAG 2.2 guidelines.
- **Styling:** Use Bootstrap for responsive design.
- **HTMX:** Implement advanced features like inline edits and live search.
- **Permissions:** Enforce role-based permissions for CRUD operations.
- **CI/CD:** Set up GitHub Actions for automated testing.

## Acceptance

- **User flow:** 
  - Users can log in and out using Django’s built-in authentication.
  - Users can create, read, update, and delete blog posts and categories, with permissions enforced.
  - Inline edits and live search are implemented using HTMX.
  - The UI is accessible and styled with Bootstrap.
  - CI/CD pipeline passes all tests.

- **Include migration?** Yes (for new/updated models).
- **Documentation:** Update documentation and PR checklist to reflect changes.

## Prompts for Copilot

- "Generate Django models for blog post and related entity with CRUD."
- "Implement login/logout using Django’s built-in authentication."
- "Add Bootstrap styling and HTMX interactions for forms and lists."
- "Document accessibility compliance (WCAG 2.2)."
- "Add role-based permissions for CRUD operations."
- "Implement advanced HTMX features (inline edit, live search)."
- "Set up CI/CD pipeline for Django tests."
- "Explain changes and propose commit messages."
- "Refactor into CBV while preserving behavior; show diff-ready patch."