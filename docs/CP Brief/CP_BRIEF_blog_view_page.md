# BRIEF: Build blog view page slice

Goal

- Implement blog view page addressing PRD §blog-view.

Scope (single PR)

- Files to touch: myblog/models.py, myblog/views.py, myblog/urls.py, myblog/templates/myblog/blog_view.html
- Non-goals: Advanced blog features (comments, tags, pagination), admin interface changes.

Standards

- Commits: conventional style (feat/fix/docs/refactor/chore).
- No secrets; env via settings.
- Django tests: use unittest/Django TestCase (no pytest).

Acceptance

- User flow: User visits blog page URL and sees a list of blog posts rendered from the database.
- Include migration? yes (for new model)
- Update docs & PR checklist.

Prompts for Copilot

- "Generate a Django model for a blog post with title, content, and published_date."
- "Generate a Django view and template to display all blog posts."
- "Add URL pattern for the blog view page."
- "Explain changes and propose commit messages."
- "Refactor into CBV while preserving behavior; show diff-ready patch."