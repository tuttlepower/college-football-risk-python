# college-football-risk
Companion API for College Football Risk

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

You can install directly using:

```sh
pip install college_football_risk
```
(you may need to run `pip` with root permission: `sudo pip install college_football_risk`)

Then import the package:
```python
import college_football_risk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import college_football_risk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import college_football_risk
from college_football_risk.rest import ApiException
from pprint import pprint


# Defining host is optional and default to https://collegefootballrisk.com/api
configuration.host = "https://collegefootballrisk.com/api"
# Enter a context with an instance of the API client
with college_football_risk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = college_football_risk.PlayersApi(api_client)
    player = 'player_example' # str | Player username without the \"u/\" (e.g. \"u/BlueSCar\" would just be \"BlueSCar\")

    try:
        # Player information
        api_response = api_instance.get_player(player)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://collegefootballrisk.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PlayersApi* | [**get_player**](docs/PlayersApi.md#get_player) | **GET** /player | Player information
*PlayersApi* | [**get_players**](docs/PlayersApi.md#get_players) | **GET** /players | List of players
*StatsApi* | [**get_leaderboard**](docs/StatsApi.md#get_leaderboard) | **GET** /stats/leaderboard | Game leaderboard
*StatsApi* | [**get_turns**](docs/StatsApi.md#get_turns) | **GET** /turns | Get turns list
*TeamsApi* | [**get_player_moves_by_turn**](docs/TeamsApi.md#get_player_moves_by_turn) | **GET** /api/team/players | Get players moves by turn
*TeamsApi* | [**get_team_history**](docs/TeamsApi.md#get_team_history) | **GET** /stats/team/history | Get historical team stats
*TeamsApi* | [**get_team_strength**](docs/TeamsApi.md#get_team_strength) | **GET** /stats/team | Get current team strength
*TeamsApi* | [**get_teams**](docs/TeamsApi.md#get_teams) | **GET** /teams | Get list of teams
*TerritoriesApi* | [**get_territories**](docs/TerritoriesApi.md#get_territories) | **GET** /territories | Get list of territories
*TerritoriesApi* | [**get_territory_history**](docs/TerritoriesApi.md#get_territory_history) | **GET** /territory/history | Get historical territory data
*TerritoriesApi* | [**get_territory_turn**](docs/TerritoriesApi.md#get_territory_turn) | **GET** /territory/turn | Get teritory statistics for a specific turn


## Documentation For Models

 - [LeaderboardTeam](docs/LeaderboardTeam.md)
 - [Player](docs/Player.md)
 - [PlayerRatings](docs/PlayerRatings.md)
 - [PlayerStats](docs/PlayerStats.md)
 - [PlayerTeam](docs/PlayerTeam.md)
 - [PlayerTeamColors](docs/PlayerTeamColors.md)
 - [PlayerTurns](docs/PlayerTurns.md)
 - [Team](docs/Team.md)
 - [TeamHistory](docs/TeamHistory.md)
 - [TeamHistoryStarBreakdown](docs/TeamHistoryStarBreakdown.md)
 - [TeamPlayer](docs/TeamPlayer.md)
 - [TeamPlayerLastTurn](docs/TeamPlayerLastTurn.md)
 - [TeamStrength](docs/TeamStrength.md)
 - [TeamTurnPlayer](docs/TeamTurnPlayer.md)
 - [Territory](docs/Territory.md)
 - [TerritoryHistory](docs/TerritoryHistory.md)
 - [TerritoryNeighbors](docs/TerritoryNeighbors.md)
 - [TerritoryTurn](docs/TerritoryTurn.md)
 - [TerritoryTurnPlayers](docs/TerritoryTurnPlayers.md)
 - [TerritoryTurnTeams](docs/TerritoryTurnTeams.md)
 - [Turn](docs/Turn.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

admin@collegefootballdata.com


