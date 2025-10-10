# ADR-0001: Create a Simple Blog Page in Django (myblog app)

Date: 2025-10-05
Status: Accepted

Context

- PRD link: <myblog-blog-page>
- Problem/forces
  - The project needs a basic blog page to display posts for users.
  - No existing blog functionality in the myblog app.
  - Simplicity and maintainability are priorities for initial implementation.

Options

- A) Build a simple blog page using Django's generic views and templates in the myblog app.
- B) Use a third-party Django blog package for more features.

Decision

- We choose A because it allows for a lightweight, maintainable, and customizable solution tailored to our needs without unnecessary complexity.

Consequences

- Positive: Quick implementation, easy to maintain, full control over features and design.
- Negative/Risks: May require more development effort for advanced features in the future.

Validation

- Measure/rollback: Blog page is accessible, displays posts correctly, and meets initial requirements. Rollback by removing the new view/template if needed.
