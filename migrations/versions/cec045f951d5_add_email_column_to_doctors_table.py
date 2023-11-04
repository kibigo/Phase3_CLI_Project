"""Add email column to doctors table

Revision ID: cec045f951d5
Revises: 887524be99fc
Create Date: 2023-11-04 23:47:58.309436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cec045f951d5'
down_revision = '887524be99fc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('doctors', sa.Column('email', sa.String(), nullable=False))


def downgrade():
    op.drop_column('doctors', 'email')
