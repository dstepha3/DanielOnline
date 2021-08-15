<template lang="html">
    <footer>
        <div class="flex">
            <div class="col">
                <h6>Site</h6>
                <router-link class="nav-link disabled" to="/code">Code</router-link>
                <router-link class="nav-link" to="/music">Music</router-link>
                <router-link class="nav-link disabled" to="/plants">Plants</router-link>
                <router-link class="nav-link" to="">&nbsp;</router-link>
            </div>
            <div class="col">
                <h6 class="title">FOLLOW ME ON SOCIAL MEDIA</h6>
                <div class="social-media flex">
                    <a 
                       href="https://discordapp.com/users/Dantchule.Albert#8446/">
                        <i class="fab fa-discord"></i></a>          <!--    discord     -->
                    <a  
                       href="https://www.facebook.com/iDanny330">
                        <i class="fab fa-facebook-square"></i></a>         <!--    facebook    -->
                    <a href="https://github.com/dstepha3">
                        <i class="fab fa-github-square"></i></a>    <!--    github      -->
                    <a  
                       href="https://www.instagram.com/dantchulealbert/">
                        <i class="fab fa-instagram"></i></a>               <!--    instagram   -->
                    <a href="https://www.linkedin.com/in/dstephan316/">
                        <i class="fab fa-linkedin"></i></a>         <!--    linkedin    -->
                </div>
                <div class="social-media flex">
                    <a class="disabled" 
                       href="#">
                        <i class="fab fa-snapchat-square"></i></a>         <!--    snapchat    -->
                    <a href="https://www.soundcloud.com/neonstarbuzz">
                        <i class="fab fa-soundcloud"></i></a>       <!--    soundcloud  -->
                    <a 
                       href="https://twitter.com/dantchulealbert">
                        <i class="fab fa-twitter-square"></i></a>          <!--    twitter     -->
                    <a href="https://www.youtube.com/channel/UCNmg26mkinOe079BFzhbR_g">
                        <i class="fab fa-youtube"></i></a>          <!--    youtube     -->
                </div>
                
                <router-link to="/"><img class="logo" src="@/assets/images/star-logo.png" width="50" style="margin: 30px 0 0; opacity: .5"></router-link>
                <p class="copyright">Copyright &copy; 2021 D.Stephan. All Rights Reserved</p>
            </div>
            <div class="col">
                <h6>Resources</h6>
                <router-link class="nav-link disabled" to="/about">About</router-link>
                <router-link class="nav-link disabled" to="/blog">Blog</router-link>
                <router-link class="nav-link disabled" to="/contact">Contact</router-link>
                <router-link class="nav-link disabled" to="/faqs">FAQs</router-link>
                <router-link class="nav-link disabled" to="/help">Help</router-link>
            </div>
        </div>
    </footer>
</template>

<script>

export default {
    name: "footer_large"
}

</script>