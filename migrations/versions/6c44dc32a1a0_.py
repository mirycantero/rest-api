"""Create cereal table

Revision ID: 6c44dc32a1a0
Revises:
Create Date: 2019-11-29 10:07:50.969257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c44dc32a1a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cereal',
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('mfr', sa.String(length=10), nullable=True),
                    sa.Column('type', sa.String(length=10), nullable=True),
                    sa.Column('calories', sa.Float(), nullable=True),
                    sa.Column('protein', sa.Float(), nullable=True),
                    sa.Column('fat', sa.Float(), nullable=True),
                    sa.Column('sodium', sa.Float(), nullable=True),
                    sa.Column('fiber', sa.Float(), nullable=True),
                    sa.Column('carbo', sa.Float(), nullable=True),
                    sa.Column('sugars', sa.Float(), nullable=True),
                    sa.Column('potass', sa.Float(), nullable=True),
                    sa.Column('vitamins', sa.Float(), nullable=True),
                    sa.Column('shelf', sa.Float(), nullable=True),
                    sa.Column('weight', sa.Float(), nullable=True),
                    sa.Column('cups', sa.Float(), nullable=True),
                    sa.Column('rating', sa.Float(), nullable=True),
                    sa.PrimaryKeyConstraint('name', name=op.f('pk_cereal'))
                    )


def downgrade():
    op.drop_table('cereal')
