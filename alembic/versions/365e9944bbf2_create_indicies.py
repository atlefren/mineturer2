"""create indicies

Revision ID: 365e9944bbf2
Revises: 8fc6c74565d
Create Date: 2014-07-09 20:45:55.675080

"""

# revision identifiers, used by Alembic.
revision = '365e9944bbf2'
down_revision = '8fc6c74565d'

from alembic import op


def upgrade():
    op.execute('SET search_path TO mineturer')
    op.create_index('trip_idx', 'points', ['tripid'])
    op.create_index('time_idx', 'points', ['time'])
    op.create_index('start_time_idx', 'trips', ['start'])
    op.execute('SET search_path TO public')


def downgrade():
    pass
