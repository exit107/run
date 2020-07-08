"""Added connectivity between users and runs.

Revision ID: e9aecbd5b42a
Revises: 6f9d56f5168e
Create Date: 2020-07-07 21:05:16.146533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9aecbd5b42a'
down_revision = '6f9d56f5168e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('race')
    op.drop_table('day')
    op.drop_table('timezone')
    op.drop_table('lap')
    op.add_column('run', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'run', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'run', type_='foreignkey')
    op.drop_column('run', 'user_id')
    op.create_table('lap',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('avg_speed', sa.NUMERIC(), nullable=True),
    sa.Column('max_speed', sa.NUMERIC(), nullable=True),
    sa.Column('start_position_lat', sa.FLOAT(), nullable=True),
    sa.Column('start_position_long', sa.FLOAT(), nullable=True),
    sa.Column('end_position_lat', sa.FLOAT(), nullable=True),
    sa.Column('end_position_long', sa.FLOAT(), nullable=True),
    sa.Column('total_ascent', sa.NUMERIC(), nullable=True),
    sa.Column('total_descent', sa.NUMERIC(), nullable=True),
    sa.Column('total_distance', sa.NUMERIC(), nullable=True),
    sa.Column('start_time', sa.DATETIME(), nullable=True),
    sa.Column('total_timer_time', sa.NUMERIC(), nullable=True),
    sa.Column('total_elapsed_time', sa.NUMERIC(), nullable=True),
    sa.Column('run_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['run_id'], ['run.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timezone',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('day',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('sunrise', sa.DATETIME(), nullable=True),
    sa.Column('sunset', sa.DATETIME(), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('race',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###