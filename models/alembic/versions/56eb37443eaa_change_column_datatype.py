"""change_column_datatype

Revision ID: 56eb37443eaa
Revises: 
Create Date: 2023-07-09 08:00:56.668760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56eb37443eaa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('products', 'description', type_=sa.Text)


def downgrade() -> None:
    pass
