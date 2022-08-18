<template>
       <!-- `@/assets/creatures/heroes/${heros_reversed[hero]}/hero_face.png`)} -->
   <div ref="partialMatch" class="partial-match mb-2" @click.self="onClick(player.game_id)">
        <HeroIcon :hero_name="player.hero" width="32" height="32"></HeroIcon>
        <span class="kills">{{player.kills}}</span>
        <span>/</span>
        <span class="assists">{{player.assists}}</span>
        <span>/</span>
        <span class="deaths">{{player.deaths}}</span>
   </div>
</template>

<script>

import HeroIcon from './hero_icon.vue';

export default {
    name: "KopMatchHistory",

    components: {
        HeroIcon,
    },

    props:{
        player: Object
    },

    methods: {
        onClick(id) {
            this.$router.push({ name: 'Match', params: { id } })
        }
    }
}


</script>

<style scoped>
.partial-match {
    background-color: rgba(150, 150, 150);

}
</style>
