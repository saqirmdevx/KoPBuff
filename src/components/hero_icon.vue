
<template>
    <img src=""  :width="width || 32" :height="height || 32" ref="heroImg" @click.self="onClick()">
</template>

<script>

import api_communication from "@/api_communication"
import utils from "@/utils"

export default {
    name: "KopHeroIcon",

    props:{
        hero_name: [String, Number],
        width: String,
        height: String,
    },

    data () {
        return {
            api_communication,
            hero_nameLocal: this.hero_name,
        }
    },

    mounted () {
        if (isNaN(this.hero_name)) { // Converts the hero name to the hero id
            this.hero_nameLocal = utils.getHeroIdByName(this.hero_nameLocal)
        }
        this.$refs.heroImg.src = this.api_communication.getHeroAssetURL(this.hero_nameLocal)
    },

    methods: {
        onClick(){
            this.$router.push({ name: 'Hero', params: { name: this.hero_name } })
        }
    },

    // Stop receiving events from parent
    
     
}

</script>

<style scoped>
</style>
