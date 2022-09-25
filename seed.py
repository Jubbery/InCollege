import sqlite3
con = sqlite3.connect("incollege.db")
cur = con.cursor()
# Create `users` table
cur.execute("""
DROP TABLE IF EXISTS `users`;
""")
cur.execute("""
CREATE TABLE `users` (
  `user_id` INTEGER PRIMARY KEY NOT NULL,
  `user_username` varchar(32) NOT NULL,
  `user_password` varchar(12) NOT NULL,
  `user_firstname` varchar(32) NOT NULL,
  `user_lastname` varchar(32) NOT NULL
)
""")

cur.execute("""
DROP TABLE IF EXISTS `jobs`;
""")
cur.execute("""
CREATE TABLE `jobs` (
  `job_id` INTEGER PRIMARY KEY NOT NULL,
  `job_title` varchar(32) NOT NULL,
  `job_description` varchar(256) NOT NULL,
  `job_employer` varchar(32) NOT NULL,
  `job_location` varchar(64) NOT NULL,
  `job_salary` varchar(64) NOT NULL,
  `job_user_id` INTEGER NOT NULL,
  FOREIGN KEY(job_user_id) REFERENCES users(user_id)
)
""")