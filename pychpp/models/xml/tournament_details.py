from datetime import datetime
from typing import Optional

from pychpp.models.ht_field import HTField
from pychpp.models.ht_init_var import HTInitVar
from pychpp.models.ht_model import HTModel


class RequestTournamentDetails(HTModel):
    """
    Tournament Details - Request arguments
    """
    SOURCE_FILE = 'tournamentdetails'
    LAST_VERSION = '1.0'

    _r_tournament_id: int = HTInitVar('tournamentId', init_arg='tournament_id')
    _r_season: Optional[int] = HTInitVar('season', init_arg='season')


class TournamentDetails(RequestTournamentDetails):
    """
    Tournament Details
    """
    XML_PREFIX = 'Tournament/'

    id: int = HTField('TournamentId')
    name: str = HTField('Name')
    type: int = HTField('TournamentType')
    season: int = HTField('Season')
    logo_url: str = HTField('LogoUrl')
    trophy_type: int = HTField('TrophyType')
    number_of_teams: int = HTField('NumberOfTeams')
    number_of_groups: int = HTField('NumberOfGroups')
    last_match_round: int = HTField('LastMatchRound')
    first_match_round_date: datetime = HTField('FirstMatchRoundDate')
    next_match_round_date: datetime = HTField('NextMatchRoundDate')
    is_matches_ongoing: bool = HTField('IsMatchesOngoing')
    creator: 'Creator' = HTField('Creator')


class Creator(HTModel):
    """
    Tournament Details -> Creator
    """
    id: int = HTField('UserId')
    login_name: str = HTField('Loginname')
