alter table mineturer.users add column bcrypt_pwd varchar(255) default null;
--run fix_pw.py
ALTER TABLE mineturer.users ALTER COLUMN password DROP NOT NULL;
ALTER TABLE mineturer.users ADD CONSTRAINT unique_username UNIQUE (username);

CREATE INDEX trip_idx ON mineturer.points(tripid);
CREATE INDEX time_idx ON mineturer.points(time);
CREATE INDEX start_time_idx ON mineturer.trips(start); 