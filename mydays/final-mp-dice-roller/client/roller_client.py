import uplink
from uplink_helpers import raise_for_status, response_to_data


@response_to_data
@raise_for_status
@uplink.json
class RollerService(uplink.Consumer):

#    def __init__(self):
#        super(self).__init__(base_url='http://localhost:5000')

    @uplink.get('/roller/roll_turn/{num_dice}')
    def roll_turn(self, num_dice):
        pass

    @uplink.put('/roller/record_score/{player_id}/{current_score}')
    def record_score(self, player_id, current_score):
        pass

    @uplink.put('/roller/record_high_score/{player_id}/{current_score}')
    def record_high_score(self, player_id, current_score):
        pass

    @uplink.get('/roller/check_high_score/{player_id}/{current_score}')
    def check_high_score(self, player_id, current_score):
        pass

    @uplink.get('/roller/find_player/{name}')
    def find_player(self, name):
        pass

    @uplink.post('/roller/create_player/{name}')
    def create_player(self, name):
        pass

    @uplink.get('/roller/get_all_high_scores')
    def get_all_high_scores(self):
        pass

    @uplink.get('/roller/get_all_scores')
    def get_all_scores(self):
        pass

    @uplink.get('/roller/get_all_players')
    def get_all_players(self):
        pass
