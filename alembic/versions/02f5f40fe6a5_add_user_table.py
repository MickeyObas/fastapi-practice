"""Add user table

Revision ID: 02f5f40fe6a5
Revises: 467adebf1cd9
Create Date: 2022-12-15 12:05:29.120672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02f5f40fe6a5'
down_revision = '467adebf1cd9'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
     

def downgrade():
    op.drop_table('users')
