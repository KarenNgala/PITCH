"""Change field name

Revision ID: 6f703eda3a49
Revises: 6e9f0b0e0a72
Create Date: 2020-07-14 17:07:03.560736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f703eda3a49'
down_revision = '6e9f0b0e0a72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_encrypt', sa.String(length=128), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_encrypt')
    # ### end Alembic commands ###