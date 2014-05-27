alter table mineturer.users add column bcrypt_pwd varchar(255) default null;
ALTER TABLE mineturer.users ALTER COLUMN password DROP NOT NULL;
