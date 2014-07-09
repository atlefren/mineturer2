Mineturer2
==========


Running
-------
1. Install Vagrant
2. Install Alembic
3. run 'vagrant up dev'
4. vagrant ssh dev
5. sudo su - postgres
5. cd /vagrant
6. psql -d mineturer2 -f mineturer_schema.sql (or path to a mineturer1 db dump)
7. exit
8. alembic upgrade head
9. to run the app: foreman start
10. the app is available at localhost:9080 (via nginx) and localhost:9081 (foreman directly)


Todo
----
1. make a prod playbook
2. cleanup playbook
3. make it fast
