import { createWebHistory, createRouter} from "vue-router";

import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Contact from "@/views/Contact.vue";
import Code from "@/views/Code.vue";
import Plants from "@/views/Plants.vue";
import Music from "@/views/Music.vue";
import ContactThankYou from "@/views/ContactThankYou.vue";

const routes = [
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
        path: "/contact",
        name: "Contact",
        component: Contact,
        meta: {
            title: 'Contact - Daniel Online!'
        }
    },
    {
        path: "/code",
        name: "Code",
        component: Code,
        meta: {
            title: 'Code - Daniel Online!'
        }
    },
    {
        path: "/plants",
        name: "Plants",
        component: Plants,
        meta: {
            title: 'Plants - Daniel Online!'
        }
    },
    {
        path: "/music",
        name: "Music",
        component: Music,
        meta: {
            title: 'Music - Daniel Online!'
        }
    },
    {
        path: "/contact/thank-you",
        name: "ContactThankYou",
        component: ContactThankYou,
        meta: {
            title: 'Thanks - Daniel Online!'
        }
    }
];

const router = createRouter ({
    history: createWebHistory(),
    routes
});

/***************************************************************************/
// Metadata Update Block
// This callback runs before every route change, including on page load.
// Updates page Metadata using info from @/router/index.js
router.beforeEach((to, from, next) => {

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