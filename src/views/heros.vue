<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col"></th>
                    <th scope="col">Name</th>
                    <th scope="col">Games Played</th>
                    <th scope="col">Pick Rate</th>
                    <th scope="col">Ban Rate</th>
                    <th scope="col">Win Rate</th>
                    <th scope="col">Points</th>
                    
                </tr>
            </thead>

            <tbody>
               <tr v-for="(heroDetails, heroName, index) in heroesDetails" :key="index">
                    <td><HeroIcon :hero_name="heroName" width="48" height="48"></HeroIcon></td>
                    <td>{{heroName}}</td>
                    <td>{{heroDetails.games}}</td>
                    <td>{{heroDetails.pickrate}}</td>
                    <td>{{heroDetails.banrate}}</td>
                    <td>{{heroDetails.winrate}}</td>
                    <td>{{heroDetails.points}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

/* eslint-disable vue/no-unused-components */

import HeroIcon from '@/components/hero_icon.vue';
import utils from "@/utils";
// import api_communication from '@/api_communication';

export default {
    name: "KopLeaderboard",
    components: {
        HeroIcon
    },

    data() {
        return {
            matches: [],
            heroesDetails: {},
            utils,
        }
    },

    async mounted () {
       this.matches = await this.utils.getMatches(5)
       console.log(this.matches)
       this.heroesDetails = {}
        this.utils.heroesNames.forEach(hero => {
            if (hero != "Dummy"){
                this.heroesDetails[hero] = {
                    games: 0,
                    wins: 0,
                    losses: 0,
                    winrate: 0,
                    pickrate: 0,
                    banrate: 0,
                    points: 0,
                }
            }
        })
        this.matches.forEach(match => {
            this.utils.getAllPlayers(match).forEach(player => {
                if(player.won){
                    this.heroesDetails[player.heroName].wins++
                    this.heroesDetails[player.heroName].points += 1
                } else {
                    this.heroesDetails[player.heroName].losses++
                    this.heroesDetails[player.heroName].points -= 1
                }
                this.heroesDetails[player.heroName].games++
                this.heroesDetails[player.heroName].winrate = this.heroesDetails[player.heroName].wins / this.heroesDetails[player.heroName].games * 100
                
            })
        })
       
    },

    
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