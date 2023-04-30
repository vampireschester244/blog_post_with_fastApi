# Blog REST API
## Tech Stack
 - Fast API
 - Mongo DB
 - HTML/CSS
 # API Usage and Capabilities 
 ## Users
  - Ability to register and login users for performing actions on their blogs.
  - Triggering email notification to registered users.
  - Facilitate password reset functionality through email communication.
  - Providing security constraints like OAuth2 with Password (and hashing), Bearer with JWT tokens to the registered users in order to ensure secure blogging.
 ## Blog Posts
  - Ability for the users to create, read, update and delete their blogs.
  - To limit showing lists of blogs created in the page as per user convenience.
 ## CI/CD Pipelines
  - To create procfile, docker images and docker compose files in order to deploy the API to cloud platform for further usage
  - To buid git workflows using Github Actions for continuous integration and continuous delivery (CI/CD) of this Fast API Blog project
