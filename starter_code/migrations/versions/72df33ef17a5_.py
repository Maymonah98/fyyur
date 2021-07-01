"""empty message

Revision ID: 72df33ef17a5
Revises: 0361384e5cff
Create Date: 2021-06-26 09:51:18.711479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72df33ef17a5'
down_revision = '0361384e5cff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('show',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'artist_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    # ### end Alembic commands ###