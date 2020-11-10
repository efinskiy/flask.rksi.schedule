"""empty message

Revision ID: 9b9c41c874a0
Revises: 4f2d85b137db
Create Date: 2020-11-08 00:57:48.427002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b9c41c874a0'
down_revision = '4f2d85b137db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weekdays', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('weekdays', sa.Column('wdid', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weekdays', 'wdid')
    op.drop_column('weekdays', 'date')
    # ### end Alembic commands ###