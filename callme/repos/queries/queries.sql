CREATE TABLE teams (
    team_id SERIAL PRIMARY KEY,
    name TEXT,
    scheduling_timezone TEXT,
    email TEXT,
    slack_channel TEXT
);

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    team_id INT REFERENCES teams(id),
    name TEXT,
    full_name TEXT,
    phone_number TEXT,
    email TEXT
);

CREATE TABLE duties (
    duty_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    date TEXT,
    role TEXT
);

-- 
INSERT INTO teams (name, scheduling_timezone, email, slack_channel)
VALUES ()
RETURNING team_id;

DELETE 