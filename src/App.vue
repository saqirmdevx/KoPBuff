<template>
  <div class="background-image"></div>
  <div class="container">
    <TopStatsBar></TopStatsBar>
    <navbar>

    <template #Home>
        <router-link class="nav-link" to="/">Home</router-link>
      </template>
     
     <template #Matches>
          <router-link class="nav-link" to="/matches">Matches</router-link>
      </template>

      <template #Heros>
          <router-link class="nav-link" to="/heros">Heros</router-link>
      </template>

      <template #Items>
          <router-link class="nav-link" to="/items">Items</router-link>
      </template>

      <template #Leaderboard>
        <router-link class="nav-link" to="/leaderboard">Leaderboard</router-link>
      </template>

    </navbar>
    <router-view></router-view>
  </div>


</template>


<script>
import navbar from './components/navbar.vue';
import TopStatsBar from './components/top_stats_bar.vue';
import "bootstrap/dist/css/bootstrap.min.css";
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'



export default {
  name: 'App',
  components: {
    navbar,
    TopStatsBar
  },

}
</script>


<style>

@font-face {
    src: url('./assets/fonts/pixel.ttf');
    font-family: "Glasstown NBP";
}

.background-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  background-image: url('./assets/background.png');
  background-size: cover;
  filter: hue-rotate(40deg) brightness(20%) 
  /* Add backlight effect */
  

}

.router-link-active {
  color: white !important;
}


a {
  color: #D9D9D9 !important;
  text-decoration: none !important;
}

a:hover {
  color: white !important;
  filter: brightness(0.9);
}

p, span {
  color: #D9D9D9 !important;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: rgb(1, 15, 20); 
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: rgb(2, 24, 33)
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: rgb(3, 31, 43)
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}
</style>
