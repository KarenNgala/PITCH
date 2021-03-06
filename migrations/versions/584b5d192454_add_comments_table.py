"""Add comments table

Revision ID: 584b5d192454
Revises: 37cb0589a40a
Create Date: 2020-07-17 02:51:38.155791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '584b5d192454'
down_revision = '37cb0589a40a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
