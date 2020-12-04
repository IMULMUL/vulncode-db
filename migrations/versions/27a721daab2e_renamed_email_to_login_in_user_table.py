"""renamed email to login in user table

Revision ID: 27a721daab2e
Revises: 9d370f33f1a0
Create Date: 2020-12-04 16:14:19.390278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "27a721daab2e"
down_revision = "9d370f33f1a0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "email",
        new_column_name="login",
        existing_type=sa.String(256),
        existing_nullable=False,
    )
    # op.drop_index("email", table_name="user")
    # op.create_unique_constraint("user_login_uniq", "user", ["login"])
    # op.drop_column("user", "email")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "user",
        "login",
        new_column_name="email",
        existing_type=sa.String(256),
        existing_nullable=False,
    )
    # op.add_column("user", sa.Column("email", mysql.VARCHAR(length=256), nullable=False))
    # op.drop_constraint("user_login_uniq", "user", type_="unique")
    # op.create_index("email", "user", ["email"], unique=True)
    # op.drop_column("user", "login")
    # ### end Alembic commands ###
