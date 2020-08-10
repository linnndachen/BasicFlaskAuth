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

`eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImxDX21saU9pYVgxZXRiYkxKbDdmciJ9.eyJpc3MiOiJodHRwczovL2NsYXNzZGVtby51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYxZjBmZDdkOTNjMTAwMDNkY2IwN2U1IiwiYXVkIjoiaW1hZ2UiLCJpYXQiOjE1OTcxMDM0OTIsImV4cCI6MTU5NzExMDY5MiwiYXpwIjoiTGNCWUxGelo3b0RtWjJjcktyVEk3N1N6eTllc0s0NWwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDppbWFnZXMiLCJwb3N0OmltYWdlcyJdfQ.zZV0k7K4w6FqJhXdw-kLgIOR9RXyL9GgF6Eg2lIbozQg4ys02NhJHJEmWcce1kpBh8NbLH2cHtn8bSU8N_UP4uPIs2p8gR04OWRY1yt80NWXKN2zdj1AsbOqy8QvxuINMigEg53b0M81sdcF_2oq5VmDdW2oTNUJx4UDOiGXZKMQBggmG7DOxFQh8U6GbffZHNi7UuhsB9qzyoeF5kzQJApEWf8v9I6tG9UPFEzkBYP2E9OuhUX5LE3FC_0qwuJGAsjeKRCUbL6lwxgax4zzet3EtWPKjftaR51--dzuPl_n2ZHhifIRiObOeWXD4ZxERpddeGiUlXRaBl8WwSm0cA`