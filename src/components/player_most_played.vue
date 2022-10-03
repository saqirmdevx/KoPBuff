<template>

    <div class="most-played-container p-2">
        <div class="d-flex">
            <HeroIcon :hero_name="heroData.heroId" width="48" height="48"></HeroIcon>
            <div class="ms-3 d-flex flex-column w-100 text-center">
                <div class="row">
                    <div class="col-4">
                        <span>{{utils.getHeroName(heroData.heroId)}}</span>
                    </div>
                    <div class="col-4">
                        <span>{{KDA}} KDA</span>

                    </div>
                    <div class="col-4">
                        <span>{{winrate}}</span>
                    </div>
                </div>

                    <div class="specific-stats row text-center">
                        <div class="col-4">
                            <span>{{averageCS}}</span>
                        </div>

                        <div class="col-4">
                            <span>{{averageKDA}}</span>
                        </div>

                        <div class="col-4">
                            <span>{{heroData.seasonGamesTotal}} Played</span>
                        </div>

                </div>
            </div>
            
            

        </div>
    </div>
</template>



<script>
/* eslint-disable */
import utils from "@/utils";
// import match_history from "./../assets/pretty_match_history.json";
import HeroIcon from './hero_icon.vue';


export default {
    name: "KopMostPlayedHeros",
    props: {
        heroData: {}
    },

    components: {
        HeroIcon,
    },

    data(){
        return {
            utils

        }
    },


    computed: {
        winrate(){
            const total = this.heroData.seasonGamesTotal
            const losses = this.heroData.seasonGamesLost
            const wins = total - losses
            console.log(wins, losses, total)
            return `${(wins/total*100).toFixed(2)}%`
        },

        KDA(){
            const KDA = (this.heroData.kills + this.heroData.assists) / this.heroData.deaths
            if (KDA == Infinity){
                return "Perfect"
            }
            return KDA.toFixed(2)
        },

        averageKDA(){
            const total = this.heroData.seasonGamesTotal
            const kills = this.heroData.kills
            const deaths = this.heroData.deaths
            const assists = this.heroData.assists
            return `${(kills/total).toFixed(0)} / ${(deaths/total).toFixed(0)} / ${(assists/total).toFixed(0)}`
        },

        averageCS(){
            const total = this.heroData.seasonGamesTotal
            const minions = this.heroData.lastHits || 1
            return `${(minions/total).toFixed(0) || 1} CS`
        }
    }

}


</script>

<style scoped>
.most-played-container  {
    background-color: #01212e;
    font-size: 20px;
    height: auto;
    border-top: 1px solid hsla(197, 37%, 24%, 0.5)
}

.specific-stats span {
    color: grey !important;
    font-size: 16px;
    white-space: nowrap;
}
</style>
