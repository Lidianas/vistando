"""empty message

Revision ID: b0beb42c2c0a
Revises: a326b23bde54
Create Date: 2018-10-24 01:50:13.436495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0beb42c2c0a'
down_revision = 'a326b23bde54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('salas', sa.Column('senha', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('salas', 'senha')
    # ### end Alembic commands ###
