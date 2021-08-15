<template lang="html">
    <NavBar></NavBar>
    <div id="contact-body">
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
            <input type="submit" value="Send" class="btn" style="color: #000000; background: var(--theme-primary-dark)"/>
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
            
                router.push({name: "ContactThankYou"});
            
        }, (error) => {
            console.log('FAILED...', error);
        });
    }
  }
}

</script>