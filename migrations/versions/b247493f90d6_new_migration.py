"""new migration

Revision ID: b247493f90d6
Revises:
Create Date: 2024-06-06 02:07:57.038709

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "b247493f90d6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
user_role_enum = sa.Enum("USER", "RESELLER", name="userroleenum")


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("first_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("last_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("date_of_birth", sa.Date(), nullable=True),
        sa.Column("address", sa.JSON(), nullable=True),
        sa.Column("phone", sa.JSON(), nullable=True),
        sa.Column("email", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "created_with_ip", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("last_login_on", sa.DateTime(), nullable=False),
        sa.Column(
            "last_login_with_ip", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("profile_pic_url", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("banned", sa.Boolean(), nullable=False),
        sa.Column("role", user_role_enum, nullable=False),
        sa.Column("referral_code", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "used_referral_code", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")

    user_role_enum.drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###