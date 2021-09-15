<template lang="html">

<div style="margin-top: 80px; padding-top: 100px; border-top: 1px solid var(--theme-primary-dark);">
    <div class="align-center">
        <img class="promo" src="@/assets/images/music-image1.jpg">
    </div>
</div>

</template>

<script>

export default {
    name: "music-promo"
}

</script>

<style scoped>

  img.promo {
    margin: 80px 0 160px; 
    border: 1px solid var(--theme-primary-light);
    box-shadow: 0px 0px 100px 5px #ffffff;
    animation-duration: 5s;
    animation-name: glow;
    animation-iteration-count: infinite;
    width: 50%;
    background-attachment: fixed;
  }

    @keyframes glow {
    0% {
      box-shadow: 0px 0px 10px 5px #000000;
    }
  
    50%{
      box-shadow: 0px 0px 100px 5px var(--theme-warning-dark);
    }

    100%{
      box-shadow: 0px 0px 10px 5px #000000;
    }
  }

</style>