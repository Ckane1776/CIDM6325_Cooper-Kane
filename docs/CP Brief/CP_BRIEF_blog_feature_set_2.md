# BRIEF: Build Forms, Validation, and Multi-Model Design slice

## Goal

- Implement custom forms with validation and extend models with additional relationships addressing PRD §Part A and Part B Requirements.

## Scope (single PR)

- **Files to touch:**
  - `myblog/forms.py`: Add custom forms with validation and clean methods.
  - `myblog/models.py`: Extend models with additional relationships (One-to-Many or Many-to-Many).
  - `myblog/views.py`: Update views to handle new forms and relationships.
  - `myblog/templates/`: Update templates for new forms and relationships.
  - `docs/schema_diagram.png`: Provide schema diagram for updated models.
  - `docs/migration_notes.md`: Document migration notes.
- **Non-goals:**
  - Do not implement unrelated features outside the scope of forms and model relationships.

## Standards

- **Commits:** Use conventional style (feat/fix/docs/refactor/chore).
- **No secrets:** Use environment variables via settings.
- **Django tests:** Use `unittest`/`Django TestCase` (no pytest).

## Acceptance

- **User flow:** 
  - Users can interact with custom forms that validate input and handle errors gracefully.
  - Extended models support additional relationships and are functional in the application.
- **Include migration?** Yes.
- **Update docs & PR checklist:** 
  - Include schema diagram and migration notes.
  - Document WCAG 2.2 compliance for forms and templates.

## Prompts for Copilot

- "Generate a Django Form + view for custom validation with success redirect to the blog list."
- "Extend models with One-to-Many and Many-to-Many relationships; include migration scripts."
- "Explain changes and propose commit messages."
- "Refactor into CBV while preserving behavior; show diff-ready patch."

- **Additional Updates:**
  - Added a `tags` field to the `BlogPost` model to support many-to-many relationships.
  - Updated `BlogPostForm` to include validation logic for the `title` field, ensuring a minimum length of 5 characters.