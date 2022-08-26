<template>
    <div>
        <table class="table table-dark table-hover">
            <thead>
                <tr>
                    <th scope="col"></th>
                    <th scope="col">Item</th>
                    <th scope="col">Times Used</th>
                    <!-- <th scope="col">Use Rate</th>
                    <th scope="col">Win Rate</th> -->
                </tr>
            </thead>

            <tbody>
                <tr v-for="(item_used_amount, item_name) in used_items" :key="item_name">
                    <td><ItemIcon :item_name="item_name" width="32" height="32"></ItemIcon></td>
                    <td>{{item_name}}</td>
                    <td>{{item_used_amount}}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>

import ItemIcon from '@/components/item_icon.vue';
import utils from "@/utils";
import match_history from "./../assets/pretty_match_history.json";

export default {
    name: "KopItemsPage",
    components: {
        ItemIcon
    },
    

    data() {
        return {
            match_history: match_history,
            utils: utils,
            used_items: [],
        }
    },
        
    methods: {

    },

    mounted() {
        this.used_items = this.utils.get_items_used_amount(this.match_history);
        console.log(this.used_items);
    }
    
}
</script>

<style scoped>

</style>