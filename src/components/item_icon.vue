<template>
    <img src="" :width="width || 32" :height="height || 32" ref="hero-img">
</template>

<script>

import item_names_to_png_names from "./../assets/item_names_to_png_names.json";

export default {
    name: "KopItemIcon",

    props:{
        item_name: String,
        width: Number,
        height: Number,
    },

    mounted () {
        if (this.item_name == "empty"){
            this.$refs["hero-img"].src = require(`@/assets/itemUsed/empty.png`)
            return
        }

        this.$refs["hero-img"].src = require(`@/assets/itemUsed/${item_names_to_png_names[this.item_name]}`)
    },

    methods: {
      
    }
     
}

</script>

<style scoped>
img {
    display: inline-block;
}
</style>
