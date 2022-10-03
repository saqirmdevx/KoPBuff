import api_communication from "./api_communication";


const team = {
    blue: 1,
    red: 2,
}


const matchesAdditions = {
    playedAtUtc: "playedAtUtc",
    gameTime: "gameTime",
    winner: "winner",
    mmr: "mmr",
    bans: "bans",

    heroId: "heroId",
    team: "team",
    kills: "kills",
    deaths: "deaths",
    assists: "assists",
    diff: "diff",
    networth: "networth",
    lasthits: "lasthits",
    towerDamage: "towerDamage",
    damageTaken: "damageTaken",
    heroDamage: "heroDamage",
    heroHealing: "heroHealing",
    items: "items",
    auras: "auras",
    talents: "talents",
}

// TODO Make stuff cache-able with local storage


const heroesNames = []
api_communication.getHeroesNames().then(data => {
    for (let hero of data) {
        heroesNames.push(hero.charAt(0).toUpperCase() + hero.slice(1).toLowerCase())
    }
});

const getHeroName = (heroId) => heroesNames[heroId]


const itemNames = []
api_communication.getItems().then(data => {
    for (let key in data) {
        itemNames.push(data[key].replace(".png", ""))
    }
})


const prettyMatch = match => {
    const newMatch = structuredClone(match)
    
    if (newMatch.winner )
        newMatch.winnerName = newMatch.winner === team.blue ? "blue" : "red"

    if (newMatch.bans) 
        newMatch.bans = newMatch.bans.replace(/\[|\]/g, '').split(',').map(Number).map(getHeroNameById); // [0,1] -> ["Kumihu", "Sparrow"]
    
        newMatch["MatchData"].forEach(player => {
        if (player.items)
            player.items = player.items.replace(/\[|\]/g, '').split(',').map(Number).map(getItemNameById); // [1,2,3,4] -> ["item_name1", "item_name2", "item_name3", "item_name4"]
        if (player.team)
            player.teamName = player.team === team.blue ? "blue" : "red"
        if (player.heroId)
            player.heroName = getHeroNameById(player.heroId)
        if (player.teamName && newMatch.winnerName)
            player.won = player.teamName === newMatch.winnerName
    });
    
    return newMatch;
}



const getMatches = async (numberOfMatches, additions=[], playerName=null) => {
    const matches = await api_communication.getMatches(numberOfMatches, additions, playerName);
    const newMatches = [];
    matches.forEach(match => {
        newMatches.push(prettyMatch(match));
    });
    return newMatches;
}


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

const getItemNameById = id => itemNames[id]
// const getItemIdByName = itemName => itemNames.indexOf(itemName)



const getPlayersByTeam = (team, match) => {
    let players = [];
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
    return match["MatchData"];
}


const getPlayerMatchesByName = (playerName, matches=null) => {
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
    try{
        let mostPlayed_counter = 0
        let mostPlayed = null
        console.log(player)

        const heroes = player["AccountHeroStats"];
        heroes.forEach(hero => {
            if (hero["gamesTotal"] > mostPlayed_counter) {
                mostPlayed_counter = hero["gamesTotal"];
                mostPlayed = hero
            }
        });

        return mostPlayed;
    } catch (e) {
        console.log(e)
    }
    
}





const getItemsUsedAmount = (matches=null) => {
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
    getHeroName,
    itemNames,
    team,
    matchesAdditions,
    getMatches,
    getHerosByTeam,
    getHeroNameById,
    getHeroIdByName,
    getPlayersByTeam,
    getAllPlayers,
    getPlayerByName,
    getMostPlayedHero,
    getItemsUsedAmount,
    getPlayerMatchesByName,
}