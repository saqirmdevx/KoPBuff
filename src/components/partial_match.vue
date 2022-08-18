<template>
       <!-- `@/assets/creatures/heroes/${heros_reversed[hero]}/hero_face.png`)} -->
   <div ref="partialMatch" class="partial-match mb-2" @click="onClick(player.game_id)">
        <img class="hero-img" 
        :src="require(`../assets/creatures/heroes/${heros_reversed[player.hero]}/hero_face.png`)"
        width="32" height="32">
        <span class="kills">{{player.kills}}</span>
        <span>/</span>
        <span class="assists">{{player.assists}}</span>
        <span>/</span>
        <span class="deaths">{{player.deaths}}</span>
   </div>
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

export default {
    name: "KopMatchHistory",

    props:{
        player: Object
        // gameId: String,

        // gamemode: String,
        // winningTeam: String,
        // gameDuration: String,
        // gameHerosBlue: Array,
        // gameHerosRed: Array,
    },

    data () {
        return {
            item_names_to_png_names,
            heros_reversed
        }
    },

    methods: {
        onClick(id) {
            this.$router.push({ name: 'Match', params: { id } })
        }
    }
}


</script>

<style scoped>
.partial-match {
    background-color: rgba(150, 150, 150);

}
</style>
