<template>
   <div>
    <img src="" :width="width || 32" :height="height || 32" ref="hero-img" @click.self="onClick()">
   </div>
</template>

<script>

const heros_reversed = {
  "Kumihu": 0,
  "Sparrow": 1,
  "Belle": 2,
  "Iceat": 3,
  "Thomas": 4,
  "Veil": 5,
  "Flin": 6,
  "Kira": 7,
  "Hazel": 8,
  "Arel": 9,
  "Alvar": 10,
}

export default {
    name: "KopHeroIcon",

    props:{
        hero_name: String,
        width: Number,
        height: Number,
    },

    mounted () {
        this.$refs["hero-img"].src = require(`@/assets/creatures/heroes/${heros_reversed[this.hero_name]}/hero_face.png`)
    },

    methods: {
        onClick(){
            this.$router.push({ name: 'Hero', params: { name: this.hero_name } })
        }
    }
     
}


</script>

<style scoped>
</style>
