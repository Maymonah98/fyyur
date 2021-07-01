"""empty message

Revision ID: 7ab21561716f
Revises: b62445bc4689
Create Date: 2021-06-21 15:44:13.923229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab21561716f'
down_revision = 'b62445bc4689'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    # ### end Alembic commands ###