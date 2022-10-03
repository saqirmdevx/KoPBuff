<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col"></th>
                    <th scope="col">Name</th>
                    <th scope="col">Games Played</th>
                    <th scope="col">Win Rate</th>
                    <th scope="col">KDA</th>
                    <th scope="col">Pick Rate</th>
                    <th scope="col">Ban Rate</th>
                    <th scope="col" title="Formula: (KDA * 0.5 + Winrate * 0.25 + TowerDamage * 0.1 + HeroDamage * 0.1 + DamageTaken * 0.1 + Networth * 0.1 + Games * 0.1)">Points</th>
                    
                </tr>
            </thead>

            <tbody>
               <tr v-for="(heroDetails, heroName, index) in heroesDetails" :key="index">
                    <td><HeroIcon :hero_name="heroName" width="48" height="48"></HeroIcon></td>
                    <td>{{heroName}}</td>
                    <td>{{heroDetails.games}}</td>
                    <td>{{heroDetails.winrate}}</td>
                    <td>{{heroDetails.kda}}</td>
                    <td>{{heroDetails.pickrate}}</td>
                    <td>{{heroDetails.banrate}}</td>
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
            heroesDetails: {},
            utils,
        }
    },


    async mounted () {
        const matches = await this.utils.getMatches(200, [
            this.utils.matchesAdditions.winner,
            this.utils.matchesAdditions.heroId, 
            this.utils.matchesAdditions.gameTime,
            this.utils.matchesAdditions.team,
            this.utils.matchesAdditions.kills,
            this.utils.matchesAdditions.deaths,
            this.utils.matchesAdditions.assists,
            this.utils.matchesAdditions.towerDamage,
            this.utils.matchesAdditions.heroDamage,
            this.utils.matchesAdditions.bans,
            this.utils.matchesAdditions.lasthits,
            this.utils.matchesAdditions.damageTaken,
            this.utils.matchesAdditions.networth,
        ])

        

        console.log(matches)
        
        this.heroesDetails = {}
        this.utils.heroesNames.forEach(hero => {
            if (hero != "Dummy"){
                this.heroesDetails[hero] = {
                    games: 0,
                    wins: 0,
                    losses: 0,

                    kills: 0,
                    deaths: 0,
                    assists: 0,
                    kda: 0,
                    lastHits: 0,
                    towerDamage: 0,
                    heroDamage: 0,
                    heroHealing: 0,
                    damageTaken: 0,
                    networth: 0,
                    bans: 0,
                    winrate: 0,
                    pickrate: 0,
                    banrate: 0,
                    points: 0,
                }
            }
        })

        
        matches.forEach(match => {
            match.bans.forEach(ban => {
                this.heroesDetails[ban].bans++
            })
            this.utils.getAllPlayers(match).forEach(player => {
                if(player.won){
                    this.heroesDetails[player.heroName].wins++
                } else {
                    console.log(player.heroName)
                    console.log(match)
                    this.heroesDetails[player.heroName].losses++
                }
                this.heroesDetails[player.heroName].kills += player.kills
                this.heroesDetails[player.heroName].deaths += player.deaths
                this.heroesDetails[player.heroName].assists += player.assists

                this.heroesDetails[player.heroName].lastHits += player.lasthits
                this.heroesDetails[player.heroName].towerDamage += player.towerDamage
                this.heroesDetails[player.heroName].heroDamage += player.heroDamage
                this.heroesDetails[player.heroName].heroHealing += player.heroHealing
                this.heroesDetails[player.heroName].damageTaken += player.damageTaken
                this.heroesDetails[player.heroName].networth += player.networth

                
            })
        })
        for (let hero in this.heroesDetails) {
            this.heroesDetails[hero].games = this.heroesDetails[hero].wins + this.heroesDetails[hero].losses
            this.heroesDetails[hero].winrate = (this.heroesDetails[hero].wins / this.heroesDetails[hero].games * 100).toFixed(2)
            this.heroesDetails[hero].pickrate = (this.heroesDetails[hero].games / this.heroesDetails[hero].wins).toFixed(2)
            this.heroesDetails[hero].banrate = (this.heroesDetails[hero].games / this.heroesDetails[hero].losses).toFixed(2)
            this.heroesDetails[hero].kda = ((this.heroesDetails[hero].kills + this.heroesDetails[hero].assists) / this.heroesDetails[hero].deaths).toFixed(2)
            this.heroesDetails[hero].points = (this.heroesDetails[hero].kda * 0.5 + this.heroesDetails[hero].winrate * 0.25 + this.heroesDetails[hero].towerDamage * 0.1 + this.heroesDetails[hero].heroDamage * 0.1 + this.heroesDetails[hero].damageTaken * 0.1 + this.heroesDetails[hero].networth * 0.1 + this.heroesDetails[hero].games * 0.1).toFixed(2)
            
        }
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