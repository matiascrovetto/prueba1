"""empty message

Revision ID: d866cbdde01c
Revises: 6e0c025d7440
Create Date: 2023-05-20 02:03:47.079039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd866cbdde01c'
down_revision = '6e0c025d7440'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('github', sa.String(length=100), nullable=True),
    sa.Column('linkedin', sa.String(length=100), nullable=True),
    sa.Column('instagram', sa.String(length=100), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###
