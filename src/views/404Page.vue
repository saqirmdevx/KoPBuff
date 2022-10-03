<template>
    <div class="row">
        <div class="col-4">
            <img src="../assets/bandeira1.gif" width="100" height="500"/>
            <img src="../assets/bandeira1.gif" width="100" height="500"/>
            <img src="../assets/bandeira1.gif" width="100" height="500"/>
        </div>
        <div class="col-4">
            <h1>Path Not Found</h1>
        </div>
        <div class="col-4">
            <img src="../assets/bandeira1.gif" width="100" height="500"/>
            <img src="../assets/bandeira1.gif" width="100" height="500"/>
            <img src="../assets/bandeira1.gif" width="100" height="500"/>
        </div>
    </div>
    
</template>

<script>

export default {
    name: "NotFound",
}


</script>

<style scoped>

h1 {
    text-align: center;
    line-height: 500px;
    color: white;
}


@keyframes hue-rotate {
    from {
        filter: hue-rotate(0deg);
    }
    to {
        filter: hue-rotate(360deg);
    }
}

img {
    animation: hue-rotate 20s ease-in-out infinite;

}
</style>
