<template lang="html">
    <NavBar></NavBar>
    <div id="body" style="text-align: center; padding: 0 30px" class="fade-in">
        <h1>Thank You for Reaching Out!
        </h1>
        <span class="coming-soon">I'll get back to you as soon as I can.</span>
    </div>

</template>

<script lang="js">
import NavBar from "@/components/NavBar.vue";

export default {
    name: 'ContactThankYou',
    components: {
        NavBar
    }
}

</script>