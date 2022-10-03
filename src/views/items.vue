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
                    <th scope="col" title="Games * Winrate * KDA">Points</th>
                    
                </tr>
            </thead>

            <tbody>
               <tr v-for="(itemDetails, itemName, index) in itemDetails" :key="index">
                    <td><ItemIcon :item_name="itemName" width="48" height="48"></ItemIcon></td>
                    <td>{{itemName}}</td>
                    <td>{{itemDetails.games}}</td>
                    <td>{{itemDetails.winrate}}</td>
                    <td>{{itemDetails.kda}}</td>
                    <td>{{itemDetails.points}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

/* eslint-disable vue/no-unused-components */

import ItemIcon from '@/components/item_icon.vue';
import utils from "@/utils";

export default {
    name: "KopItems",
    components: {
        ItemIcon
    },

    data() {
        return {
            itemDetails: {},
            utils,
        }
    },


    async mounted () {
        const matches = await this.utils.getMatches(20, [
            this.utils.matchesAdditions.items,
            this.utils.matchesAdditions.kills,
            this.utils.matchesAdditions.deaths,
            this.utils.matchesAdditions.assists,
            this.utils.matchesAdditions.winner,
            this.utils.matchesAdditions.team
        ])
        
        this.itemDetails = {}

        for (let item of this.utils.itemNames) {
            if (item && item !== "undefined"){
                this.itemDetails[item] = {
                    games: 0,
                    wins: 0,
                    losses: 0,
                    winrate: 0,

                    kills: 0,
                    deaths: 0,
                    assists: 0,
                    kda: 0,

                    points: 0
                }
            }
        }
        matches.forEach(match => {
            this.utils.getAllPlayers(match).forEach(player => {
                player.items.forEach(item => {
                    this.itemDetails[item].games++
                    if(player.won){
                        this.itemDetails[item].wins++
                    } else {
                        this.itemDetails[item].losses++
                    }
                    this.itemDetails[item].kills += player.kills
                    this.itemDetails[item].deaths += player.deaths
                    this.itemDetails[item].assists += player.assists
                })
            })
        })

        for (let item in this.itemDetails){
            this.itemDetails[item].winrate = (this.itemDetails[item].wins / this.itemDetails[item].games * 100).toFixed(2)
            this.itemDetails[item].kda = ((this.itemDetails[item].kills + this.itemDetails[item].assists) / this.itemDetails[item].deaths).toFixed(2)
            this.itemDetails[item].points = (this.itemDetails[item].games * this.itemDetails[item].winrate * this.itemDetails[item].kda).toFixed(2)
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