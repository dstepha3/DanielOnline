
import blogLanding from "@/views/blog/blog.vue";
import articleTemplate from "@/views/blog/articleTemplate.vue";

const blogRoutes = [
    {
      path: '/blog',
      name: 'blog-listing',
      component: blogLanding,
    },
    {
      path: '/blog/article-template',
      name: 'article-template',
      component: articleTemplate,
    }
  ];
  
  export default blogRoutes;