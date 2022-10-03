<template>
    <div class="row">
        <div class="col-12">
            <div class="player-card p-4">
                <div class="row">
                    
                    <div class="col-1">
                        <div class="player-card-image">
                            <img :src="player.picture" alt="">
                        </div>
                    </div>
                    <div class="col-1">
                        <h1 class="player-card-text">{{player.name}}</h1>
                    </div>
                </div>
                
                
            </div>
        </div>
    </div>


    <div class="row">
        <div class="col-4">
            <div class="most-played-heroes-container">
                <div class="most-played-heroes-head-bg">
                    <h3 class="text-white">Most Played Heros</h3>
                </div>
                <mostPlayedHero v-for="(heroData, index) of player.AccountHeroStats" :key="heroData.heroId" :heroData="heroData" :index="index"></mostPlayedHero>
            </div>
        </div>
        <div class="col-8">
            <div class="game-card"></div>
        </div>
    </div>
    
</template>

<script>



// import partial_match from '@/components/partial_match.vue';
import api_communication from '@/api_communication';
import mostPlayedHero from '@/components/player_most_played.vue';

export default {
    name: "KopMatchHistory",
    components: {
        // partial_match,
        mostPlayedHero
    },
    data () {
        return {
            api_communication,
            player: {},
        }
    },

    mounted () {
        api_communication.getPlayer(this.$route.params.name).then((playerData) => {
            this.player = playerData
            console.log(this.player)
        }).catch((error) => { // handle this error and display it on the frontend
            console.log(error);
        });
        
    },

    methods: {
      
    }
     
}


</script>

<style scoped>

/* -----------top player card------------ */

.player-card {
    background-color: #01212E;
    width: 100%;
    height: 100px;
    margin-bottom: 15px;
    padding: 15px;
}

.player-card-image {
    width: 50px;
    height: 50px;
    background-color: white;
}

.player-card-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.player-card-text {
    color: white;
}


/* ----------most played------------- */

.most-played-heroes-container {
    background-color: #021821;
    width: 100%;
    height: 600px;
    border: 1px solid #0C2630;
}

.most-played-heroes-head-bg {
    background-color: #011D28;
    width: 100%;
    height: 50px;
}


.most-played-hero-card {

}

.most-played-hero-image {

}

.most-played-hero-top-text {

}

.most-played-hero-bottom-text {
    
}

h3 {
    text-align: center;
    line-height: 50px;
}

/* ----------games------------- */

.game-card {
    width: 100%;
    height: 100px;
    background: #021821;
    border: 1px solid #0C2630;
}

</style>
