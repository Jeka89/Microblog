"""followers

Revision ID: 6528aa588d67
Revises: e025b62de824
Create Date: 2019-01-23 12:32:35.769065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6528aa588d67'
down_revision = 'e025b62de824'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
