"""add households filter to meal plans

Revision ID: 1fe4bd37ccc8
Revises: be568e39ffdf
Create Date: 2024-09-18 14:52:55.831540

"""

import sqlalchemy as sa
from alembic import op

import mealie.db.migration_types

# revision identifiers, used by Alembic.
revision = "1fe4bd37ccc8"
down_revision: str | None = "be568e39ffdf"
branch_labels: str | tuple[str, ...] | None = None
depends_on: str | tuple[str, ...] | None = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "plan_rules_to_households",
        sa.Column("group_plan_rule_id", mealie.db.migration_types.GUID(), nullable=True),
        sa.Column("household_id", mealie.db.migration_types.GUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["group_plan_rule_id"],
            ["group_meal_plan_rules.id"],
        ),
        sa.ForeignKeyConstraint(
            ["household_id"],
            ["households.id"],
        ),
        sa.UniqueConstraint("group_plan_rule_id", "household_id", name="group_plan_rule_id_household_id_key"),
    )
    with op.batch_alter_table("plan_rules_to_households", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_plan_rules_to_households_group_plan_rule_id"), ["group_plan_rule_id"], unique=False
        )
        batch_op.create_index(batch_op.f("ix_plan_rules_to_households_household_id"), ["household_id"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("plan_rules_to_households", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_plan_rules_to_households_household_id"))
        batch_op.drop_index(batch_op.f("ix_plan_rules_to_households_group_plan_rule_id"))

    op.drop_table("plan_rules_to_households")
    # ### end Alembic commands ###
