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
- django-4.2
- gunicorn-25.3.0
- psycopg2-binary-2.9.11
- whitenoise-6.12.0


## Testing

| Test | Action                 | Expected Result            | Actual Result | Pass |
| ---- | ---------------------- | -------------------------- | ------------- | ---- |


## Bugs and Fixes

| Bug                                   | Cause                          | Fix                         |
| ------------------------------------- | ------------------------------ | --------------------------- |

## Validator Testing

## Deployment

## Credits and attributions

