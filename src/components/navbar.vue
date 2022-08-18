<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-3">
          <a class="navbar-brand" href="#">KOPBuff</a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav navbar-dark">
              <li class="nav-item active">
                <a class="nav-link" href="#"><slot name="Meta"></slot></a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="#"><slot name="Winning"></slot></a>
              </li>

              <li class="nav-item">
                <a class="nav-link" href="#"><slot name="Matches"></slot></a>
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
  background-color: #3a3a3a !important
}
</style>