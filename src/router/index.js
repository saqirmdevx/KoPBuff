import {createRouter, createWebHistory} from 'vue-router'
import index from '../views/index.vue'
import match from '../views/match.vue'
import matches from '../views/matches.vue'
import player from '../views/player.vue'
import hero from '../views/hero.vue'
import leaderboard from '../views/leaderboard.vue'

import heros from '../views/heros.vue'
import items from '../views/items.vue'


const routes = [
    {
        path: '/',
        name: 'Home',
        component: index
    },

    {
        path: '/matches',
        name: 'matches',
        component: matches
    },

    {
        path: '/heros',
        name: 'Heros',
        component: heros
    },

    {
        path: '/items',
        name: 'Items',
        component: items
    },



    {
        path: '/leaderboard',
        name: 'Leaderboard',
        component: leaderboard
    },

    {
        path: '/match/:id',
        name: 'Match',
        component: match
    },
    {
        path: '/player/:name',
        name: 'Player',
        component: player
    },
    {
        path: '/hero/:name',
        name: 'Hero',
        component: hero
    },


]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

export default router