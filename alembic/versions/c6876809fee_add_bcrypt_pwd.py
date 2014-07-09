'''add bcrypt_pwd

Revision ID: c6876809fee
Revises: 3b9a3e20e9e9
Create Date: 2014-07-08 22:25:07.439006

'''

# revision identifiers, used by Alembic.
revision = 'c6876809fee'
down_revision = '3b9a3e20e9e9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('SET search_path TO mineturer')

    op.add_column(
        'users',
        sa.Column('bcrypt_pwd', sa.String(), nullable=True),
        schema='mineturer'
    )
    op.execute('SET search_path TO public')


def downgrade():
    pass
