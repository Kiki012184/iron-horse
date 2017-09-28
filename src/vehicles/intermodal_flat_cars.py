import global_constants
from train import IntermodalConsist, Wagon

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = IntermodalConsist(title = '[Intermodal Flat Car]',
                           roster = 'pony',
                           base_numeric_id = 1060,
                           wagon_generation = 3,
                                        intro_date = 1960,
                           vehicle_life = 40,
                           speedy = True)

    consist.add_unit(Wagon(consist = consist,
                            capacity_freight = 40, # was matched for some time to RH and Squid containers, but blah
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date,
                           graphics_processor = consist.graphics_processors[0])


    #--------------- llama ----------------------------------------------------------------------
