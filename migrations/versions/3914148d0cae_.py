"""empty message

Revision ID: 3914148d0cae
Revises: 1e87e395a664
Create Date: 2015-02-26 19:40:13.363889

"""

# revision identifiers, used by Alembic.
revision = '3914148d0cae'
down_revision = '1e87e395a664'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('size', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'size')
    ### end Alembic commands ###
