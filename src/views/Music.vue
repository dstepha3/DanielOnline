<template lang="html">
    <NavBar></NavBar>
    <div id="music-body">
        <album_row></album_row>
        <h1 style="margin-bottom: 80px; padding: 0 40px 10px; border-bottom: 1px solid var(--theme-primary-dark);">Hear the Latest</h1>
        <div class="soundcloud-player">
            <sc_player1></sc_player1>
        </div>
        <MusicPromo></MusicPromo>
    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">
import sc_player1 from "@/components/Soundcloud-Player.vue";
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import album_row from "@/components/AlbumRow.vue";
import MusicPromo from "@/components/Music-Promo.vue";

export default {
    name: 'music',
    components: {
        sc_player1,
        album_row,
        NavBar,
        FooterLarge,
        MusicPromo
    }
}

</script>

<style scoped>
  #music-body {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
  }
</style>