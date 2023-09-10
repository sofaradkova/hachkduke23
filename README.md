# PennyPro

Are you a student looking to take control of your finances? Look no further. PennyPro is here to revolutionize the way you manage your money.

What will we do?

1. Ask what you want: PennyPro we'll help you pinpoit a specific achievable financial goal.

2. Analyze what you have: PennyPro lets you securily link your bank account, putting all your finances in one place. After linking your bank account, PennyPro provides an overview of your spending habits.

3. Suggest actions to bridge this gap: PennyPro offers budgeting limits you can set for the next month based on your goal and current financial situation.

4. Shame you into actually taking these actions: If your spending gets close to the budget limit or exceeds it, PennyPro will send you (threatening) reminders. If you maintain your budget limit streak, you'll receive achievements.

5. Support you along the way: PennyPro will answer any of your finance-related questions with the help of our trained AI chat assistant. 

# Setup

Setting up the frontend server: 

Enter the frontend directory and run

```bash
npm install
npm run dev
```

Setting up the database:

Enter the backend directory and run (the database should be hosted at http://localhost:8090)

```bash
go run main.go serve
```

Setting up the API: 

- Set up the environment variables by cloning the provided env.example file to a file named ".env"
- Enter a client ID and a secret key provided by Plaid at https://dashboard.plaid.com/team/keys
- At /Api directory run

```bash
make up language=python
```
- To check logs, run
```bash
make logs language=python
```
- To close the container, run
```bash
make stop language=python
```

The quickstart backend will be running on http://localhost:8000 and the frontend will be running on http://localhost:3000

Setting up the backend: run tmp.pynb before running main.pynb
