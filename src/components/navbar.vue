<template>
    <div>
        <nav class="navbar navbar-expand-lg mb-3 px-4">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse pr-4" id="navbarNav">
            <ul class="navbar-nav me-auto">

              <li class="nav-item active">
                <slot name="Home"></slot>
              </li>

              <li class="nav-item">
                <slot name="Matches"></slot>
              </li>

              <li class="nav-item">
                <slot name="Heros"></slot>
              </li>

              <li class="nav-item">
                <slot class="nav-link" name="Items"></slot>
              </li>


              <li class="nav-item">
                <slot name="Leaderboard"></slot>
              </li>

            </ul>
            <ul class="navbar-nav navbar-dark ms-auto">
              <li class="nav-item">
                <a class="nav-link" href="https://discord.gg/U3TT62TjZB" target="_blank">Discord</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="https://leagueofpixels.eu/?ref=KOPBuff" target="_blank">Play Game</a>
              </li>


            </ul>
          </div>
        </nav>
    </div>
</template>

<script>

export default {
    name: "KopNavbar",

    props:{

    },

    methods: {
      
    }
}
</script>


<style scoped>

nav {
  background-color: #021821 !important;
  border: 1px solid rgba(38, 70, 83, 0.3) !important;
}

</style>