"""add customers date_of_birth

Revision ID: 2cb96ed8e66e
Revises: a83256da4228
Create Date: 2022-11-01 14:59:14.344535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cb96ed8e66e'
down_revision = 'a83256da4228'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )


def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
