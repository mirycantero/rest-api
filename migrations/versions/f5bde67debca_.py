"""Add active column to cereal table

Revision ID: f5bde67debca
Revises: 6c44dc32a1a0
Create Date: 2019-11-29 11:26:15.651346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5bde67debca'
down_revision = '6c44dc32a1a0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('cereal',
                  sa.Column('active', sa.Boolean(),
                            server_default=sa.text('true'), nullable=True))


def downgrade():
    op.drop_column('cereal', 'active')
