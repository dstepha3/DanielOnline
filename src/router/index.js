import { createWebHistory, createRouter} from "vue-router";

import Home from "@/views/Home.vue";
import About from "@/views/About.vue";
import Contact from "@/views/Contact.vue";
import Code from "@/views/Code.vue";
import Plants from "@/views/Plants.vue";
import Music from "@/views/Music.vue";

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/about",
        name: "About",
        component: About
    },
    {
        path: "/contact",
        name: "Contact",
        component: Contact
    },
    {
        path: "/code",
        name: "Code",
        component: Code
    },
    {
        path: "/plants",
        name: "Plants",
        component: Plants
    },
    {
        path: "/music",
        name: "Music",
        component: Music
    }
];

const router = createRouter ({
    history: createWebHistory(),
    routes
});

export default router;