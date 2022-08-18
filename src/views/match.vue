<template>
    <h1 style="color: rgba(100,100,255)">Blue team</h1>
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

        <tbody ref="blueTeamTbody">
            <tr v-for="(player, player_name) in match.blue_team" :key="player_name">
                <td><HeroIcon :hero_name="player.hero" width="48" height="48"></HeroIcon></td>
                <td>{{player_name}}</td>
                <td>{{player.kills}}</td>
                <td>{{player.deaths}}</td>
                <td>{{player.assists}}</td>
                <td>{{player.total_damage}}</td>
                <td>{{player.tower_damage}}</td>
                <td>{{player.total_healing}}</td>
                <td>{{player.total_net}}</td>
                <td>{{player.items}}</td>
                <td>{{player.talents}}</td>
            </tr>
        </tbody>
    </table>

    <h1 style="color: rgba(255,100,100)">Red team</h1>
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
        <tbody ref="redTeamTbody">
            <tr v-for="(player, player_name) in match.red_team" :key="player_name">
                <td><HeroIcon :hero_name="player.hero" width="48" height="48"></HeroIcon></td>
                <td>{{player_name}}</td>
                <td>{{player.kills}}</td>
                <td>{{player.deaths}}</td>
                <td>{{player.assists}}</td>
                <td>{{player.total_damage}}</td>
                <td>{{player.tower_damage}}</td>
                <td>{{player.total_healing}}</td>
                <td>{{player.total_net}}</td>
                <td>{{player.items}}</td>
                <td>{{player.talents}}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>

import match_history_methods from "@/match_history_methods";
import match_history from "./../assets/pretty_match_history.json";
import HeroIcon from "@/components/hero_icon.vue";

export default {
    name: "KopMatchHistory",
    components: {
        HeroIcon
    },

    data() {
        return {
            match: match_history_methods.get_games_by(match_history, (game) => game.game_id == this.gameId)[0],
        }
    },
}


</script>

<style scoped>
</style>
