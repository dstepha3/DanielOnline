import { createWebHistory, createRouter} from "vue-router";

import Home from "@/views/Home.vue";
import AdminDashboard from "@/views/Admin.vue";

import About from "@/views/pages/About.vue";
import Contact from "@/views/pages/Contact.vue";
import FAQs from "@/views/pages/FAQs.vue";
import ContactThankYou from "@/views/pages/ContactThankYou.vue";
import NotFound from "@/views/errors/NotFound-404.vue";

import ping from '@/views/ping.vue';

import blogRoutes from '@/router/blog.js';
import gameRoutes from '@/router/game.js';

const baseRoutes = [
    {
        path: "/",
        name: "Home",
        component: Home,
        meta: {
            title: 'Home - Daniel Online!'
        }
    },
    {
        path: "/about",
        name: "About",
        component: About,
        meta: {
            title: 'About - Daniel Online!'
        }
    },
    {
        path: "/admin",
        name: "AdminDashboard",
        component: AdminDashboard,
        meta: {
            title: 'Admin Dashboard - Daniel Online!'
        }
    },
    {
        path: "/contact",
        name: "Contact",
        component: Contact,
        meta: {
            title: 'Contact - Daniel Online!'
        }
    },
    {
        path: "/faqs",
        name: "Faq",
        component: FAQs,
        meta: {
            title: 'FAQs - Daniel Online!'
        }
    },
    {
        path: "/contact/thank-you",
        name: "ContactThankYou",
        component: ContactThankYou,
        meta: {
            title: 'Thanks - Daniel Online!'
        }
    },
    { 
        path: '/:pathMatch(.*)*', 
        name: 'not-found', 
        component: NotFound,
        meta: {
            title: '404 | PAGE NOT FOUND - Daniel Online!'
        }
    },
    {
        path: "/ping",
        name: "Ping",
        component: ping,
        meta: {
            title: 'Ping!'
        }
    },
];

const routes = baseRoutes.concat(blogRoutes).concat(gameRoutes);

const router = createRouter ({
    history: createWebHistory(),
    routes,
    // eslint-disable-next-line no-unused-vars
    scrollBehavior (to, from, savedPosition) {
        if (savedPosition) {
        return savedPosition
        } else {
            return { x: 0, y: 0 }
        }
        },
  
      
          
});

/***************************************************************************/
// Metadata Update Block
// This callback runs before every route change, including on page load.
// Updates page Metadata using info from @/router/index.js
router.beforeEach((to, from, next) => {
    
    // Timeout Function to Scroll To Top of window when Router View changes
    setTimeout(function () {window.scrollTo(0, 0);}, 2);

    const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);
  
    const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  
    const previousNearestWithMeta = from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  
    if(nearestWithTitle) {
      document.title = nearestWithTitle.meta.title;
    } else if(previousNearestWithMeta) {
      document.title = previousNearestWithMeta.meta.title;
    }
  
    Array.from(document.querySelectorAll('[data-vue-router-controlled]')).map(el => el.parentNode.removeChild(el));
  
    if(!nearestWithMeta) return next();
  
    nearestWithMeta.meta.metaTags.map(tagDef => {
      const tag = document.createElement('meta');
  
      Object.keys(tagDef).forEach(key => {
        tag.setAttribute(key, tagDef[key]);
      });
        tag.setAttribute('data-vue-router-controlled', '');
      return tag;
    })
    .forEach(tag => document.head.appendChild(tag));
  
    next();
  });

// End of Metadata Update Block
/*******************************************************************/


export default router;