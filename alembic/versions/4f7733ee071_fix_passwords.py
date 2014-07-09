'''fix passwords

Revision ID: 4f7733ee071
Revises: c6876809fee
Create Date: 2014-07-08 22:43:49.353256

'''

# revision identifiers, used by Alembic.
revision = '4f7733ee071'
down_revision = 'c6876809fee'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
import bcrypt


def upgrade():
    op.execute('SET search_path TO mineturer')
    conn = op.get_bind()
    res = conn.execute('select userid, password from users')
    results = res.fetchall()

    users = table(
        'users',
        column('bcrypt_pwd', sa.String),
        column('userid', sa.Integer)
    )

    for result in results:
        userid = result[0]
        pwd = result[1]
        bcrypt_pwd = bcrypt.hashpw(
            pwd.encode('utf-8'),
            bcrypt.gensalt()
        )
        op.execute(
            users.update().where(
                users.c.userid == op.inline_literal(userid)
            ).values({
                'bcrypt_pwd': op.inline_literal(bcrypt_pwd)}
            )
        )

    op.execute('SET search_path TO public')


def downgrade():
    pass
