<template>
    <div>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Match ID</th>
                    <th scope="col">Game Mode</th>
                    <th scope="col">Result</th>
                    <th scope="col">Duration</th>
                    <th class="blue-team-text" scope="col">Blue Team</th>
                    <th class="red-team-text" scope="col">Red Team</th>
                </tr>
            </thead>

            <tbody>
               <tr v-for="(match) in matches" :key="match.id">
                    <td>{{match.id}}</td>
                    <td>{{calcGamemode(match)}}</td>
                    <td :class="utils.team.blue == match.winner ? 'blue-team-text' : 'red-team-text'">{{utils.team.blue == match.winner ? 'Blue Team' : 'Red Team'}}</td>
                    <td>{{secondsToMinutes(match.gameTime)}}</td>
                     <td>
                        <HeroIcon v-for="(heroName, index) in utils.getHerosByTeam(this.utils.team.blue, match)" :hero_name="heroName" width="48" height="48" :key="index"></HeroIcon>
                     </td>
                    <td>
                        <HeroIcon v-for="(heroName, index) in utils.getHerosByTeam(this.utils.team.red, match)" :hero_name="heroName" width="48" height="48" :key="index"></HeroIcon>
                    </td>
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
            utils,
        }
    },

    async mounted () {
        this.matches = await this.utils.getMatches(20, [
            this.utils.matchesAdditions.winner,
            this.utils.matchesAdditions.heroId, 
            this.utils.matchesAdditions.gameTime,
            this.utils.matchesAdditions.team,
        ])
        console.log(this.matches)
    },

    methods: {
        sortMatchesKey(matches, key) {
            return matches.sort((a, b) => {
                return b[key] - a[key]
            })
        },

        sortMatchesByID(matches) {
            return this.sortMatchesKey(matches, 'id')
        },

        sortMatchesByGameTime(matches) {
            return this.sortMatchesKey(matches, 'gameTime')
        },

        sortMatchesByWinner(matches) {
            return this.sortMatchesKey(matches, 'winner')
        },

        
        
        secondsToMinutes(seconds){
            return Math.floor(seconds / 60) + ":" + (seconds % 60).toString().padStart(2, "0");            
        },

        calcGamemode(match) {
            // Calculates if it is a 1v1, 2v2, 1v2, etc.. based on the MatchData and team.
            console.log(420, match)
            const matchData = match.MatchData;
            const teams = {
                1: 0,
                2: 0,
            }
            matchData.forEach(player => {
                teams[player.team] += 1;
            });
            return `${teams[1]}v${teams[2]}`
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
    color: white !important;
    text-align: center;
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

.red-team-text {
    color: 	rgb(238, 75, 43)
}
.blue-team-text {
    color: rgb( 0, 150, 255	);
}


</style>