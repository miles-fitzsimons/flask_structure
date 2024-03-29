"""empty message

Revision ID: 75f223db81eb
Revises: 98f731955ef3
Create Date: 2019-07-24 16:53:47.400821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75f223db81eb'
down_revision = '98f731955ef3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wine',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('added_on', sa.DateTime(), nullable=False),
    sa.Column('public_id', sa.String(length=100), nullable=True),
    sa.Column('brand', sa.String(length=100), nullable=True),
    sa.Column('variety', sa.String(length=100), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.public_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wine')
    # ### end Alembic commands ###
