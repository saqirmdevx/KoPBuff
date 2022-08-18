<template>
    <div>
        <div class="mt-5 mb-5 text-center">
            <img src="../assets/logo.png" alt="KOPBuff Logo" class="logo " width="140" height="200">
        </div>
        <div class="input-group">
            <input type="text" class="form-control" aria-label="Text input with dropdown button" placeholder="Search by username or match id" ref="inputText">
            <button class="btn btn-primary br-2" type="button" id="button-addon2" @click="onSearch">Search</button>

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
