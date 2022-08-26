<template>
       <!-- `@/assets/creatures/heroes/${heros_reversed[hero]}/hero_face.png`)} -->
   <div class="partial-match mb-2"  >
        <div class="row">
            <div role="button" class="col-2" @click="onClick(player.game_id)">
                <div class="row">
                    <div class="col-12">
                        <p class="text-center" :class="(player.won && 'won' || 'lost') + '-text'">{{player.won && 'Won' || 'Lost'}}</p>
                    </div>
                    
                </div>

                 <div class="row">
                    <div class="col-12">
                        <p class="text-center">2v2</p>
                    </div>
                </div>

                 <div class="row">
                    <div class="col-12">
                        <p class="text-center">12 hours ago</p>
                    </div>
                </div>
            </div>
            <div class="col-10">
                <div class="row">
                    <div class="col-2 mt-1">
                        <HeroIcon class="hero-icon" :hero_name="getHeroName(player.hero)" width="48" height="48"></HeroIcon>
                    </div>
                    

                    <div class="col-3 mt-3">
                       <span class="kills">{{player.kills}}/</span><span class="deaths">{{player.deaths}}/</span><span class="assists">{{player.assists}}</span>
                    </div>

                    <!-- <div class="col mt-3"> -->
                        <!-- <ItemIcon class="item-icon" :item_name="item_name" width="32" height="32" v-for="(item_name, index) in player.items" :key="index"></ItemIcon>     -->
                    <!-- </div>  -->


                </div>

                
            </div>
        </div>
        
   </div>
</template>

<script>

import HeroIcon from './hero_icon.vue';
// import ItemIcon from './item_icon.vue';
import utils from "@/utils";
export default {
    name: "KopMatchHistory",

    components: {
        HeroIcon,
        // ItemIcon
    },

    props:{
        player: Object
    },

    data () {
        return {
            utils
        }
    },

    methods: {
        onClick(id) {
            console.log(id);
            this.$router.push({ name: 'Match', params: { id } })
        },

        getHeroName(id) {
            return this.utils.getHeroById(id);
        }
    },

    computed: {
        
    }
}

</script>

<style scoped>
.partial-match {
    background-color: #264653;
    height: 60px;
    /* width: 80%; */
    border: 1px solid #005B80;
}

.won-text {
     color: #57A773 !important;
}


.lost-text {
     color: #E76F51 !important;
}

p {
    margin-bottom: 0;
    line-height: 20px;
    font-size: 16px;
}



@media only screen and (max-width: 480px) {
    .partial-match {
        height: 100px;
    }

    p {
        font-size: 15px;
    }

    .hero-icon {
        width: 30px !important;
        height: 30px !important;
    }

    .item-icon {
        width: 30px;
        height: 30px;
    }

    p {
        line-height: 15px;
        font-size: 12px;
    }

}

.dropdown-btn {
    position: relative;
    display: inline-block;
    width: 30px;
    height: 100%;
    left: 15px;
    border: 1px solid red;
}

</style>
