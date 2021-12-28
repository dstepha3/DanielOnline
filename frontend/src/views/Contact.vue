<template lang="html">
    <NavBar></NavBar>
    <div id="contact-body" class="fade-in">
        <h1 class="mb-3">Contact Me</h1>
        <p class="mb-5">Fill out the form below and I will be in touch as soon as I can.</p>
            <div class="form-container align-center">
          <form class="contact-form" @submit.prevent="sendEmail">
            <div class="mb-4">
                <input type="text" class="form-control" name="users-name" placeholder="John Doe">
            </div>
            <div class="mb-4">
                <input type="email" class="form-control" name="users-email" placeholder="name@example.com">
            </div>
            <div class="mb-5">
                <textarea class="form-control" name="users-message" placeholder="message" rows="5"></textarea>
            </div>
            <div style="display: flex; justify-content: space-between;">
              <input type="reset" class="btn" style="color: var(--theme-white); background: var(--theme-black); width: 150px;"/>
              <input type="submit" onclick="document.body.style.cursor='wait'; return true;" value="Send" class="btn" style="color: var(--theme-white); background: var(--theme-primary-dark); width: 150px;"/>
            </div>
            </form>
        </div>
    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import emailjs from 'emailjs-com';
import { init } from 'emailjs-com';
import router from '@/router/index.js';

init("user_vsho8JdW4BokewL2D4klp");

export default {
    name: 'contact',
    components: {
        NavBar,
        FooterLarge
    },
    methods: {
    sendEmail: (e) => {
      emailjs.sendForm('dstephan316', 'template_contact_donline', e.target, 'user_vsho8JdW4BokewL2D4klp')
        .then((result) => {
            console.log('SUCCESS!', result.status, result.text);
            document.body.style.cursor='default';
            router.push({name: "ContactThankYou"});
        }, (error) => {
            document.body.style.cursor='default';
            console.log('FAILED...', error);
        });
    }
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

  @media screen and (max-width: 786px){
      #contact-body {
          margin: 80px 10%;
      }
  }
</style>