<template lang="html">

<LockedComponents />

<NavBar></NavBar>

<div v-if="$store.state.adminAuthPassed">
    
    <div id="article-body" class="fade-in">
        <h1>Article Template H1 Title</h1>
        <div class="meta">
            <span>By Daniel Stephan</span> &nbsp;&bullet;&nbsp;
            <span>January 12, 2022</span>
        </div>
        <div class="banner-image">
            <img src="https://wallpaperaccess.com/full/2828905.jpg">
        </div>
        <div class="top-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. Donec lacinia pulvinar sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis.</p>
            <p>Pellentesque cursus eleifend ipsum, et dictum neque tristique ut. Sed sed nunc porttitor justo consequat porta eget a dolor. Suspendisse vulputate laoreet risus, semper auctor est porttitor non. Mauris vel fringilla justo. Donec feugiat, sapien sed euismod consequat, est sem vehicula diam, a rutrum urna ipsum quis quam. Nunc sodales sollicitudin ligula, in volutpat magna malesuada at. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
        </div>
        <div class="jump-section">
            <div class="floating-title">
                <h4>Jump to Section</h4>
            </div>
            <div class="jump-row flex">
                <a class="toc">
                    Title of Section
                    <div class="readMore">
                        <p><i class="fas fa-angle-double-down"></i></p>
                    </div>
                </a>
                <a class="toc">
                    Title of Section
                    <div class="readMore">
                        <p><i class="fas fa-angle-double-down"></i></p>
                    </div>
                </a>
                <a class="toc">
                    Title of Section
                    <div class="readMore">
                        <p><i class="fas fa-angle-double-down"></i></p>
                    </div>
                </a>
            </div>
            <div class="jump-row flex">
                <a class="toc">
                    Title of Section
                    <div class="readMore">
                        <p><i class="fas fa-angle-double-down"></i></p>
                    </div>
                </a>
                <a class="toc">
                    Title of Section, May Span One or More Lines
                    <div class="readMore">
                        <p><i class="fas fa-angle-double-down"></i></p>
                    </div>
                </a>
                <a class="toc">
                    Title of Section
                    <div class="readMore">
                        <p><i class="fas fa-angle-double-down"></i></p>
                    </div>
                </a>
            </div>
        </div>

        <section>
            <h2>Header Title H2</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. <router-link to="/">Donec lacinia pulvinar</router-link> sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis. Pellentesque cursus eleifend ipsum, et dictum neque tristique ut. Sed sed nunc porttitor justo consequat porta eget a dolor. Suspendisse vulputate laoreet risus, semper auctor est porttitor non. Mauris vel fringilla justo. Donec feugiat, sapien sed euismod consequat, est sem vehicula diam, a rutrum urna ipsum quis quam. Nunc sodales sollicitudin ligula, in volutpat magna malesuada at. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
            <h3>Header Title H3</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. Donec lacinia pulvinar sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis.</p>
            <div class="split-list flex">
                <ul>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                </ul>
                <ul>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
                </ul>
            </div>
        </section>

        <div class="banner-image">
            <img src="https://getwallpapers.com/wallpaper/full/0/4/1/349449.jpg">
        </div>
        <section class="align-center">
            <h2>Centered Title Header H2</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. Donec lacinia pulvinar sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis. Pellentesque cursus eleifend ipsum, et dictum neque tristique ut. Sed sed nunc porttitor justo consequat porta eget a dolor.</p>
        </section>

        <section>
            <div class="numberedList">
                <div class="listItem flex">
                    <h4>1</h4>
                    <div class="content">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet.</p>
                    </div>
                </div>
                <div class="listItem flex">
                    <h4>2</h4>
                    <div class="content">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet.</p>
                    </div>
                </div>
                <div class="listItem flex">
                    <h4>3</h4>
                    <div class="content">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet.</p>
                    </div>
                </div>
            </div>
        </section>

        <hr />

        <section>
            <div class="split-section flex">
                <div class="image-container">
                    <img src="https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/SRsQjwFQMjby34s1c/videoblocks-futuristic-red-digital-earth-seamless-loop-global-data-network-around-planet-in-modern-age-worldwide-internet-and-blockchain-technology-connectivity-science-and-business-concept-3d-animation_hhxnqnkjb_thumbnail-1080_01.png">
                </div>
                <div class="content">
                    <h2>Header Title H2</h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet.</p>
                </div>
            </div>
        </section>

        <section style="margin-top: 80px;">
            <h2>Header Title H2</h2>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. <router-link to="/">Donec lacinia pulvinar</router-link> sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis. Pellentesque cursus eleifend ipsum, et dictum neque tristique ut. Sed sed nunc porttitor justo consequat porta eget a dolor. Suspendisse vulputate laoreet risus, semper auctor est porttitor non. Mauris vel fringilla justo. Donec feugiat, sapien sed euismod consequat, est sem vehicula diam, a rutrum urna ipsum quis quam. Nunc sodales sollicitudin ligula, in volutpat magna malesuada at. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.</p>
            <h3>Header Title H3</h3>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. Donec lacinia pulvinar sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis.</p>
        </section>

        <section>
            <div class="cta">
                <h2>Conclusion Header Title H2</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed augue quis risus aliquam semper vel quis lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nunc venenatis felis vitae tellus condimentum, quis tristique nunc laoreet. Fusce faucibus consequat felis at varius. Donec lacinia pulvinar sodales. In bibendum dictum lectus, a ultrices nibh interdum non. Aenean cursus ullamcorper ex vitae mattis. Pellentesque cursus eleifend ipsum, et dictum neque tristique ut. Sed sed nunc porttitor justo consequat porta eget a dolor. </p>
                <div class="button-container">
                    <router-link to="#" class="dark button">Contact</router-link>
                    <router-link to="#" class="red button">Get Help</router-link>
                </div>
            </div>
        </section>


    </div>
    <FooterLarge />
    <ScrollTopArrow />
</div>

</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import LockedComponents from "@/components/Locked-Page.vue"
import ScrollTopArrow from "@/components/Scroll-To-Top-Arrow/ScrollTopArrow.vue";

export default {
    name: 'articleTemplate',
    components: {
        NavBar,
        FooterLarge,
        ScrollTopArrow,
        LockedComponents
    },
}

</script>

<style scoped>

#article-body{
    margin: 80px 15%;
}
.flex{
    display: flex;
}
h1{
    text-align: center;
    color: var(--theme-white);
}
h2, h3{
    color: var(--theme-primary-dark);
    opacity: 0.9;
    margin-bottom: 0;
}
p, ul{
    color: var(--theme-white);
    margin-bottom: 30px;
}
a{
    color: var(--theme-primary-dark);
    padding: 0 5px;
    text-decoration: none;
    transition: all 0.3s;
}
a:hover{
    color: var(--theme-primary-light);
    border-bottom: 0.5px solid var(--theme-primary-light);
}
.meta{
    text-align: center;
    color: var(--theme-light-gray);
}
.banner-image{
    width: 100%;
    height: 250px;
    margin: 30px 0;
}
.banner-image img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: fill;
}
.top-content{
    background-color: rgba(255, 0, 0, 0.25);
    padding: 60px;
}
.top-content p{
    color: var(--theme-white);
}
.top-content > p:last-child{
    margin: 0;
}
.jump-section{
    border: 1px solid rgba(175, 0, 0, 0.2);
    padding: 60px;
    margin: 80px 0;
    position: relative;
}
.jump-row{
    margin-bottom: 30px;
}
.jump-section > .jump-row:last-child{
    margin-bottom: 0;
}

.toc{
    color: var(--theme-light-gray);
    text-decoration: none;
    cursor: pointer;
    
    border: 1px solid rgba(175, 0, 0, 0.4);
    flex-basis: 33%;
    background-color: black;
    height: 140px;
    position: relative;

    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    opacity: 0.8;
    padding: 0 10px 30px;
    text-align: center;
    transition: all 0.3s;
}
.toc:hover{
    color: var(--theme-lightest-gray);
    opacity: 1;
    border: 0.5px solid var(--theme-primary-light);
}
.jump-row > .toc:nth-child(2){
    margin: 0 30px;
}
.readMore{
    position: absolute;
    bottom: 0;
    right: 0;
    overflow: hidden;
    width: 100%;
    height: 0;
    transition: .5s ease;
    text-align: center;
}
.readMore p{
    cursor: pointer !important;
}
.toc:hover .readMore {
  height: 50px;
}
.jump-section .floating-title{
    position: absolute;
    top: -20px;
    display: flex;
    justify-content: center;
    width: 100%;
    margin-left: -60px;
}
.jump-section .floating-title h4{
    color: var(--theme-light-gray);
    background: #0d0d0d;
    padding: 0 50px;
}
section{
    margin: 80px 0;
    padding: 0;
    border: 0;
}
ul > li:last-child{
    margin-bottom: 0;
}
ul{
    list-style: none;
    margin-left: 15px;
}
li{
    position: relative;
    padding-left: 20px;
    margin-bottom: 15px;
}
ul li::before {
  position: absolute;
  content: "\2022"; 
  color: var(--theme-primary-dark);
  font-weight: bold; 
  display: inline-block; 
  width: 1em; 
  top: 0;
  left: -20px;
}
.split-list{
    margin-bottom: 30px;
}

.split-list ul{
    margin-bottom: 0;
}
section > :last-child{
    margin-bottom: 0;
}
hr{
    border-top: 1px solid rgba(175, 0, 0, 0.6);
    opacity: 1;
}
.numberedList{
    margin: 0 13%;
}
.listItem{
    border-bottom: 1px solid rgba(175, 0, 0, 0.6);
    padding-bottom: 50px;
    margin-bottom: 50px;
}
.numberedList > .listItem:last-child{
    margin-bottom: 0;
    border-bottom: none;
}
.listItem h4{
    flex-basis: 5%;
    background: rgba(175, 0, 0, 0.4);
    height: 65px;
    padding: 10px 20px;
    margin: 0;
    display: flex;
    align-items: baseline;
    color: #000000;
    border-radius: 10px;
    margin-top: 6px;
}
.listItem .content{
    flex-basis: 95%;
    margin-left: 60px;
}
.content > p:last-child{
    margin-bottom: 0;
}
.image-container{
    flex-basis: 50%;
    text-align: center;
}
.image-container img{
    width: 100%;
    object-fit: cover;
    object-position: center;
}
.split-section{
    margin: 100px 0;
}
.split-section .content{
    flex-basis: 50%;
    margin-left: 60px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.split-section .content h2{
    line-height: 0.75em;
}
.cta{
    border: 1px solid var(--theme-primary-dark);
    padding: 60px;
    text-align: center;
}
.cta p{
    margin-bottom: 40px;
}
.cta > p:last-child{
    margin-bottom: 0;
}
#article-body > :last-child{
    margin: 100px 0;
}

@media only screen and (max-width: 768px){
    #article-body{
        margin: 80px 5%;
    }
    .flex{
        display: block;
    }
    .top-content{
        padding: 40px;
    }
    p, ul{
        font-size: 15px !important;
    }
    a{
        font-size: 15px !important;
    }
    .jump-section {
        padding:  60px 40px;
    }
    .jump-section .floating-title{
        margin-left: -40px;
    }
    .jump-row > .toc:nth-child(2){
        margin: 30px 0;
    }
    .split-list > ul:first-child{
        margin-bottom: 15px;
    }
    .listItem h4{
        width: 55px;
        margin-bottom: 30px;
    }
    .listItem.flex{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .listItem .content{
        margin-left: 0;
    }
    .split-section .content{
        margin-left: 0;
        margin-top: 30px;
    }
    .cta {
        padding: 30px;
    }
    .button-container > a:last-child{
        margin-top: 15px;
    }

}

</style>