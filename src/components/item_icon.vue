<template>
    <img src=""  :width="width || 32" :height="height || 32" ref="itemImg">
</template>

<script>

import api_communication from '@/api_communication'

export default {
    name: "KopItemIcon",

    props:{
        item_name: String,
        width: String,
        height: String,
    },

    data () {
        return {
            api_communication,
        }
    },

    mounted () {
        if (this.item_name && this.item_name !== "undefined"){
            console.log(this.item_name, typeof this.item_name)
            this.$refs.itemImg.src = this.api_communication.getItemAssetURL(this.item_name)
        }
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
