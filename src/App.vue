<template>
  <div class="container">
    <TopStatsBar></TopStatsBar>
    <navbar>
       <template #Home>
        <router-link to="/">Home</router-link>
      </template>

      <template #Meta>
        <router-link to="/meta">Meta</router-link>
      </template>
      
      <template #Winning>
        <router-link to="/winning">Winning</router-link>
      </template>

      <template #Matches>
        <router-link to="/matches">Matches</router-link>
      </template>

      <template #Leaderboard>
        <router-link to="/leaderboard">Leaderboard</router-link>
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

html, body{
  background-color: rgb(40,40,40) !important
}

a {
  color: #D9D9D9 !important;
  text-decoration: none !important;
}

a:hover {
  color: #D9D9D9 !important;
  filter: brightness(0.9);
}

p {
  color: #D9D9D9 !important;
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
