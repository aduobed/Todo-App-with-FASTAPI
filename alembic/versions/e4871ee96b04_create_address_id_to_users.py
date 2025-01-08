"""create address_id_to_users

Revision ID: e4871ee96b04
Revises: b06044037be2
Create Date: 2025-01-08 00:34:41.127629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4871ee96b04'
down_revision: Union[str, None] = 'b06044037be2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users',
    referent_table='address', local_cols=['address_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name='users', type_='foreignkey')
    op.drop_column('users', 'address_id')
