<template lang="html">

<LockedComponents />

<NavBar></NavBar>

<div v-if="$store.state.adminAuthPassed">
    <div id="code-body" class="fade-in">
        <h1 class="mb-3">Code</h1>
        <p class="center">Here you can find project's I've previously worked on.
        </p>
        <p class="center">Find something you're interested in or would like propose a project?<br/><router-link class="link" to="contact">Contact me</router-link> and I will get back to you as quickly as I can.</p>
    
    <div class="project-container">
        <a class="project" href="https://webdev-stark.cs.kent.edu/~dstepha3/Assignment4/assign4-home.html" target="_blank">
            <img src="https://webdev-stark.cs.kent.edu/~dstepha3/Assignment4/images/banner/presents-153926.png" style="object-position: center -30px;">
            <span class="project-title">RYUG!</span>
        </a>
        <a class="project" href="https://danielonline-ecom.pages.dev/" target="_blank">
            <img src="@/assets/images/eComm-img.png" style="object-position: center -17px;">
            <span class="project-title">eCommerce Example</span>
        </a>
        <a class="project" href="https://troyersdutchmarket.pages.dev/" target="_blank">
            <img src="@/assets/images/troyers-logo.png">
            <span class="project-title">Troyer's Dutch Market</span>
        </a>
        <a class="project" href="https://www.outerboxdesign.com/company/about-us" target="_blank">
            <img src="https://www.outerboxdesign.com/frontend/img/outerbox.jpg" style="object-position: center -48px;">
            <span class="project-title">OuterBox Solutions</span>
        </a>


    </div>
    
    </div>
        
    <FooterLarge style="margin-top: 60px"></FooterLarge>
    <ScrollTopArrow />
</div>
</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import LockedComponents from "@/components/Locked-Page.vue";
import ScrollTopArrow from "@/components/Scroll-To-Top-Arrow/ScrollTopArrow.vue";

export default {
    name: 'Code',
    components: {
        NavBar,
        FooterLarge,
        LockedComponents,
        ScrollTopArrow
    }
}

</script>

<style scoped>
  #code-body {
    text-align: center;
    padding: 80px 15% 0;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    position: relative;
  }
  p{
    color: var(--theme-lightest-gray);
  }
  .project-container{
      border-top: 1px solid var(--theme-primary-dark);
      margin-top: 60px;
      padding-top: 60px;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
  }
  .project{
      cursor: pointer;
      text-decoration: none;
      flex-basis: 46%;
      margin-bottom: 60px;
  }
  .project img{
      height: 169px;
      object-fit: cover;
      width: 100%;
      margin-bottom: 15px;
      opacity: 0.6;
      transition: 0.3s all;
  }
  .project-title{
    font-family: var(--title);
    margin: 0 0 10px;
    font-size: 38px !important;
    color: var(--theme-primary-dark);
    transition: all 0.3s;
  }
  .project:hover .project-title{
      color: var(--theme-primary-light);
  }
  .project:hover img{
      opacity: 1;
  }

  @media screen and (max-width: 768px){
      #code-body {
          padding: 80px 5%;
      }
      h1{
          line-height: 0.9 !important;
      }
      .projects-container{
          flex-direction: column;
      }
  }
</style>