"""empty message

Revision ID: 21457b202c31
Revises: b35ad503d19d
Create Date: 2021-01-12 11:08:55.015330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21457b202c31'
down_revision = 'b35ad503d19d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###