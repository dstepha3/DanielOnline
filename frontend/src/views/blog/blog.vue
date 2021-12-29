<template lang="html">
    <NavBar></NavBar>
    <div id="bloglanding-body" class="fade-in">
        <h1 class="mb-3">Blog</h1>
        <p class="center">Finding yourself on this page must mean you're looking for answers and lucky, I've got you.<br/>I've summarized a couple questions I've been frequently asked and I'm here to address them. </p>
        <p class="center">Not able to find what you're looking for? <router-link class="link" to="contact">Contact me</router-link> and I'll try to get back to you as quickly as I can.</p>

        <a class="featured-post" v-for="post in featuredPost" :key="post">
            <div class="featured-image-container">
                <img src="https://dummyimage.com/1200x800/3b0909/fff">
            </div>
            <div class="featured-content">
                <h2 class="featured-title"> {{ post.title }} </h2>
                <div class="tag-container">
                    <p class="tag" v-for="tags in post.tags" :key="tags"> 
                        {{ tags }}
                    </p>
                </div>
                <p> {{ post.excerpt }} </p>
                <div class="readMore">
                    <p>Read More <span class="carat">></span></p>
                </div>
            </div>
        </a>

        <div class="filter-container">
            <h4>Display By Tag</h4>
            <div class="tag-container" style="margin-top: 10px;">
                <p class="tag" id="all" v-on:click="tagFilterKey = 'all'" :class="{ active: tagFilterKey == 'all' }" >Show All</p>
                <p class="tag" id="gettingStarted" v-on:click="tagFilterKey = 'gettingStarted'" :class="{ active: tagFilterKey == 'getting started' }" >getting Started</p>
                <p class="tag" id="cheese" v-on:click="tagFilterKey = 'cheese'" :class="{ active: tagFilterKey == 'cheese' }" >cheese</p>
                <p class="tag" id="newShit" v-on:click="tagFilterKey = 'newShit'" :class="{ active: tagFilterKey == 'new shit' }" >new shit</p>
            </div>
        </div>

        <div class="flex">
            <a class="article" v-for="post in tagFilter" :key="post">
                <img src="https://dummyimage.com/1200x800/3b0909/fff">
                <div class="article-inner">
                    <h3> {{ post.title }} </h3>
                    <div class="tag-container">
                        <p class="tag" v-for="tags in post.tags" :key="tags" > 
                            {{ tags }}
                        </p>
                    </div>
                    <p> {{ post.excerpt }} </p>
                    <div class="readMore">
                        <p>Read More <span class="carat">></span></p>
                    </div>
                </div>
            </a>
        </div>

        <div class="pagination-container">
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                    <li class="page-item disabled">
                    <a class="page-link" href="#" aria-label="Previous">
                        <span aria-hidden="true">&laquo;</span>
                    </a>
                    </li>
                    <li class="page-item active"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">3</a></li>
                    <li class="page-item">
                    <a class="page-link" href="#" aria-label="Next">
                        <span aria-hidden="true">&raquo;</span>
                    </a>
                    </li>
                </ul>
            </nav>
        </div>

    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">

import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";


export default {
    name: 'blog',
    components: {
        NavBar,
        FooterLarge
    },
    data() {
        return {
            hover: false,
            tagFilterKey: 'all',
            featuredPost: [
                {
                    'title': 'Title of Featured Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                }
            ],
            allPosts: [
                {
                    'title': 'Newer Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [  'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit'],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Oldest Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                }
            ],
        };
    },
    mounted(){
        console.log(this.allPosts);
    },
    computed: {
        tagFilter() {
            return this[this.tagFilterKey]
        },
        all() {
            return this.allPosts;
        },
        gettingStarted() {
            this.resetActiveTags();
            var element = document.getElementById('gettingStarted');
            element.classList.add("active");
            return this.allPosts.filter((allPosts) => allPosts.tags.includes('getting started'));

        },
        cheese() {
            this.resetActiveTags();
            return this.allPosts.filter((allPosts) => allPosts.tags.includes('cheese'))
        },
        newShit() {
            this.resetActiveTags();
            var element = document.getElementById('newShit');
            element.classList.add("active");
            return this.allPosts.filter((allPosts) => allPosts.tags.includes('new shit'))
        
        },
    },
    methods: {
        resetActiveTags(){
            console.log("inside resetActiveTags");
            var element = document.getElementsByClassName('active');
            console.log(element);
            element[0].classList.remove("active");
            console.log(element);
        },
    },
}

</script>

<style scoped>

  #bloglanding-body {
    display: flex;
    flex-direction: column;
    min-height: 100%;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    margin: 80px 10% 20px;
  }

  #bloglanding-body h1 {
    margin-bottom: 40px;
    text-align: center;
  }

  #bloglanding-body p {
    color: var(--theme-lightest-gray);
  }

  #bloglanding-body p.center {
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


  a.featured-post{
      display: flex;
      border: 3px solid var(--theme-primary-dark);
      margin: 40px 0;
      opacity: 0.75;
      transition: all 0.3s;
      text-decoration: none;
      cursor: pointer;
  }
  a.featured-post:hover{
      opacity: 1;
  }
  .featured-image-container{
      flex-basis: 50%;
      height: 100%;
  }
  .featured-image-container img{
      width: 100%;
      height: 350px;
      object-fit: cover;
      object-position: center;
      border-right: 3px solid var(--theme-primary-dark);
  }
  .featured-content{
      flex-basis: 50%;
      padding-left: 40px;
      padding-right: 40px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
   }
  .tag-container{
      margin-bottom: 15px;
  }
  .tag{
      background-color: var(--theme-dark-gray);
      font-size: 12px !important;
      padding: 5px 15px;
      margin-right: 15px;
      margin-bottom: 10px;
      margin-top: 0;
      border-radius: 25px;
      color: black !important;
      font-weight: 900;
      text-transform: uppercase;
      text-align: center;
      display: inline-block;
  }
  .featured-title{
      margin-bottom: 0;
      line-height: 1;
      color: var(--theme-primary-dark);
      cursor: pointer;
  }
  .featured-content p{
      cursor: pointer;
  }
  .flex{
      display: flex;
      flex-wrap: wrap;
  }
  .article{
      flex-basis: 48%;
      border: 2px solid var(--theme-primary-dark);
  }
  .article img{
      display: block;
      width: 100%;
      height: 200px;
      object-fit: cover;
      object-position: center;
      border-bottom: 2px solid var(--theme-primary-dark); 
  }
  .article-inner{
      padding: 40px;
      padding-bottom: 60px;
      position: relative;
  }
  .article > p:last-child{
      margin-bottom: 0;
  }
  .flex > .article:nth-child(odd){
      margin-right: 20px;
      margin-bottom: 40px;
  }
  .flex > .article:nth-child(even){
      margin-left: 20px;
      margin-bottom: 40px;
  }
  a.article{
      text-decoration: none;
      opacity: 0.75;
      transition: all 0.3s;
      cursor: pointer;
  }
  a.article:hover{
      opacity: 1;
  }
  .article h3{
      color: var(--theme-primary-dark);
      line-height: 1;
      cursor: pointer;
  }
  .article p{
      cursor: pointer;
  }
  .readMore{
      position: absolute;
      bottom: 0;
      right: 40px;
      overflow: hidden;
      width: 100%;
      height: 0;
      transition: .5s ease;
      text-align: right;
  }

.featured-post:hover .readMore,
.article:hover .readMore {
  height: 50px;
}

  .readMore p{
      font-family: var(--title);
      color: var(--theme-primary-dark) !important;
      font-size: 22px !important;
      opacity: 0.7;
  }


  .readMore .carat{
      font-family: var(--text);
      vertical-align: bottom;
      margin-left: 10px;
  }
  
  .filter-container{
      margin: 80px 0 30px; 
      border-top: 1px solid var(--theme-primary-dark); 
      padding: 40px; 
      display: flex; 
      flex-direction: column; 
      justify-content: center; 
      align-items: center;
      position: relative;
  }
  .filter-container h4{
      position: absolute;
      background: #0d0d0d;
      top: -23px;
      padding: 0 15px;
  }
  .filter-container .tag{
      opacity: 0.7;
      cursor: pointer;
      transition: all 0.3s;
  }
  .filter-container .tag:hover{
      opacity: 1;
  }
  .filter-container .tag.active{
      opacity: 1;
      background-color: var(--theme-lightest-gray);
  }
  .pagination-container{
      display: flex;
      justify-content: center;
      margin-top: 60px;
  }
  .page-item .page-link {
      background-color: hsl(0, 0%, 3%);
      color: var(--theme-primary-dark);
      border: 1px solid hsl(0, 0%, 3%);
      padding-left: 15px;
      padding-right: 15px;
      opacity: 0.75;
  }
  .page-item.disabled:hover .page-link{
      background-color: hsl(0, 0%, 3%);
      color: var(--theme-primary-dark);
      border: 1px solid hsl(0, 0%, 3%);
      padding-left: 15px;
      padding-right: 15px;
      opacity: 0.75;
  }
  .page-item.active .page-link{
      opacity: 1;
      color: var(--theme-primary-light);
      background-color: hsl(0, 0%, 0%);
  }
  .page-item:hover .page-link{
      opacity: 1;
      color: var(--theme-primary-light);
      background-color: hsl(0, 0%, 0%);
  }

  @media screen and (max-width: 786px){
      #bloglanding-body {
          margin: 80px 10%;
      }
      a.article{
          flex-basis: 100%;
      }
      .flex > .article:nth-child(odd){
      margin-right: 0;
      margin-bottom: 40px;
  }
    .flex > .article:nth-child(even){
        margin-left: 0;
        margin-bottom: 40px;
    }
  }
</style>