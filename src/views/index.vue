<template>
    <div>
        <p class="text-center text-header" >KOPBuff</p>
        <div class="img-container text-center">
            <img src="../assets/logo.png" alt="KOPBuff Logo" class="logo " width="140" height="200">
        </div>
        <div class="input-group">
            <input type="text" class="form-control" aria-label="Text input with dropdown button" placeholder="Search by username or match id" @keyup.enter="onSearch" ref="inputText">
            <button class="btn btn-primary br-2" type="button" id="button-addon2" @click.self="onSearch">Search</button>
        </div>
    </div>
</template>

<script>
// import navbar from '../components/navbar.vue';

export default {
    name: "KopNavbar",
    components: {
        // navbar,
    },
    props:{

    },

    methods: {
        onSearch() {
            const is_numbers = /^\d+$/.test(this.$refs.inputText.value);
            if (is_numbers) {
                this.$router.push({ name: 'Match', params: { id: this.$refs.inputText.value } })
            } else {
                console.log(123)
                this.$router.push({ name: 'Player', params: { name: this.$refs.inputText.value } })
            }
        }
    }
}
</script>

<style scoped>

.img-container {
    margin-bottom: 80px;
}

img {
    /* Make backgroudn glow */
    /* box-shadow: inset 0 0 10px #57A773, 0 0 40px #57A773, 0 0 80px #57A773; */
     width: 150px;
    filter: drop-shadow(0px 4px 60px #57A773);
}

button {
    background-color: #57A773;
    outline: none;
    border: none;
}

.text-header {
    font-size: 75px;
    src: url('./../assets/fonts/pixel.ttf');
    font-family: "Glasstown NBP";
    filter: drop-shadow(0px 40px 60px #57A773);
}

</style>