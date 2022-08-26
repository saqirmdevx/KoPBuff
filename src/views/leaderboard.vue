<template>
    <div>
        <table class="table">
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
                    <td><HeroIcon :hero_name="utils.getMostPlayedHero(player).heroId" width="48" height="48"></HeroIcon></td>
                    <!-- If index is 1 then gold-text -->
                    <!-- If index is 2 then silver-text -->
                    <!-- If index is 3 then bronze-text -->
                    <!-- If index is 4 or more then nothing -->
                    <td :class="index+1 == 1 ? 'gold-text' : index+1 == 2 ? 'silver-text' : index+1 == 3 ? 'bronze-text' : ''">{{player.name}}</td>
                    <td>{{player.AccountStats.seasonGamesTotal - player.AccountStats.seasonGamesLost}}</td>
                    <td>{{player.AccountStats.seasonGamesLost}}</td>
                    <td>{{player.AccountStats.mmr}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

/* eslint-disable vue/no-unused-components */

import HeroIcon from '@/components/hero_icon.vue';
import utils from "@/utils";
import api_communication from '@/api_communication';

export default {
    name: "KopLeaderboard",
    components: {
        HeroIcon
    },

    data() {
        return {
            colors: {
                gold: 1,
                silver: 2,
                bronze: 3,
            },
            leaderboard: [],
            utils,
            gamemode_types: {
                "1v1": 1,
                "2v2": 2,
            }
        }
    },

    async mounted () {
        this.leaderboard = await api_communication.getLeaderboard()
        console.log(this.colors)
        
    }
    
}



</script>

<style scoped>

th {
    background-color: rgba(2, 24, 33, 0.7);
    border-bottom: 2px solid rgba(22, 44, 53, 1);
}


tr {
    text-align: center;

    color: white !important
}
tr:hover {
    background-color: rgba(2, 24, 33, 0.7);
    filter: brightness(1);
}

td {
    background-color: rgba(2, 24, 33, 0.7);
    filter: brightness(0.8);
    border-bottom: 1px solid rgba(22, 44, 53, 1);
}


.gold-text:before, .gold-text:after {
    content: " 👑 "
}
.silver-text:before, .silver-text:after {
    content: " 🥈 "
}
.bronze-text:before, .bronze-text:after {
    content: " 🥉 "
}



</style>