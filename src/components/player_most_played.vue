<template>
    <div class="mb-2" v-for="(hero_data, hero_name) in most_played_heros" :key="hero_name">
        <div>
            <img class="hero-img"
            :src="require(`../assets/creatures/heroes/${heros_reversed[hero_name]}/hero_face.png`)"
            width="48" height="48">
            <span>{{Math.floor(hero_data.winrate)}}% ({{hero_data.wins + hero_data.losses}})</span>
        </div>
    </div>
</template>



<script>


import match_history_methods from '@/match_history_methods'
import match_history from "./../assets/pretty_match_history.json";

import item_names_to_png_names from "./../assets/item_names_to_png_names.json";

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
    name: "KopMostPlayedHeros",
    props: {
        player_name: String
    },

    data () {
        return {
            heros_reversed,
            match_history,
            match_history_methods,
            item_names_to_png_names,
            most_played_heros: match_history_methods.get_most_played_hero_and_winrate(match_history, this.player_name)
        }
    },

    mounted () {
        console.log(this.most_played_heros)
    },

    methods: {
    
    }
     
}


</script>

<style scoped>
div {
    background-color: rgb(150, 150, 150);
}
</style>
