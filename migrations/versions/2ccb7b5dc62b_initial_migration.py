"""Initial Migration

Revision ID: 2ccb7b5dc62b
Revises: 
Create Date: 2022-01-09 21:53:22.208306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ccb7b5dc62b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('nilai', sa.String(length=200), nullable=True))
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'score')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('score', sa.FLOAT(), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.drop_column('users', 'nilai')
    # ### end Alembic commands ###
