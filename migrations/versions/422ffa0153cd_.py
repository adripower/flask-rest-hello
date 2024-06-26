"""empty message

Revision ID: 422ffa0153cd
Revises: 55425377f174
Create Date: 2024-04-22 00:20:19.874967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '422ffa0153cd'
down_revision = '55425377f174'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favoritos_vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vehiculos_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehiculos_id'], ['vehiculos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos_vehiculos')
    # ### end Alembic commands ###
