"""empty message

Revision ID: 1c62104cd9f7
Revises: 2cac40b5d61f
Create Date: 2019-10-14 21:28:00.764842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c62104cd9f7'
down_revision = '2cac40b5d61f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('df_goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('df_goods_type',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('logo', sa.String(length=20), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('df_goods_sku',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('goods', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.Column('price', sa.DECIMAL(), nullable=True),
    sa.Column('unite', sa.String(length=20), nullable=True),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.Column('sales', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['goods'], ['df_goods.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['type'], ['df_goods_type.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('df_goods_sku')
    op.drop_table('df_goods_type')
    op.drop_table('df_goods')
    # ### end Alembic commands ###