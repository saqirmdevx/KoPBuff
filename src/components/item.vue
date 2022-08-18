<template>
   <table class="table table-dark table-hover">
    <thead>

        <tr>
            <th scope="col">Hero</th>
            <th scope="col">Player</th>
            <th scope="col">K</th>
            <th scope="col">D</th>
            <th scope="col">A</th>
            <th scope="col">Damage</th>
            <th scope="col">Tower Damage</th>
            <th scope="col">Healing</th>
            <th scope="col">Net</th>
            <th scope="col">Items</th>
            <th scope="col">Talents</th>
        </tr>
    </thead>
        <tbody ref="tablebody">
        
        </tbody>
    </table>
</template>

<script>

export default {
    name: "KopMatchHistory",

    props:{
        gameId: String,
        gamemode: String,
        winningTeam: String,
        gameDuration: String,
        gameHerosBlue: Array,
        gameHerosRed: Array,
    },

    methods: {
        addPlayer(hero, player, kills, deaths, assists, damage, towerDamage, healing, networth, items, talents) {
            
        },
    }
     
}


</script>

<style scoped>
</style>
