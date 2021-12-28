<template lang="html">
    <NavBar></NavBar>
    <div id="faq-body" class="fade-in">
        <h1 class="mb-3">Blog</h1>
        <p class="center">Finding yourself on this page must mean you're looking for answers and lucky, I've got you.<br/>I've summarized a couple questions I've been frequently asked and I'm here to address them. </p>
        <p class="center">Not able to find what you're looking for? <router-link class="link" to="contact">Contact me</router-link> and I'll try to get back to you as quickly as I can.</p>

        <a class="featured-post" v-for="post in featuredPost" :key="post">
            <div class="featured-image-container">
                <img src="https://dummyimage.com/600x400/3b0909/fff">
            </div>
            <div class="featured-content">
                <h2 class="featured-title"> {{ post.title }} </h2>
                <div class="tag-container">
                    <p class="tag" v-for="tags in post.tags" :key="tags"> 
                        {{ tags }}
                    </p>
                </div>
                <p> {{ post.excerpt }} </p>
            </div>
        </a>

        <div class="flex">
            <a class="article" v-for="post in allPosts" :key="post">
                <img src="https://dummyimage.com/350x250/3b0909/fff">
                <div class="article-inner">
                    <h3> {{ post.title }} </h3>
                    <div class="tag-container">
                        <p class="tag" v-for="tags in post.tags" :key="tags" > 
                            {{ tags }}
                        </p>
                    </div>
                    <p> {{ post.excerpt }} </p>
                </div>
            </a>
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
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                },
                {
                    'title': 'Title of Oldest Article',
                    'slug': 'page-slug', 
                    'featured_img': ' "/" ',
                    'tags': [ 'getting started', 'new shit', 'cheese' ],
                    'excerpt': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
                }
            ],
        };
    },
    mounted(){
        console.log(this.allPosts);
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
    margin: 80px 10%;
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

  @media screen and (max-width: 786px){
      #faq-body {
          margin: 80px 10%;
      }
  }
</style>