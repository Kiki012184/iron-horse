from train import EngineConsist, ElectroDieselEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="ultra_shoebox",
        base_numeric_id=2170,
        name="Ultra Shoebox",
        role="express",
        role_child_branch_num=-1,
        power=1650,
        power_by_railtype={"RAIL": 1650, "ELRL": 2800},
        random_reverse=True,
        pantograph_type="z-shaped-single",
        gen=6,
        default_livery_extra_docs_examples=[
            ("COLOUR_RED", "COLOUR_RED"),
            ("COLOUR_PINK", "COLOUR_WHITE"),
            ("COLOUR_PURPLE", "COLOUR_WHITE"),
            ("COLOUR_CREAM", "COLOUR_MAUVE"),
            ("COLOUR_YELLOW", "COLOUR_YELLOW"),
            ("COLOUR_DARK_BLUE", "COLOUR_BLUE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
        ],
        sprites_complete=True,
    )

    consist.add_unit(
        type=ElectroDieselEngineUnit,
        weight=78,
        vehicle_length=8,
        effect_offsets=[(2, 0)],
        spriterow_num=0,
    )

    consist.description = (
        """Top to bottom, it's an old Shoebox made new. Right powerful small engines."""
    )
    consist.foamer_facts = (
        """Network Rail / GBRF Class 73/9 (re-engineered), BR class 74, proposed Class 75"""
    )

    return consist
