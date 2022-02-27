<template lang="html">

<LockedComponents />

<NavBar></NavBar>


<div v-if="$store.state.adminAuthPassed">
    <div id="code-body" class="fade-in">
        <h1 class="mb-3">Code</h1>
        <p class="center">Finding yourself on this page must mean you're looking for answers and lucky, I've got you.<br/>I've summarized a couple questions I've been frequently asked and I'm here to address them. </p>
        <p class="center">Not able to find what you're looking for? <router-link class="link" to="contact">Contact me</router-link> and I'll try to get back to you as quickly as I can.</p>
    </div>
        
    <FooterLarge style="margin-top: 120px"></FooterLarge>
</div>
</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import LockedComponents from "@/components/Locked-Page.vue";

export default {
    name: 'Code',
    components: {
        NavBar,
        FooterLarge,
        LockedComponents
    }
}

</script>

<style scoped>
  #code-body {
    text-align: center;
    padding: 80px 15%;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    position: relative;
  }
  p{
    color: var(--theme-lightest-gray);
  }

  @media screen and (max-width: 768px){
      #body{
          text-align: center;
          padding-top: 120px;
      }
      h1{
          line-height: 0.9 !important;
      }
      .coming-soon{
          font-size: 16px;
      }
      img{
          opacity: 0.6;
      }
  }
</style>