# README: Feature Set 2

## Project Overview
Feature Set 2 introduces forms, validation, and multi-model design to enhance the blog functionality. This includes the ability to create and manage tags, as well as improved validation for blog post creation.

## Key Features
- **Custom Forms**: Added validation for blog post titles (minimum 5 characters).
- **Tags Management**: Introduced a many-to-many relationship between blog posts and tags.
- **Create Tags**: Added a form and view to allow users to create tags dynamically.

## Usage
### Create Tags
1. Navigate to `/tags/create/` to create new tags.
2. Enter a tag name and submit the form.

### Blog Post Management
- Tags can be added to blog posts during creation or editing.

## Testing
- All features have been tested, including form validation, tag creation, and integration with blog posts.

## Documentation
- Refer to `ADR-0003_blog_feature_set_2.md` for architectural decisions.
- Refer to `CP_BRIEF_blog_feature_set_2` for the scope and requirements.

## License
This project is licensed under the MIT License.