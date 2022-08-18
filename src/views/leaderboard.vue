<template>
    <div>
        <table class="table table-dark table-hover">
            <thead>
                <tr>
                    <th scope="col">Rank</th>
                    <th scope="col">Hero</th>
                    <th scope="col">Player</th>
                    <th scope="col">Wins</th>
                    <th scope="col">Losses</th>
                    <th scope="col">MMR</th>
                    
                </tr>
            </thead>

            <tbody>
                <tr v-for="(player, index) in leaderboard" :key="player.id">
                    <td>{{index + 1}}</td>
                    <td><HeroIcon :hero_name="mostPlayedHeroes(player.name)" width="48" height="48"></HeroIcon></td>
                    <td>{{player.name}}</td>
                    <td>{{player.games_total - player.games_lost}}</td>
                    <td>{{player.games_lost}}</td>
                    <td>{{player.mmr_2v2}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>


import axios from 'axios';
import { decode } from "msgpackr/unpack";
import { Buffer } from "buffer";

import HeroIcon from '@/components/hero_icon.vue';
import match_history_methods from "@/match_history_methods";
import match_history from "./../assets/pretty_match_history.json";

export default {
    name: "KopLeaderboard",
    components: {
        HeroIcon
    },
    

    data() {
        return {
            leaderboard: [],
            match_history_methods,
            match_history,
            // mostPlayedHeroes
        }
    },

        

    methods: {
       getLeaderboard(type) {
            const url = `https://us.leagueofpixels.eu/api/leaderboard/?type=${type}`
            axios.get(url, {
                responseType: 'arraybuffer'
            }).then((response) => {
                const data = decode(Buffer.from(response.data));
                this.leaderboard = data;
                console.log(data);
            })
       },

       mostPlayedHeroes(playerName) {
            const most_played = match_history_methods.get_most_played_hero(this.match_history, playerName);
            console.log(playerName, most_played);
            return most_played
       }
    },

    mounted() {
       this.getLeaderboard(2)
    }
    
}
</script>

<style scoped>

</style>