<template>
    <h1 style="color: rgba(100,100,255)">Blue team</h1>
   <table class="table table-dark table-hover">
    <thead>
        <tr>
            <th scope="col">Hero</th>
            <th scope="col">Player</th>
            <th scope="col">K</th>
            <th scope="col">D</th>
            <th scope="col">A</th>
            <th scope="col">Damage</th>
            <th scope="col">Tower Damage</th>
            <th scope="col">Healing</th>
            <th scope="col">Net</th>
            <th scope="col">Items</th>
            <th scope="col">Talents</th>
        </tr>
    </thead>
        <tbody ref="blueTeamTbody">
        
        </tbody>
    </table>

    <h1 style="color: rgba(255,100,100)">Red team</h1>
    <table class="table table-dark table-hover">
    <thead>
        <tr>
            <th scope="col">Hero</th>
            <th scope="col">Player</th>
            <th scope="col">K</th>
            <th scope="col">D</th>
            <th scope="col">A</th>
            <th scope="col">Damage</th>
            <th scope="col">Tower Damage</th>
            <th scope="col">Healing</th>
            <th scope="col">Net</th>
            <th scope="col">Items</th>
            <th scope="col">Talents</th>
        </tr>
    </thead>
        <tbody ref="redTeamTbody">
        
        </tbody>
    </table>
</template>

<script>

const heros_reversed = {
  "Kumihu": 0,
  "Sparrow": 1,
  "Belle": 2,
  "Iceat": 3,
  "Thomas": 4,
  "Veil": 5,
  "Flin": 6,
  "Kira": 7,
  "Hazel": 8,
  "Arel": 9,
  "Alvar": 10,
}


import item_names_to_png_names from "./../assets/item_names_to_png_names.json";
import match_history_methods from "@/match_history_methods";
import match_history from "./../assets/pretty_match_history.json";


export default {
    name: "KopMatchHistory",

    props:{
        gameId: String,
        gamemode: String,
        winningTeam: String,
        gameDuration: String,
        gameHerosBlue: Array,
        gameHerosRed: Array,
    },

    mounted () {
       this.match = match_history_methods.get_games_by(match_history, (game) => {
        return game.id == this.$route.params.id
       })[0]
       
        for (const player_name in this.match.blue_team) {
            this.addPlayer(player_name, "blueTeam", this.match.blue_team[player_name])
        }
        for (const player_name in this.match.red_team) {
            this.addPlayer(player_name, "redTeam", this.match.red_team[player_name])
        }
    },

    methods: {
        addPlayer(player_name, team, player) {
            const tableBody = this.$refs[team + "Tbody"];

            const row = tableBody.insertRow();
            const heroCell = row.insertCell();
            const playerCell = row.insertCell();
            const killsCell = row.insertCell();
            const deathsCell = row.insertCell();
            const assistsCell = row.insertCell();
            const damageCell = row.insertCell();
            const towerDamageCell = row.insertCell();
            const healingCell = row.insertCell();
            const networthCell = row.insertCell();
            const itemsCell = row.insertCell();
            const talentsCell = row.insertCell();

            const hero_image = `<img src="${require(`@/assets/creatures/heroes/${heros_reversed[player.hero]}/hero_face.png`)}" alt="${player.hero}" width="32" height="32">`

            heroCell.innerHTML = hero_image;


            playerCell.innerText = player_name;
            killsCell.innerText = player.kills;
            deathsCell.innerText = player.deaths;
            assistsCell.innerText = player.assists;
            damageCell.innerText = player.total_damage;
            towerDamageCell.innerText = player.tower_damage;
            healingCell.innerText = player.total_healing;
            networthCell.innerText = player.total_net;

            const game_item_images = []
            player.items.forEach(item => {
                if (item != "empty"){
                    item = item_names_to_png_names[item];
                    game_item_images.push(`<img class='mr-2' src="${require(`@/assets/itemUsed/${item}`)}" alt="${item}" width="32" height="32">`)
                }else{
                    game_item_images.push(`<img class='mr-2' src="${require(`@/assets/itemUsed/empty.png`)}" alt="empty" width="32" height="32">`)
                }
            });

            itemsCell.innerHTML = Object.values(game_item_images).join("")
            talentsCell.innerHTML = player.talents;
        },
    }
}


</script>

<style scoped>
</style>
