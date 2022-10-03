<template>
    <div>
        <div class="img-container text-center floating">
            <p class="text-center text-header floating" >KOPBuff</p>
            <img src="../assets/logo.png" alt="KOPBuff Logo" class="logo " width="140" height="200">
        </div>


        
        <div class="input-group form-floating">
            <input type="text" class="form-control" aria-label="Text input with dropdown button" placeholder="Search by username or match id" @keyup.enter="onSearch" ref="inputText">
            <label style="color: white; z-index: 999" for="floatingTextarea">Search by username or match id</label>
            <button class="btn btn-primary br-2" type="button" id="button-addon2" @click.self="onSearch">Search</button>
        </div>
    </div>
</template>

<script>
import navbar from '../components/navbar.vue';
// import match_history_methods from '@/match_history_methods';
import api_communication from '@/api_communication';
export default {
    name: "KopNavbar",
    components: {
    },

    props:{
        navbar
    },

    data () {
        return {
            // match_history_methods,
            api_communication
        }
    },

    mounted() {
       
    },

    methods: {
        onSearch() {
            const is_numbers = /^\d+$/.test(this.$refs.inputText.value);
            if (is_numbers) {
                this.$router.push({ name: 'Match', params: { id: this.$refs.inputText.value } })
            } else {
                this.$router.push({ name: 'Player', params: { name: this.$refs.inputText.value } })
            }
        }
    }
}
</script>

<style scoped>
 
@keyframes floating {
    0% { transform: translate(0,  0px); }
    50%  { transform: translate(0, 5px); }
    100%   { transform: translate(0, -0px); }   
}

.img-container {
    margin-bottom: 80px;
    animation: floating 3s ease-in-out infinite;

}

img {
    width: 150px;
    filter: drop-shadow(0px 4px 60px #286f8b);
    transition: all 3s ease;
}


.text-header {
    font-size: 75px;
    src: url('./../assets/fonts/pixel.ttf');
    font-family: "Glasstown NBP";
    filter: drop-shadow(0px 40px 60px #286f8b);
    transition: all 3s ease;
}


input {
    background-color: hsl(197, 89%, 7%);
    border: none;
    color: white;
    border: 1px solid hsla(197, 37%, 24%, 0.5) !important
}

input::placeholder {
    color: rgb(150, 150, 150);
}


input:focus {
    background-color: hsl(197, 89%, 7%);
    border: none;
    outline: none;
    box-shadow: none;
    color: rgb(217, 217, 217);
    border: 1px solid hsl(197, 37%, 24%) !important
}

button {
    background-color: rgb(38, 70, 83); 
    outline: none;
    border: none;
}

</style>