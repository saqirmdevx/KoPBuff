<template>
    <div class="row">
        <div class="col-3">
            <h3 class="text-white">Most Played Heros</h3>
        </div>
        <div class="col-lg">
            <h1 ref="playerName" class="text-white">{{this.$route.params.name}}</h1>
        </div>
    </div>
    <div class="row">
        <div class="col-3">
            <player_most_played :player_name="this.$route.params.name"></player_most_played>
        </div>
        <div class="col-lg">
            <div v-for="player_game in player_games" :key="player_game.id">
                <partial_match :player="player_game"></partial_match>
            </div>
        </div>
   </div>
</template>

<script>


import match_history_methods from '@/match_history_methods'
import match_history from "./../assets/pretty_match_history.json";
import partial_match from '@/components/partial_match.vue';
import player_most_played from '@/components/player_most_played.vue';

export default {
    name: "KopMatchHistory",
    components: {
        partial_match,
        player_most_played,
    },
    data () {
        return {
            player_games: []
        }
    },

    mounted () {
        this.player_games = match_history_methods.get_player_by_name(match_history, this.$route.params.name)
    },

    methods: {
      
    }
     
}


</script>

<style scoped>

</style>
