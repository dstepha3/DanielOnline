<template lang="html">
    
    <NavBar></NavBar>

    <div id="body">
        <!-- CTA -->
        <div class="row cta" style="margin-top: 4% !important; margin-bottom: 4% !important">
            <h3>Welcome to the main Plant Landing</h3>
            <p>I know there isn't much here right now... I'm working on it.</p>
            <p>For now, you can enjoy my plants below</p>
            <router-link to="/plants/my-plants" class="cta-btn">
                View my Plants
            </router-link>
        </div>

    </div>

    <FooterLarge></FooterLarge>

</template>

<script lang="js">
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";

export default {
    name: 'Plants',
    components: {
        NavBar,
        FooterLarge,
    },
}

</script>