"""create address table

Revision ID: b06044037be2
Revises: f7d4d368c50d
Create Date: 2025-01-08 00:25:39.019207

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b06044037be2'
down_revision: Union[str, None] = 'f7d4d368c50d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("address",
                    sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
                    sa.Column("address1", sa.String(), nullable=False),
                    sa.Column("address2", sa.String(), nullable=False),
                    sa.Column("city", sa.String(), nullable=False),
                    sa.Column("state", sa.String(), nullable=False),
                    sa.Column("zip", sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("address")
