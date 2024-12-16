"""empty message

Revision ID: 1921c9dc6f98
Revises: 163d4c3550b4
Create Date: 2024-12-16 20:41:50.242860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1921c9dc6f98'
down_revision = '163d4c3550b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('pic')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pic', sa.VARCHAR(length=750), autoincrement=False, nullable=True))

    op.drop_table('favorite')
    # ### end Alembic commands ###