Setup Instructions

Setting up the frontend server:
enter the frontend directory
run command "node run dev"

Setting up the databse:
enter the backend directory
run command "go run main.go serve"
the database should be hosted at http://localhost:8090

Setting up the api:
set up the environment variables by cloning the provided env.example file
to a file named ".env"
Enter a client ID and a secret key provided by Plaid at https://dashboard.plaid.com/team/keys
run the command at /Api directory using the command "make up language=python"
if you need to check logs, run "make logs language=python"
if you need to close the container, run "make stop language=python"
The quickstart backend will be running on http://localhost:8000 and the frontend will be running on http://localhost:3000

Setting up the backend:
run tmp.pynb before running main.pynb
