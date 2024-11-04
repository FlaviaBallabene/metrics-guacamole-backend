"""empty message

Revision ID: 083bd0c950a9
Revises: a5cffa318ac2
Create Date: 2024-11-04 20:55:58.676879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '083bd0c950a9'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platform',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('campaign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('budget', sa.Float(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('platform_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['platform_id'], ['platform.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('location_campaign',
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['location.id'], ),
    sa.PrimaryKeyConstraint('location_id', 'campaign_id')
    )
    op.create_table('weekly_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month', sa.String(), nullable=False),
    sa.Column('spending', sa.Float(), nullable=False),
    sa.Column('impressions', sa.Integer(), nullable=False),
    sa.Column('clicks', sa.Integer(), nullable=False),
    sa.Column('conversions', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(), nullable=False))
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    op.drop_table('weekly_data')
    op.drop_table('location_campaign')
    op.drop_table('campaign')
    op.drop_table('project')
    op.drop_table('platform')
    op.drop_table('location')
    # ### end Alembic commands ###
