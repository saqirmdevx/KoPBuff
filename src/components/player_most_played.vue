<template>
    <div class="mb-2" v-for="(hero_data, hero_name) in most_played_heros" :key="hero_name">
        <div>
            <HeroIcon :hero_name="hero_name" width="32" height="32"></HeroIcon>
            <span>{{Math.floor(hero_data.winrate)}}% ({{hero_data.wins + hero_data.losses}})</span>
        </div>
    </div>
</template>



<script>
import match_history_methods from '@/match_history_methods'
import match_history from "./../assets/pretty_match_history.json";
import HeroIcon from './hero_icon.vue';


export default {
    name: "KopMostPlayedHeros",
    props: {
        player_name: String
    },

    components: {
        HeroIcon,
    },

    data () {
        return {
            match_history,
            match_history_methods,
            most_played_heros: match_history_methods.get_most_played_hero_and_winrate(match_history, this.player_name)
        }
    },     
}


</script>

<style scoped>
div {
    background-color: rgb(150, 150, 150);
}
</style>
