<template lang="html">
    <div id="music-body">
        <h1 style="margin-bottom: 80px; padding: 0 40px 10px; border-bottom: 1px solid var(--theme-primary-dark);">Hear the Latest</h1>
        <div style="width: 50%">
            <sc_player1></sc_player1>
        </div>
    </div>
</template>

<script lang="js">
import sc_player1 from "@/components/Soundcloud-Player.vue";

export default {
    name: 'music',
    components: {
        sc_player1
    }
}

</script>