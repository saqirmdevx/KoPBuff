<template>
    <div class="mb-5 statsbar">
        <div class="box top">
            <p class="fw-bold text-center">24H Statistics</p>
        </div>
        <div class="row mt-4">
            <div class="col-sm">
                <p class="text-center">Games played: 10</p>
            </div>

            <div class="col-sm">
                <p class="text-center mr-2">Most played hero: Sparrow</p>
            </div>
            
            <div class="col-sm">
                <p class="text-center mr-2">Most banned hero: Hazel</p>
            </div>

            <div class="col-sm">
                <p class="text-center mr-2">Kills: 82</p>
            </div>
        </div>
        <div class="box bottom">
            <p class="bottom-text text-center text-warning text-nowrap" style="overflow: hidden;">MVP: Pokeplaya</p>
        </div>
    </div>

</template>

<script>

export default {
    name: "KopTopStatsBar",

    props:{

    },

    methods: {
      
    }
}
</script>


<style scoped>
.statsbar {
  background-color: #021821  !important;
  border: 1px solid #264653 !important;
  width: 100%;
  height: 70px;
}

p {
    color: #D9D9D9;
}

.box {
    position: absolute;
    margin: 0 auto;
    width: 10%;
    height: 20px;
    background-color: #021821 !important;
    
}

.top {
    top: 41px;
    left: 45%;
    border-color: #264653;
    border-width: 1px;
    border-style: solid;
    border-bottom: none;
    border-top: 1px solid #264653;
}

.bottom {
    top: 128px;
    border-color: #264653;
    border-width: 1px;
    border-style: solid;
    border-top: none;
    border-bottom: 1px solid #264653;
    left: 45%;
}

.bottom-text {
    position: relative;
    bottom: 5px;
}

</style>