"""Add content column

Revision ID: 467adebf1cd9
Revises: b9964e4cdf31
Create Date: 2022-12-15 12:01:15.573401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '467adebf1cd9'
down_revision = 'b9964e4cdf31'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('posts', 'content')
