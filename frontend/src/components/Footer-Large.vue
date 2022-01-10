<template lang="html">
    <footer>
        <div class="flex">
            <div class="col">
                <h6>Site</h6>
                <router-link class="nav-link" to="/blog">Blog</router-link>
                <router-link class="nav-link disabled" to="/code">Code</router-link>
                <router-link class="nav-link" to="/contact">Contact</router-link>
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
                    <a  
                       href="https://www.snapchat.com/add/dantchulealbert?share_id=NDU4NTUy&local=en_US">
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
                <p class="copyright">Copyright &copy; 2021 DanielOnline. All Rights Reserved</p>
            </div>
            <div class="col">
                <h6>Resources</h6>
                <router-link class="nav-link" to="/about">About</router-link>
                <router-link class="nav-link" to="/faqs">FAQs</router-link>
                <router-link class="nav-link" to="/contact">Help</router-link>
            </div>
        </div>
    </footer>
</template>

<script>

export default {
    name: "footer_large"
}

</script>

<style scoped>
.flex {
    display: flex;
}

footer h6 {
    color: var(--theme-primary-dark);
    border-bottom: 1px solid var(--theme-black);
    line-height: .9;
    margin-bottom: 15px;
    padding: 0 20px 5px;
}

footer h6.title {
    color: var(--theme-black);
    border-bottom: 1px solid var(--theme-primary-dark);
}

footer {
    background-color: #000000;
    min-height: 250px;
    border-top: 3px solid var(--theme-primary-dark);
    padding: 50px 0 0;
}

footer a.router-link-exact-active{
    color: var(--theme-primary-light) !important;
}

footer .col a:hover {
    color: var(--theme-primary-light) !important;
    font-weight: 500;
}
footer .col a {
    color: var(--theme-primary-dark);
}

footer .col {
    flex-basis: 33%;
    display: flex;
    flex-direction: column;
    align-items: center;
}
footer .col:nth-child(odd) { 
    margin-bottom: 40px;
}

footer .col a.footer-link {
    display: block;
    font-size: 16px;
    text-transform: uppercase;
    margin-bottom: 10px;
    font-family: var(--text);
    text-decoration: none;
    color: var(--theme-primary-dark);
}
footer a.footer-link:hover{
    color: var(--theme-primary-light) !important;
    font-weight: 500;
}
footer .col a.footer-link:visited {
    color: var(--theme-black);
}

footer .social-media {
    margin: 10px;
    justify-content: space-between;
}

footer > div > div:nth-child(2) > div:nth-child(2){
    margin: 25px 0 20px;
}

footer > div > div:nth-child(2) > div:nth-child(2) a{
    margin: 0 30px;
}

footer .social-media a {
    margin: 0 20px;
    color: var(--theme-darkest-gray);
}

.social-media .fa-discord:hover {
    color: #6666ff;
}

.social-media .fa-facebook-square:hover {
    color: #0039e6;
}

.social-media .fa-github-square:hover,
.social-media .fa-linkedin:hover {
    color: var(--theme-black);
} 

.social-media .fa-instagram:hover {
    color: #c44dff;
}

.social-media .fa-soundcloud:hover {
    color: #e68a00;
}

.social-media .fa-snapchat-square:hover{
    color: #ffff00;
}

.social-media .fa-youtube:hover {
    color: var(--theme-primary-light);
}

.social-media .fa-twitter-square:hover{
    color: #00b8e6;
}

footer .social-media .disabled .fab {
    color: var(--theme-darkest-gray);
    cursor: default;
    opacity: 0.25;
}

footer .social-media i {
    font-size: 45px;
}

footer .copyright {
    margin-top: 30px;
    margin-bottom: 10px;
    font-size: 16px !important;
    color: var(--theme-primary-dark);
    opacity: .75;
}

footer .social-media .logo:hover{
    opacity: 1 !important;
}

@media only screen and (max-width:  780px) {
    footer .flex {
        flex-direction: column;
    }
    
    footer .social-media.flex {
        flex-direction: row;
    }
    
    footer .flex > .col:nth-child(1){
        order: 1;
        margin-bottom: 30px;
    }
    footer .flex > .col:nth-child(3){
        order: 2;
        margin-bottom: 70px;
    }
    footer .flex > .col:nth-child(2){
        order: 3;
    }
    footer {
    padding: 50px 0 20px;
}
}

@media only screen and (max-width:  500px) {
    footer .flex > .col:nth-child(2) a{
        margin: 0 15px;
    }
    footer .copyright {
        margin-bottom: 20px;
        padding: 0 16%;
        text-align: center;
    }
}
</style>