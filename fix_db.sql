alter table mineturer.users add column bcrypt_pwd varchar(255) default null;
ALTER TABLE mineturer.users ALTER COLUMN password DROP NOT NULL;
ALTER TABLE mineturer.users ADD CONSTRAINT unique_username UNIQUE (username);