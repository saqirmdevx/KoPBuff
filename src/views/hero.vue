<template>
    <div class="row">
        <HeroIcon :hero_name="hero_name" width="128" height="128"></HeroIcon>
   </div>
</template>

<script>

import HeroIcon from '@/components/hero_icon.vue';



export default {
    name: "KopMatchHistory",
    components: {
        HeroIcon
    },


    data () {
        return {
            hero_name: this.$route.params.name
        }
    },


    methods: {
      
    }
     
}


</script>

<style scoped>

</style>
