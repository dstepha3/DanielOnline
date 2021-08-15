<template lang="html">
    <NavBar></NavBar>
    <div id="music-body">
        <h1 style="margin-bottom: 80px; padding: 0 40px 10px; border-bottom: 1px solid var(--theme-primary-dark);">Hear the Latest</h1>
        <div class="soundcloud-player">
            <sc_player1></sc_player1>
        </div>
    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">
import sc_player1 from "@/components/Soundcloud-Player.vue";
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";

export default {
    name: 'music',
    components: {
        sc_player1,
        NavBar,
        FooterLarge
    }
}

</script>