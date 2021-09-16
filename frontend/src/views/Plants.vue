<template lang="html">
    
    <NavBar></NavBar>

    <div id="body" class="fade-in">

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

    <div class="img-container">
        <img class="image" src="https://i.imgur.com/aCRP3jj.jpg">
        <div class="overlay"></div>
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

<style scoped>
.image{
    width: 100%;
    position: relative;
}
.overlay{
    background: linear-gradient(180deg, rgba(13,13,13,1) 1%, rgba(255,255,255,0) 100%);     
    position: absolute;
    top: 0;
    content: '';
    z-index: 99;
    height: 400px;
    width: 100%;
}
.img-container{
    position: relative;
    margin-top: 60px;
}
</style>