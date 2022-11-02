"""create customers

Revision ID: a83256da4228
Revises: 
Create Date: 2022-11-01 14:54:49.602158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83256da4228'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )

def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
