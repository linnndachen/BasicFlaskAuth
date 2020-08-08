# Basic Flask Auth - Follow Along

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within this directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API

#### Token information
Here is the link to generate the token

https://classdemo.us.auth0.com/authorize?
  audience=image&
  scope=SCOPE&
  response_type=token&
  client_id=LcBYLFzZ7oDmZ2crKrTI77Szy9esK45l&
  redirect_uri=http://localhost:5000/login-results&
  state=STATE

Here is the current token: 

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxDX21saU9pYVgxZXRiYkxKbDdmciJ9.eyJpc3MiOiJodHRwczovL2NsYXNzZGVtby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxZjBmZDdkOTNjMTAwMDNkY2IwN2U1IiwiYXVkIjoiaW1hZ2UiLCJpYXQiOjE1OTY5MTQwMDEsImV4cCI6MTU5NjkyMTIwMSwiYXpwIjoiTGNCWUxGelo3b0RtWjJjcktyVEk3N1N6eTllc0s0NWwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDppbWFnZXMiLCJwb3N0OmltYWdlcyJdfQ.kROMXfaLufyxHehwmyyeQDNlQcQ4yUYG5UNnK04j5d7EI38kfqcXqLdyHyVj_jZXeStzgG8KSIPySfO1AYaGs6PXtUzR1z9vGpQwyFpI4L1mYT00eJH2OzgSqdNzADsdEScFeTmdPE8qSKdirOCmWy7wHLNWIgIvHNp566f3FWVv9ZdF3mrhL55Nh7oKVIj5-HK7XvXnusDghBm8Sky1aqeoq4UUH-oZ4IlG5vE_WniR5nNtwQ7rjHzW_Bo0bRpjlPEU8fnozJJacu8o48F1wpeYi5Pv8KfJn82PEayrKtpqyywFB29Ggo6r3O_PWKOKSrhCJ8IVE944lM07FnA2ag`