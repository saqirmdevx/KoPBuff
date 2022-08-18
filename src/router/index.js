import {createRouter, createWebHistory} from 'vue-router'
import index from '../views/index.vue'
import match from '../views/match.vue'
import player from '../views/player.vue'
import hero from '../views/hero.vue'
import leaderboard from '../views/leaderboard.vue'
const routes = [
    {
        path: '/',
        name: 'Home',
        component: index
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
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

export default router