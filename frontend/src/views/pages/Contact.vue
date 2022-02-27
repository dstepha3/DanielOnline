<template lang="html">
    <NavBar></NavBar>
    <div id="contact-body" class="fade-in">
        <h1 class="mb-3">Contact Me</h1>
        <p class="mb-5">Fill out the form below and I will be in touch as soon as I can.</p>
            <div class="form-container align-center">
          <form class="contact-form" action="https://public.herotofu.com/v1/94eac200-70b4-11ec-b2d5-af79f33d926c" method="post">
            <div class="mb-4">
                <input type="text" class="form-control" name="Name" id="name" placeholder="John Doe">
            </div>
            <div class="mb-4">
                <input type="email" class="form-control" name="Email" id="email" placeholder="name@example.com">
            </div>
            <div class="mb-5">
                <textarea class="form-control" name="Message" id="message" placeholder="message" rows="7"></textarea>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <input type="reset" class="btn" style="color: var(--theme-white); background: var(--theme-black); width: 150px; border: 1px solid var(--theme-black); border-radius: 5px !important;"/>
              <input type="submit" onclick="document.body.style.cursor='wait'; return true;" value="Send" class="btn" style="color: var(--theme-white); background: var(--theme-primary-dark); width: 150px; border-radius: 5px !important;"/>
            </div>
            </form>
        </div>
    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
// import emailjs from 'emailjs-com';
// import { init } from 'emailjs-com';
// import router from '@/router/index.js';

// init("user_vsho8JdW4BokewL2D4klp");

export default {
    name: 'contact',
    components: {
        NavBar,
        FooterLarge
    }
}

</script>

<style scoped>

  #contact-body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    justify-items: center;
    min-height: 100%;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    margin: 80px 25%;
  }

  #contact-body h1 {
    margin-bottom: 40px;
  }

  #contact-body p {
    color: var(--theme-lightest-gray);
  }

  #contact-body .form-container {
    min-width: 100%;
  }

  #contact-body form .input.form-control {
    background-color: var(--theme-warning-dark);
  }

  .btn{
    opacity: 0.60;
    transition: all 0.3s;
  }
  .btn:hover{
    opacity: 1;
  }

  @media screen and (max-width: 786px){
      #contact-body {
          margin: 80px 10%;
      }
  }
</style>