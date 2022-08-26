import api_communication from "./api_communication";

// TODO Make stuff cacheable with local storage

const team = {
    blue: 1,
    red: 2,
} 

const heroesNames = []

api_communication.getHeroesNames().then(data => {
    for (let hero of data) {
        heroesNames.push(hero.charAt(0).toUpperCase() + hero.slice(1).toLowerCase())
    }
});


const prettyMatch = match => {
    const newMatch = structuredClone(match)
    newMatch.winnerName = newMatch.winner_team === team.blue ? "blue" : "red"
    newMatch["MatchData"].forEach(player => {
        player.teamName = player.team === team.blue ? "blue" : "red"
        player.heroName = getHeroNameById(player.heroId)
        player.won = player.teamName === newMatch.winnerName
    });
    return newMatch;
}


const getMatches = async (numberOfMatches, playerName=null) => {
    const matches = await api_communication.getMatches(numberOfMatches, playerName);
    const newMatches = [];
    matches.forEach(match => {
        newMatches.push(prettyMatch(match));
    });
    return newMatches;
}

import match_history from "./assets/match_history.json";

const matchHistory = match_history;


const sortObjectByValue = obj => {
    let sorted = {};
    Object.keys(obj).sort((a, b) => {
        return obj[b] - obj[a];
    }).forEach(key => {
        sorted[key] = obj[key];
    });
    return sorted;
}

// const sortObjectByKey = obj => {
//     let sorted = {};
//     Object.keys(obj).sort((a, b) => {
//         return a - b;
//     }).forEach(key => {
//         sorted[key] = obj[key];
//     });
//     return sorted;
// }

const getHeroNameById = id => heroesNames[id]
const getHeroIdByName = heroName => heroesNames.indexOf(heroName)
const playerWon = (player, match) => player["team"] === match["winner_team"];


const getPlayersByTeam = (team, match) => {
    let players = [];
    console.log(match)
    match["MatchData"].forEach(player => {
        if (player["team"] === team) {
            players.push(player);
        }
    });
    return players;
}


const getHerosByTeam = (team, match) => {
    let heros = [];
    getPlayersByTeam(team, match).forEach(player => {
        heros.push(player["heroId"]);
    });
    return heros;
}
const getAllPlayers = match => {
    let players = [];
    players = players.concat(getPlayersByTeam(team.blue, match));
    players = players.concat(getPlayersByTeam(team.red, match));
    return players;
}


const getPlayerMatchesByName = (playerName, matches=null) => {
    if (matches === null) {
        matches = matchHistory;
    }
    let playerMatches = [];
    matches.forEach(match => {
        getAllPlayers(match).forEach(player => {
            if (player["player_name"] === playerName) {
                playerMatches.push(match);
            }
        });
    });
    return playerMatches;
}


const getPlayerByName = (playerName, match) => {
    let players = getAllPlayers(match);
    for (let player of players) {
        if (player["player_name"] == playerName) {
            return player;
        }
    }
    return null;
}


// const getHeroByName = (heroName, match) => {
//     const heroId = heroesNames.indexOf(heroName);
//     let players = getAllPlayers(match);
//     for (let player of players) {
//         if (player["hero"] == heroId) {
//             return player;
//         }
//     }
//     return null;
// }


const getMostPlayedHero = player => {
    let mostPlayed_counter = 0
    let mostPlayed = null

    const heroes = player["AccountHeroStats"];
    heroes.forEach(hero => {
        if (hero["gamesTotal"] > mostPlayed_counter) {
            mostPlayed_counter = hero["gamesTotal"];
            mostPlayed = hero
        }
    });

    return mostPlayed;
}





const getItemsUsedAmount = (matches=null) => {
    if (matches == null) {
        matches = matchHistory;
    }
    const items = {}
    matches.forEach(match => {
        getAllPlayers(match).forEach(player => {
            player["items"].forEach(item => {
                if (items[item]) {
                    items[item]++;
                } else {
                    items[item] = 1;
                }
            });
        });
    });
    return sortObjectByValue(items);
}


export default {
    heroesNames,
    team,
    getMatches,
    getHerosByTeam,
    getHeroNameById,
    getHeroIdByName,
    getPlayersByTeam,
    getAllPlayers,
    getPlayerByName,
    playerWon,
    getMostPlayedHero,
    getItemsUsedAmount,
    getPlayerMatchesByName,
    // matchHistory,



}