import global_constants
from train import TypeConfig, WagonConsist, Wagon

# no graphics processing - don't random colour cabeese, I tried it, looks daft

type_config = TypeConfig(base_id = 'caboose_car',
                template = 'train.pynml',
                class_refit_groups = [], # refit nothing, don't mess with this, it breaks auto-replace
                label_refits_allowed = [],
                label_refits_disallowed = [],
                default_cargo = 'GOOD', # unwanted side-effect of this is that caboose replaceable by anything refitting goods
                default_capacity_type = 'capacity_freight')

type_config_ng = TypeConfig(base_id = 'caboose_car_ng',
                template = 'train.pynml',
                class_refit_groups = [], # refit nothing, don't mess with this, it breaks auto-replace
                label_refits_allowed = [],
                label_refits_disallowed = [],
                default_cargo = 'GOOD', # unwanted side-effect of this is that caboose replaceable by anything refitting goods
                default_capacity_type = 'capacity_freight',
                track_type = 'NG')

def main():
    #--------------- brit ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Caboose Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        speedy = True,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


    consist = WagonConsist(type_config = type_config_ng,
                        title = '[Caboose Car]',
                        roster = 'brit',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        use_legacy_spritesheet = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 10,
                            vehicle_length = 4))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)

    #--------------- soam ----------------------------------------------------------------------
    consist = WagonConsist(type_config = type_config,
                        title = '[Caboose Car]',
                        roster = 'soam',
                        wagon_generation = 1,
                        replacement_id = '-none',
                        intro_date = 1860,
                        vehicle_life = 40,
                        speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 0,
                            weight = 20,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           spritesheet_suffix=0)


