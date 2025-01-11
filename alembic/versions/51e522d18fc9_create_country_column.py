"""create country column

Revision ID: 51e522d18fc9
Revises: e4871ee96b04
Create Date: 2025-01-08 18:55:55.242385

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '51e522d18fc9'
down_revision: Union[str, None] = 'e4871ee96b04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("address", sa.Column("country", sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column("address", "country")
