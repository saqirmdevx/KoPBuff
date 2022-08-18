<template>
  <div class="container">
    <navbar>
      <template #Meta>
        <router-link to="/">Meta</router-link>
      </template>
      
      <template #Winning>
        <router-link to="/winning">Winning</router-link>
      </template>

      <template #Matches>
        <router-link to="/matches">Matches</router-link>
      </template>
    </navbar>
    <router-view></router-view>
  </div>


</template>


<script>
import navbar from './components/navbar.vue';
import "bootstrap/dist/css/bootstrap.min.css";
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'

export default {
  name: 'App',
  components: {
    navbar,
  },

}
</script>


<style>
html, body{
  background-color: rgb(40,40,40) !important
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
