'''cleanup user table

Revision ID: 8fc6c74565d
Revises: 4f7733ee071
Create Date: 2014-07-09 20:40:46.513424

'''

# revision identifiers, used by Alembic.
revision = '8fc6c74565d'
down_revision = '4f7733ee071'

from alembic import op


def upgrade():
    op.execute('SET search_path TO mineturer')
    op.drop_column('users', 'password')
    op.create_unique_constraint('unique_username', 'users', ['username'])
    op.execute('SET search_path TO public')


def downgrade():
    pass
