"""adds fields to Artist

Revision ID: ad210f366e77
Revises: 4f5c151c4325
Create Date: 2021-05-23 17:53:29.583926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad210f366e77'
down_revision = '4f5c151c4325'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
