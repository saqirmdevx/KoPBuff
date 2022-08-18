<template>
   <table class="table table-dark table-hover">
    <thead>
        <tr>
        <th scope="col">Match ID</th>
        <th scope="col">Gamemode</th>
        <th scope="col">Result</th>
        <th scope="col">Duration</th>
        <th scope="col">Blue Team</th>
        <th scope="col">Red Team</th>

        </tr>
    </thead>
        <tbody ref="tablebody">
        
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

    methods: {
        addMatch(matchID, gamemode, winningTeam, gameDuration, gameHerosBlue, gameHerosRed) {
            const tableBody = this.$refs.tablebody
            const row = tableBody.insertRow();
            const matchIDCell = row.insertCell();
            const gamemodeCell = row.insertCell();
            const winningTeamCell = row.insertCell();
            const gameDurationCell = row.insertCell();
            const gameHerosBlueCell = row.insertCell();
            const gameHerosRedCell = row.insertCell();

            matchIDCell.innerText = matchID;
            gamemodeCell.innerText = gamemode;
            winningTeamCell.innerText = winningTeam;
            gameDurationCell.innerText = Math.floor(gameDuration / 60) + ":" + gameDuration % 60;

            const game_hero_images = {}
                // game_hero_images[hero] = `<img src="@/assets/creatures/heros/${heros_reversed[hero]}/hero_face.png" alt="${hero}" width="32" height="32">`
            gameHerosBlue.forEach(hero => {
                game_hero_images[hero] = `<img src="${require(`@/assets/creatures/heroes/${heros_reversed[hero]}/hero_face.png`)}" alt="${hero}" width="32" height="32">`
            });
            gameHerosRed.forEach(hero => {
                game_hero_images[hero] = `<img src="${require(`@/assets/creatures/heroes/${heros_reversed[hero]}/hero_face.png`)}" alt="${hero}" width="32" height="32">`
            });

            gameHerosBlueCell.innerHTML = gameHerosBlue.map(hero => game_hero_images[hero]).join(" ");
            gameHerosRedCell.innerHTML = gameHerosRed.map(hero => game_hero_images[hero]).join(" ");

        },
    }
     
}


</script>

<style scoped>

</style>
