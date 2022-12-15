"""Create posts table

Revision ID: b9964e4cdf31
Revises: 
Create Date: 2022-12-15 11:51:11.083305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9964e4cdf31'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
