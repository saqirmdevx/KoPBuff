import {createRouter, createWebHistory} from 'vue-router'
import index from '../views/index.vue'
import match from '../views/match.vue'
import player from '../views/player.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: index
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
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router