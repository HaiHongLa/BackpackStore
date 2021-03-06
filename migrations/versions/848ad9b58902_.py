"""empty message

Revision ID: 848ad9b58902
Revises: e7f939b721f3
Create Date: 2021-11-02 17:30:17.361616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '848ad9b58902'
down_revision = 'e7f939b721f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('stock', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey'),
    sa.UniqueConstraint('name', name='product_name_key')
    )
    # ### end Alembic commands ###
