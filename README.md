Task: Create a react app that will register users with fields: username, password, confirm password, email, and phone number. 
The username should be unique and have more than five characters.
The password must match the confirm password and have more than six characters.
Email and phone numbers should be unique.
The phone number should have exactly 11 digits.

Now, create a backend app using FastAPI. The frontend(React) app will send the registration form data to the backend. You may use the post method and fetch function in React. The backend will receive the data, perform necessary validations, and return appropriate messages to the frontend. In case of successful registration, the backend will save the user data into a MongoDB table through the Pymongo package. Initially, you can save the data in a text file if Mongodb installation takes time.

The minimum character constraints must be checked in the frontend(React) app without contacting the backend(FastAPI).
