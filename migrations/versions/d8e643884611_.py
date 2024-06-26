"""empty message

Revision ID: d8e643884611
Revises: d897a22b69be
Create Date: 2024-04-19 10:22:34.135434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8e643884611'
down_revision = 'd897a22b69be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('tipo', sa.String(length=80), nullable=False),
    sa.Column('velocidad', sa.String(length=80), nullable=False),
    sa.Column('peso', sa.String(length=80), nullable=False),
    sa.Column('tripulacion', sa.String(length=250), nullable=True),
    sa.Column('armamento', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehiculos')
    # ### end Alembic commands ###
