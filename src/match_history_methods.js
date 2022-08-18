
const hero_names = [
    "Kumihu",
    "Sparrow",
    "Belle",
    "Iceat",
    "Thomas",
    "Veil",
    "Flin",
    "Kira",
    "Hazel",
    "Arel",
    "Alvar",
]


const get_game_count = (match_history) => {
    return match_history.length;
}

const get_games_by = (match_history, filter) => {
    return match_history.filter(filter);
}

const get_player_by_name = (match_history, player_name) => {
    let player_games = [];
    for (let game of match_history) {
        if (game["blue_team"][player_name]) {
            player_games.push(game["blue_team"][player_name]);
        } else if (game["red_team"][player_name]) {
            player_games.push(game["red_team"][player_name]);
        }
    }

    return player_games;
}

const get_most_played_hero_and_winrate = (match_history, player_name) => {
    let player_games = get_player_by_name(match_history, player_name);
    let hero_winrates = {};
    for (let hero of hero_names) {
        hero_winrates[hero] = {wins: 0, losses: 0, winrate: 0, kills: 0, deaths: 0, assists: 0, avg_kda: 0};
    }
    for (let game of player_games) {
        console.log(game)
        if (game["won"]) {
            hero_winrates[game["hero"]]["wins"]++;
        } else {
            hero_winrates[game["hero"]]["losses"]++;
        }
        hero_winrates[game["hero"]]["kills"] += game["kills"];
        hero_winrates[game["hero"]]["deaths"] += game["deaths"];
        hero_winrates[game["hero"]]["assists"] += game["assists"];
        hero_winrates[game["hero"]]["winrate"] = hero_winrates[game["hero"]]["wins"] / (hero_winrates[game["hero"]]["wins"] + hero_winrates[game["hero"]]["losses"]) * 100;
    }

    // Sort by number of games.
    let sorted_heros = {}
    Object.keys(hero_winrates).sort((a, b) => {
        return hero_winrates[b]["wins"] + hero_winrates[b]["losses"] - hero_winrates[a]["wins"] - hero_winrates[a]["losses"];
    }).forEach((key) => {
        sorted_heros[key] = hero_winrates[key];
    });

    return sorted_heros;
}


const get_avg_player_specific_stats = (match_history, specific_stat) => {
    let specific_stat_count = 0;
    match_history.forEach((game) => {
        Object.keys(game.blue_team).forEach((player) => {
            specific_stat_count += game.blue_team[player][specific_stat];
        });
        Object.keys(game.red_team).forEach((player) => {
            specific_stat_count += game.red_team[player][specific_stat];
        });
    });
    return specific_stat_count / (match_history.length * 2);
}

export default {
    get_game_count,
    get_games_by,
    get_player_by_name,
    get_avg_player_specific_stats,
    get_most_played_hero_and_winrate,
}