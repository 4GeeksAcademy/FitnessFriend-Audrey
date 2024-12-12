"""empty message

Revision ID: 3e042ffb527c
Revises: eaf0f70e838d
Create Date: 2024-12-10 23:43:35.292783

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3e042ffb527c'
down_revision = 'eaf0f70e838d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_metrics', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_metrics', schema=None) as batch_op:
        batch_op.alter_column('weight',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)

    # ### end Alembic commands ###
