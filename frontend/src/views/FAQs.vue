<template lang="html">
    <NavBar></NavBar>
    <div id="faq-body" class="fade-in">
        <h1 class="mb-3">Frequently Asked Questions</h1>
        <p class="center">Finding yourself on this page must mean you're looking for answers and lucky, I've got you.<br/>I've summarized a couple questions I've been frequently asked and I'm here to address them. </p>
        <p class="center">Not able to find what you're looking for? <router-link class="link" to="contact">Contact me</router-link> and I'll try to get back to you as quickly as I can.</p>

        <div class="faq-container">

          <div class="faq">
            <h3>FAQ Question</h3>
            <p>Details with words here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In iaculis ipsum a erat rutrum tincidunt. Donec id suscipit felis. Integer eu ultricies urna. In hac habitasse platea dictumst. Etiam eu quam neque. Mauris consequat nunc maximus tortor venenatis, vel aliquet sapien iaculis. Ut aliquam elementum quam, vel dignissim metus. Donec in aliquet orci. Proin gravida sollicitudin nisl non vestibulum. </p>
          </div>

          <div class="faq">
            <h3>FAQ Question</h3>
            <p>Details with words here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In iaculis ipsum a erat rutrum tincidunt. Donec id suscipit felis. Integer eu ultricies urna. In hac habitasse platea dictumst. Etiam eu quam neque. Mauris consequat nunc maximus tortor venenatis, vel aliquet sapien iaculis. Ut aliquam elementum quam, vel dignissim metus. Donec in aliquet orci. Proin gravida sollicitudin nisl non vestibulum. </p>
          </div>

          <div class="faq">
            <h3>FAQ Question</h3>
            <p>Details with words here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In iaculis ipsum a erat rutrum tincidunt. Donec id suscipit felis. Integer eu ultricies urna. In hac habitasse platea dictumst. Etiam eu quam neque. Mauris consequat nunc maximus tortor venenatis, vel aliquet sapien iaculis. Ut aliquam elementum quam, vel dignissim metus. Donec in aliquet orci. Proin gravida sollicitudin nisl non vestibulum. </p>
          </div>

        </div>
    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";


export default {
    name: 'faq',
    components: {
        NavBar,
        FooterLarge
    }
}

</script>

<style scoped>

  #faq-body {
    display: flex;
    flex-direction: column;
    min-height: 100%;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    margin: 80px 15%;
  }

  #faq-body h1 {
    margin-bottom: 40px;
    text-align: center;
  }

  #faq-body p {
    color: var(--theme-lightest-gray);
  }

  #faq-body p.center {
    text-align: center;
  }
  .faq-container .faq{
    margin: 60px 0;
  }
  .faq h3{
    color: var(--theme-primary-dark);
    border-bottom: 1px solid var(--theme-primary-dark);
    margin-bottom: 20px;
  }

  @media screen and (max-width: 786px){
      #faq-body {
          margin: 80px 10%;
      }
  }
</style>