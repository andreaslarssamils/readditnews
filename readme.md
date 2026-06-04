# Readditnews

A news discussion platform where users can post, read, and comment on news stories.

## Overview

**External users' goal:** Post, read, delete, update and comment on news stories.
**Site owner's goal:** Build and nurture a discussion community around timely topics.

## Objectives

- Provide a platform for users to discover and discuss news content
- Allow users to create and engage with posts through comments and voting
- Enable content filtering, searching, and sorting for better usability
- Ensure secure authentication and user management
- Provide moderation tools for maintaining content quality

## Design

### Wireframes

    - Homepage (Feed)
![Homepage Wireframe](/media/homepage-feed-wireframe.png)
    - Post Detail
![Post Detail Wireframe](/media/post-detail-wireframe.png)
    - Login
![Login Wireframe](/media/login-wireframe.png)
    - Registration
![Registration Wireframe](/media/registration-wireframe.png)

### Colour Scheme

The colour palette uses cool blue-greys as the foundation,
with a purple-blue accent for interactive elements. The
combination gives the platform a calm, professional feel
while maintaining clear visual hierarchy.

| Role                  | Variable / Class      | Hex       |
|-----------------------|-----------------------|-----------|
| Page background       | `body`                | `#f7fafc` |
| Primary text          | `--text-color`        | `#1a202C` |
| Headings              | `--secondary-color`   | `#2d3748` |
| Primary UI elements   | `--primary-color`     | `#4a5568` |
| Accent / interactive  | `--accent-color`      | `#667eea` |
| Card border / divider | `footer border`       | `#e2e8f0` |

CSS custom properties (variables) are used throughout
for consistency and maintainability. The accent colour
(`#667EEA`) is applied to primary buttons, links, and
active states, with a subtle lift animation on hover
(`translateY(-2px)`) to reinforce interactivity.

Cards use `box-shadow` instead of borders for a softer,
more modern look, with an elevated shadow on hover to
indicate clickability.

---

### Typography

| Role | Font | Weight | Size |
|------|------|--------|------|
| Headings | Google Sans | 600 | 1.5rem |
| Body text | Source Serif 4 / Serif | 400 | 1rem |

Google Sans is used for all headings to give the platform
a clean, modern feel — its geometric clarity suits a
fast-paced news environment. Source Serif 4 is used for
body text and UI elements, providing a journalistic warmth
that complements the sans-serif headings and improves
readability for longer content.

Both fonts are loaded via Google Fonts.

---

### Imagery

- Post images are optional and uploaded by users via Cloudinary.
- Images are displayed as thumbnails in the feed and as a full-width header on the post detail page.
- No images are required — the layout adapts gracefully to text-only posts.
- A placeholder is shown when no image has been uploaded.
- Favicons and logo follow the same red-accent colour as the rest of the UI.

## User Stories

### Guest (Not Logged In)

#### US1 - Read Posts
**User Story:**
As a guest, I want to read posts so that I can stay informed about news.

**Acceptance Criteria:**
- Posts are displayed on the homepage in a list view (Feed).
- Each post displays key information such as title, category, author, publication date, excerpt, and optional image.
- The guest can open a post to view its full content.

**Tasks:**
- Create Post model with title, slug, author, category, content, image, excerpt, created_on, updated_on, status
- Create ListView to display all posts
- Create DetailView for individual post
- Create templates for list and detail views
- Add URL routes

---

#### US2 - Filter by Category
**User Story:**
As a guest, I want to filter posts by category so that I can find topics that interest me.

**Acceptance Criteria:**
- Categories are displayed as clickable buttons or tags.
- An "All" option is available to show all posts.
- Selecting a category filters the post list.
- The active category is visually highlighted.

**Tasks:**
- Create Category model with name and slug
- Add category buttons to the list template
- Filter queryset based on selected category
- Highlight the active category in the UI

---

#### US3 - Search Posts
**User Story:**
As a guest, I want to search for posts so that I can quickly find specific content.

**Acceptance Criteria:**
- A search bar is visible at the top of the page.
- The guest can enter keywords to search.
- Results match against post title and content.
- A message is displayed if no results are found.

**Tasks:**
- Add search input field to the template
- Create search view filtering title and content
- Display results or "no results" message
- Add URL route for search

US3 was not implemented within the current project scope and remains as a future feature.

---

#### US4 - Sort Posts
**User Story:**
As a guest, I want to sort posts so that I can prioritise the most relevant or recent content.

**Acceptance Criteria:**
- A sort dropdown is available.
- Options include "Newest", "Oldest", "Most Voted", "Least Voted".
- The post list updates based on selection.
- Default sorting is "Newest".

**Tasks:**
- Add sort dropdown to template
- Handle sorting logic in the view
- Set default sorting

---

#### US5 - Register Account
**User Story:**
As a guest, I want to register an account so that I can participate in the community.

**Acceptance Criteria:**
- Registration link is available in the header.
- User can sign up with username, email, and password.
- Validation provides clear error messages.
- User is logged in and redirected after successful registration.

**Tasks:**
- Create CustomUser model (AbstractUser)
- Configure allauth
- Create registration template
- Add registration link in header

---

### Logged-in User

#### US6 - Create Post
**User Story:**
As a logged-in user, I want to create a post so that I can share news with the community.

**Acceptance Criteria:**
- A "Create Post" button is visible to logged-in users.
- The form includes title, category, content (rich text), and optional image.
- The post is saved with the logged-in user as author and current timestamp.
- After submission, the user is redirected to the newly created post.

**Tasks:**
- Create CreateView with form fields (title, category, content, image)
- Configure Summernote for rich text editing
- Configure Cloudinary for image uploads
- Automatically assign logged-in user as author
- Redirect to post detail after creation
- Add URL route

---

#### US7 - Update Post
**User Story:**
As a logged-in user, I want to update my own posts so that I can correct mistakes or add information.

**Acceptance Criteria:**
- An edit button is visible only on posts authored by the user.
- The edit form is pre-filled with existing post data.
- Only the author can update their own posts.
- After saving, the user is redirected to the updated post.

**Tasks:**
- Create UpdateView with pre-filled form
- Restrict access to post author only
- Show edit button conditionally in template
- Redirect to updated post after saving

---
#### US8 - Delete Post
**User Story:**
As a logged-in user, I want to delete my own posts so that I can remove unwanted content.

**Acceptance Criteria:**
- A delete button is visible only for the post author.
- A confirmation step is required before deletion.
- Only the author can delete their posts.
- After deletion, the user is redirected to the homepage.

**Tasks:**
- Create DeleteView with confirmation template
- Restrict access to post author only
- Show delete button conditionally
- Redirect to homepage after deletion

---
#### US9 - Comment on Post
**User Story:**
As a logged-in user, I want to comment on posts so that I can participate in discussions.

**Acceptance Criteria:**
- A comment form is displayed on the post detail page for logged-in users.
- Comments are saved with author and timestamp.
- Comments appear under the correct post in chronological order.
- Comment count is displayed and updated.

**Tasks:**
- Create Comment model (post, author, body, created_on)
- Add comment form to detail template
- Handle submission in DetailView
- Display comments in chronological order
- Update comment count on post

---
#### US10 - Vote on Post
**User Story:**
As a logged-in user, I want to upvote or downvote posts so that I can express my opinion.

**Acceptance Criteria:**
- Upvote and downvote buttons are visible on each post.
- A user can only vote once per post.
- Clicking the same vote again removes it.
- Vote count updates immediately.

**Tasks:**
- Create Vote model (user, post, value)
- Enforce unique vote per user/post
- Create view to handle vote logic (add/update/remove)
- Display vote buttons in template
- Calculate and display total vote score

---
#### US11 - Log In and Log Out
**User Story:**
As a user, I want to log in and log out so that I can securely access my account.

**Acceptance Criteria:**
- A "Log in" button is visible for guests.
- Users can log in with valid credentials.
- Invalid credentials show an error message.
- After login, username and logout option are displayed.
- After logout, the user is redirected to the homepage.

**Tasks:**
- Configure allauth login/logout URLs
- Create login template
- Show conditional header (guest vs logged-in)
- Redirect after login/logout

---

### Admin / Site Owner

#### US12 - Manage Categories
**User Story:**
As an admin, I want to manage categories so that I can organise posts effectively.

**Acceptance Criteria:**
- Admin can create, edit, and delete categories via the admin panel.
- Each category includes a name and slug.
- Deleting a category does not break existing posts.

**Tasks:**
- Register Category model in admin
- Enable create/edit/delete functionality
- Handle relationships safely on delete

---

#### US13 - Moderate Content
**User Story:**
As an admin, I want to moderate posts and comments so that I can maintain a healthy community.

**Acceptance Criteria:**
- Admin can view all posts and comments.
- Admin can edit or delete inappropriate content.
- Changes are reflected immediately.

**Tasks:**
- Register Post and Comment models in admin
- Add filters and search functionality
- Enable delete/edit actions

---

#### US14 - Approve or Reject Posts
**User Story:**
As an admin, I want to approve or reject posts so that only appropriate content is published.

**Acceptance Criteria:**
- Posts can have statuses such as draft, pending, and published.
- Admin can update post status.
- Only published posts are visible to users.
- Unapproved posts remain hidden.

**Tasks:**
- Add status field to Post model
- Configure admin to update status
- Filter queryset to show only published posts publicly
- Add admin actions for approval/rejection

### Must Have
- US1 - Read Posts
- US5 - Register Account
- US6 - Create Post
- US7 - Update Post
- US8 - Delete Post
- US9 - Comment on Post
- US11 - Log In and Log Out
- US14 - Approve or Reject Posts

### Should Have
- US2 - Filter by Category
- US3 - Search Posts
- US12 - Manage Categories
- US13 - Moderate Content

### Could Have
- US4 - Sort Posts
- US10 - Vote on Post

### Won't Have for Now
- User profiles
- Saved posts
- Notifications
- Reporting system
- Bookmarking posts

## Features

### Input Validation

## Technologies Used
- dj-database-url-3.1.2
- Django-5.2.13
- gunicorn-25.3.0
- psycopg2-binary-2.9.11
- whitenoise-6.12.0
- python
- HTML
- CSS
- JavaScript
- Cloudinary (for media storage)
- PostgreSQL (database)
- django-allauth (authentication)
- django-summernote (rich text editor)
- Heroku (deployment)

## Testing

| Test | Action | Expected Result | Actual Result | Pass |
| ---- | ------ | --------------- | ------------- | ---- |
| test_create_user | Create a regular user with username, email, and password | User is created with correct attributes, is_active=True, is_staff=False, is_superuser=False | Works | ✅ |
| test_create_superuser | Create a superuser with username, email, and password | User is created with correct attributes, is_active=True, is_staff=True, is_superuser=True | Works | ✅ |
| test_signup_template | GET request to /accounts/signup/ | Status 200, correct template used, contains "Create an account" | Works | ✅ |
| test_signup_form | POST valid data to /accounts/signup/ | User is created in database, redirects with status 302 | Works | ✅ |
| test_signup_view | Resolve /accounts/signup/ URL | URL resolves to allauth SignupView | Works | ✅ |

# Manual Testing

The following manual tests were carried out on the deployed Heroku application
to verify that all features work correctly across the entire application.

## Test Results

| Feature | Test | Action | Expected Result | Actual Result | Pass |
|---------|------|--------|-----------------|---------------|------|
| **Navigation** | Logged-out header | Load any page without logging in | Header shows Register and Login links only — no Create Post button | As expected | ✅ |
| **Navigation** | Logged-in header | Log in and load any page | Header shows Create Post button, and Logout link | As expected | ✅ |
| **Navigation** | Footer | Load any page | Footer displays "© 2025 Readditnews" | As expected | ✅ |
| **Navigation** | Brand link | Click "Readditnews" in the header | Redirects to the post feed (homepage) | As expected | ✅ |
| **Authentication** | Register — valid data | Navigate to /accounts/signup/, fill in email, username, and matching passwords, click Register | Account is created, user is logged in and redirected to the feed | As expected | ✅ |
| **Authentication** | Register — duplicate username | Submit registration form with an already existing username | Form shows validation error, no account created | As expected | ✅ |
| **Authentication** | Register — mismatched passwords | Submit form with two different passwords | Form shows "The two password fields didn't match" error | As expected | ✅ |
| **Authentication** | Register — missing fields | Submit form with one or more required fields empty | Form shows field-level validation errors | As expected | ✅ |
| **Authentication** | Login — valid credentials | Enter correct username and password, click Log In | User is logged in and redirected to the feed | As expected | ✅ |
| **Authentication** | Login — invalid credentials | Enter incorrect password and click Log In | Error message shown, user remains on login page | As expected | ✅ |
| **Authentication** | Logout | Click Logout in the header | User is logged out, redirected to the feed, header shows Register/Login | As expected | ✅ |
| **Post Feed** | Feed loads | Navigate to the homepage | Post list is displayed with title, category badge, author, time ago, image, vote indicator, comment count, and excerpt for each post | As expected | ✅ |
| **Post Feed** | Empty feed | Visit feed when no posts exist | Page loads without errors | As expected | ✅ |
| **Post Feed** | Post link | Click a post title in the feed | Navigates to the correct post detail page | As expected | ✅ |
| **Category Filter** | Filter by category | Click a category button (e.g. Technology) | Only posts from that category are displayed | As expected | ✅ |
| **Category Filter** | Active state | Click a category button | Selected category button is visually highlighted/active | As expected | ✅ |
| **Category Filter** | Show all | Click the "All" button after filtering | All posts are displayed again | As expected | ✅ |
| **Sort** | Sort Newest (default) | Load the feed without changing sort | Posts are ordered with the most recent first | As expected | ✅ |
| **Sort** | Sort Oldest | Select "Oldest" from the sort dropdown | Posts are ordered with the oldest first | As expected | ✅ |
| **Sort** | Sort Most Voted | Select "Most Voted" from the sort dropdown | Posts are ordered by highest vote score first | As expected | ✅ |
| **Sort** | Sort Least Voted | Select "Least Voted" from the sort dropdown | Posts are ordered by lowest vote score first | As expected | ✅ |
| **Create Post** | Create Post button visibility | Log in and visit the feed | Create Post button is visible in the header | As expected | ✅ |
| **Create Post** | Create Post button — logged out | Visit the feed without logging in | Create Post button is not visible | As expected | ✅ |
| **Create Post** | Create post — valid data | Fill in title, select category, add content, click Post | Post is saved and user is redirected to the new post detail page | As expected | ✅ |
| **Create Post** | Create post — missing required fields | Submit the create form with title or content empty | Form shows validation errors, this field is required, and Please fill in this field. | As expected | ✅ |
| **Create Post** | Create post — success message | Successfully create a post | "Your post was created successfully." message is displayed | As expected | ✅ |
| **Create Post** | Direct URL access — logged out | Navigate to /posts/create/ without logging in | Redirected to the login page | As expected | ✅ |
| **Edit Post** | Edit button visibility | View a post you authored | Edit button is visible on the post detail page | As expected | ✅ |
| **Edit Post** | Edit button — other user's post | View a post authored by a different user | Edit button is not visible | As expected | ✅ |
| **Edit Post** | Edit post — valid data | Click Edit, change the content, save | Post is updated and user is redirected to the post detail page | As expected | ✅ |
| **Edit Post** | Edit post — success message | Successfully save an edit | "Your post was updated successfully." message is displayed | As expected | ✅ |
| **Edit Post** | Edit URL — wrong user | Log in as a different user and manually navigate to /posts/edit/<slug>/ | Access is denied (403 Forbidden) | As expected | ✅ |
| **Delete Post** | Delete button visibility | View a post you authored | Delete button is visible on the post detail page | As expected | ✅ |
| **Delete Post** | Delete button — other user's post | View a post authored by a different user | Delete button is not visible | As expected | ✅ |
| **Delete Post** | Delete confirmation | Click Delete on your own post | A confirmation page is shown before deletion | As expected | ✅ |
| **Delete Post** | Delete post | Confirm deletion on the confirmation page | Post is deleted, user is redirected to the feed | As expected | ✅ |
| **Delete Post** | Delete post — success message | Successfully delete a post | "Your post has been deleted." message is displayed | As expected | ✅ |
| **Delete Post** | Delete URL — wrong user | Log in as a different user and navigate to /posts/delete/<slug>/ | Access is denied (403 Forbidden) | As expected | ✅ |
| **Comments** | Comment form — logged in | Open a post detail page while logged in | Comment form is visible | As expected | ✅ |
| **Comments** | Comment form — logged out | Open a post detail page without logging in | Comment form is not shown; "Log in to leave a comment" prompt is displayed | As expected | ✅ |
| **Comments** | Submit valid comment | Type a comment and click Comment | Comment appears on the page with the correct author and timestamp | As expected | ✅ |
| **Comments** | Comment success message | Successfully submit a comment | "Your comment was added." message is displayed | As expected | ✅ |
| **Comments** | Submit empty comment | Browser shows "Please fill in this field." — comment is not submitted | Browser shows native validation message | As expected | ✅ |
| **Voting** | Upvote a post | Log in and click the upvote button on a post | Vote score increases by 1 immediately | As expected | ✅ |
| **Voting** | Remove vote (toggle) | Click the same vote button again | Vote is removed and score returns to previous value | As expected | ✅ |
| **Voting** | Change vote direction | Upvote a post, then click downvote | Vote changes direction and score updates accordingly | As expected | ✅ |
| **Voting** | Vote — logged out | Visit the feed without logging in | Vote buttons require login (redirect or prompt) | As expected | ✅ |
| **Admin** | Admin access | Log in to /admin/ as a superuser | Admin panel is accessible | As expected | ✅ |
| **Admin** | Manage posts | In admin, edit or delete any post | Changes are saved and reflected on the site | As expected | ✅ |
| **Admin** | Manage categories | In admin, create a new category | Category appears in the category filter on the feed | As expected | ✅ |


## Bugs and Fixes

| Bug | Cause | Fix |
|-----|-------|-----|
| Voting on a post with an invalid or deleted slug caused an unhandled server error (500) instead of a proper error page | `PostVoteView` used `Post.objects.get(slug=slug)` which raises an unhandled `Post.DoesNotExist` exception if the post no longer exists | Replaced with `get_object_or_404(Post, slug=slug)` so the server returns a standard 404 response |
| No visual feedback was shown to users after creating, editing, or deleting a post — the action completed silently | The CBVs (`PostCreateView`, `PostUpdateView`, `PostDeleteView`) did not implement Django's messages framework | Added `SuccessMessageMixin` to all three views and defined a `success_message` on each; also added `messages.success()` and `messages.error()` to the comment submission handler in `PostDetailView` |

## Validator Testing

PEP8 validation was run using pycodestyle in the terminal. Migration files were excluded from the validation process to focus on the main project codebase. The output identified remaining E501 line-length issues in "posts, accounts, and readditnews".

![PEP8 Validation Output](/media/pycodestyle.png)

HTML code has been validated using the W3C HTML Validator (https://validator.w3.org/nu/#textarea).
No Warnings or Errors were found in the HTML code, confirming that it adheres to web standards and is well-structured.

![HTML Validation Output](/media/validator-html.png)

CSS code has been validated using the W3C CSS Validator (https://jigsaw.w3.org/css-validator/).
During the validation of the website's CSS code, a warning appears stating: "Due to their dynamic nature, CSS variables are currently not statically checked".

This is not a code error, but rather a technical notice from the validator. The warning occurs because the project utilizes CSS variables (custom properties) to efficiently manage elements such as colors and themes. Because CSS variables are dynamic—meaning their values can change in real time via JavaScript or depending on their location within the HTML structure—the validator cannot verify them through a purely static analysis of the code.

The browser handles the code completely correctly, and the warning therefore has no negative impact on the website's design, functionality, or performance. Aside from this standard notice regarding dynamic variables, the rest of the CSS stylesheet passes the validation successfully with no errors.

![CSS Validation Output](/media/css-error-warnings.png)

![CSS Validation Output](/media/css-validation.png)


## Deployment

The live application is deployed on Heroku and can be accessed at:
**https://readditnews-8170329d1dfc.herokuapp.com**

---

### Deploying to Heroku

#### Prerequisites

- A [Heroku](https://heroku.com) account
- A [Cloudinary](https://cloudinary.com) account (for media file storage)
- A PostgreSQL database (e.g. [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql) or [Neon](https://neon.tech))

---

#### 1. Clone the repository

```bash
git clone https://github.com/andreaslarssamils/readditnews
cd readditnews
```

---

#### 2. Create a Heroku app

1. Log in to [dashboard.heroku.com](https://dashboard.heroku.com).
2. Click **New → Create new app**.
3. Give the app a name and select your region, then click **Create app**.

---

#### 3. Set up a PostgreSQL database

1. In the Heroku dashboard, go to the **Resources** tab.
2. Under **Add-ons**, search for **Heroku Postgres** and select it.
3. Choose a plan and click **Submit Order Form**.
4. Heroku will automatically add a `DATABASE_URL` Config Var under **Settings**.

---

#### 4. Set up Cloudinary

1. Log in to [Cloudinary](https://cloudinary.com) and go to your dashboard.
2. Copy your **Cloud Name**, **API Key**, **Cloudinary URL** and, **API Secret** — you will need these in the next step.

---

#### 5. Set Config Vars

1. In the Heroku dashboard, go to **Settings → Config Vars → Reveal Config Vars**.
2. Add the following key/value pairs:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Your Django secret key (a long random string) |
| `DATABASE_URL` | Your PostgreSQL connection URL |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | Your Heroku app hostname, e.g. `your-app-name.herokuapp.com` |
| `CLOUDINARY_URL` | Your full Cloudinary URL (`cloudinary://<key>:<secret>@<cloud_name>`) |
| `CLOUDINARY_API_KEY` | Your Cloudinary API key |
| `CLOUDINARY_API_SECRET` | Your Cloudinary API secret |
| `CLOUDINARY_CLOUD_NAME` | Your Cloudinary cloud name |

> ⚠️ Never commit these values to version control. They are stored as
> environment variables only.

---

#### 6. Ensure the following files are in place

**`Procfile`** (in the project root — tells Heroku how to run the app):

```
web: gunicorn readditnews.wsgi
```

**`requirements.txt`** (lists all dependencies — keep this up to date):

```bash
pip freeze > requirements.txt
```

---

#### 7. Connect GitHub and deploy

1. In the Heroku dashboard, go to **Deploy → Deployment method**.
2. Select **GitHub** and connect your repository.
3. Under **Manual deploy**, select the `main` branch and click **Deploy Branch**.
4. Once the build completes, click **Open app** to verify the deployment.

To enable automatic deploys on every push to `main`, click **Enable Automatic Deploys**.

---

#### 8. Run database migrations

1. In the Heroku dashboard, go to **More → Run console**.
2. Enter the following commands one at a time:

```
python manage.py migrate
```

```
python manage.py createsuperuser
```

---

### Running Locally

#### 1. Clone the repository and create a virtual environment

```bash
git clone https://github.com/<your-username>/readditnews.git
cd readditnews
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### 2. Create an `env.py` file in the project root

```python
import os

os.environ["SECRET_KEY"] = "your-local-secret-key"
os.environ["DATABASE_URL"] = "your-database-url"
os.environ["CLOUDINARY_URL"] = "your-cloudinary-url"
os.environ["CLOUDINARY_API_KEY"] = "your-api-key"
os.environ["CLOUDINARY_API_SECRET"] = "your-api-secret"
os.environ["CLOUDINARY_CLOUD_NAME"] = "your-cloud-name"
os.environ["DEBUG"] = "True"
```

> Ensure `env.py` is listed in `.gitignore` so it is never committed.

#### 3. Apply migrations and run the server

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

---

### Security Notes

- `DEBUG` is set to `False` in production via a Config Var.
- `SECRET_KEY` is never stored in the codebase — it is read from the environment.
- `DATABASE_URL` and Cloudinary credentials are stored as Heroku Config Vars only.
- `env.py` is included in `.gitignore` and has never been committed to the repository.



## Credits and Attributions

### Frameworks and Libraries
- [Django](https://www.djangoproject.com/) — web framework
- [django-allauth](https://django-allauth.readthedocs.io/) — authentication
- [django-summernote](https://github.com/summernote/django-summernote) — rich text editor
- [WhiteNoise](https://whitenoise.readthedocs.io/) — static file serving
- [dj-database-url](https://github.com/jazzband/dj-database-url) — database configuration
- [Gunicorn](https://gunicorn.org/) — WSGI server
- [psycopg2](https://www.psycopg.org/) — PostgreSQL adapter

### Services
- [Heroku](https://heroku.com) — cloud hosting platform
- [Cloudinary](https://cloudinary.com) — media file storage
- [PostgreSQL](https://www.postgresql.org/) — relational database

### Fonts
- [Google Sans](https://fonts.google.com/) — heading font, via Google Fonts
- [Source Serif 4](https://fonts.google.com/specimen/Source+Serif+4) — body font, via Google Fonts

### Tools
- [W3C HTML Validator](https://validator.w3.org/) — HTML validation
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) — CSS validation
- [pycodestyle](https://pycodestyle.pycqa.org/) — PEP8 validation

### Acknowledgements
- Code Institute — project brief and learning outcomes

### References
- [LearnDjango](https://learndjango.com/) — Django tutorials and best practices by Will Vincent

- [Google Gemini](https://gemini.google.com/) — AI tool used to generate
  post content and images for development and testing

- [Claude](https://claude.ai) by Anthropic — AI assistant used for
  code guidance, improvements, debugging, and documentation support

- [GitHub Copilot](https://copilot.github.com/) by GitHub — AI code completion
  tool used to assist with coding tasks and improve efficiency

