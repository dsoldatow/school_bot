CREATE TABLE tasks(
    task_id serial PRIMARY KEY,
    answer text,
    photo_url text,

)

CREATE TABLE users(

)

CREATE TABLE user_tasks(
    user_task_id integer,
    user_id serial PRIMARY KEY,
    task_id integer,


)
