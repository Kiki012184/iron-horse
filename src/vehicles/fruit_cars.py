import global_constants
from train import FruitVegConsist, FreightCar


def main():
    #--------------- antelope ----------------------------------------------------------------------
    consist = FruitVegConsist(roster='antelope',
                           base_numeric_id=2140,
                           gen=1,
                           subtype='A',
                           track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=20,
                     vehicle_length=5)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FruitVegConsist(roster='antelope',
                           base_numeric_id=2170,
                           gen=2,
                           subtype='A',
                           track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=30,
                     vehicle_length=6)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])

    consist = FruitVegConsist(roster='antelope',
                           base_numeric_id=2180,
                           gen=3,
                           subtype='A',
                           track_type='NG')

    consist.add_unit(type=FreightCar,
                     capacity=40,
                     vehicle_length=8)

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=0,
                              graphics_processor=consist.graphics_processors[0])

    consist.add_model_variant(start_date=0,
                              end_date=global_constants.max_game_date,
                              spritesheet_suffix=1,
                              graphics_processor=consist.graphics_processors[1])
