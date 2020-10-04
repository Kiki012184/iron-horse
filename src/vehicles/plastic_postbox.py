from train import MailEngineRailcarConsist, DieselRailcarMailUnit


def main(roster_id):
    consist = MailEngineRailcarConsist(roster_id=roster_id,
                                       id='plastic_postbox',
                                       base_numeric_id=3080,
                                       name='Plastic Postbox',
                                       role='mail_railcar',
                                       role_child_branch_num=1,
                                       power=560,
                                       gen=5,
                                       sprites_complete=True,
                                       intro_date_offset=-5)  # introduce early by design

    consist.add_unit(type=DieselRailcarMailUnit,
                     weight=37,
                     chassis='railcar_32px',
                     tail_light='railcar_32px_3')

    consist.description = """Some people have big dreams. It's a life of luxury.""" # Paul Hardcastle, Just for Money
    consist.foamer_facts = """BR Class 128/130, BR Class 153/155/156/158 <i>Sprinters</i>."""

    return consist
