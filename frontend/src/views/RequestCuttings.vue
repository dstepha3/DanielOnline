<template lang="html">
    <div id="body" class="fade-in">
        <h1>I'm sorry, we are not able to accept cutting requests at this time.</h1>
        <span class="coming-soon">
            <div class="align-center">
            <router-link to="/plants">Plants Home</router-link>
            </div>
            <div class="align-center">
            <router-link to="/plants/my-plants">My Plants</router-link>
            </div>
        </span>
        

    </div>
</template>

<script lang="js">

export default {
    name: 'requestCuttings'
}

</script>