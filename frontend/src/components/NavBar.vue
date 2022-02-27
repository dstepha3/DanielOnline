<template lang="html">

<transition name="slide">
    <Toast v-if="showToast" :message="$store.state.pageLogoutMessage" :primary="true" style="z-index: 500" />
</transition>

<div id="navbar">
    <div class="login-dash-container">
            <router-link to="/admin" v-if="!$store.state.adminAuthPassed">
                <i class="fas fa-user-circle"></i>
            </router-link>
    </div>
    <div class="login-dash-container Logged-In">
            <div class="LoggedIn" v-if="$store.state.adminAuthPassed">
                <p>Welcome Daniel.</p>
            </div>
            <div class="mobile-box" v-if="$store.state.adminAuthPassed">
                <router-link to="/admin">Admin Dashboard</router-link>
                <a class="logout" v-on:click="admin_logout()">Logout</a>
            </div>
    </div>

    <div class="top-banner">
        <router-link to="/"><img src="@/assets/images/star-logo.png" width="105"></router-link>
    </div>

    <nav>
        <ul class="nav mobile">
            <a id="nav-toggle" v-on:click="toggleMenu()"><i class="fas fa-bars"></i></a>
        </ul>
        <ul class="nav full-nav justify-content-center">
            <li class="nav-item">
                <router-link class="nav-link" to="/">Home</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/about">About</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/blog">Blog</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/contact">Contact</router-link>
            </li>
            <!-- <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Dropdown link
                </a>
                <ul class="dropdown-menu center" aria-labelledby="navbarDropdownMenuLink">
                    <li><router-link class="nav-link" to="/">Action</router-link></li>
                    <li><router-link class="nav-link" to="/">Another Action</router-link></li>
                    <li><router-link class="nav-link" to="/">Something else here</router-link></li>
                </ul>
            </li> -->
        </ul>
    </nav>

    <div v-if="sticky_nav_on">
        <nav id="navigation-bar" v-if="visible">
            <ul class="nav mobile">
                <a id="nav-toggle" v-on:click="toggleMenu()"><i class="fas fa-bars"></i></a>
            </ul>
            <ul class="nav full-nav justify-content-center">
                <li class="nav-item">
                    <router-link class="nav-link" to="/">Home</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/about">About</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/blog">Blog</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link" to="/contact">Contact</router-link>
                </li>
                <!-- <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Dropdown link
                    </a>
                    <ul class="dropdown-menu center" aria-labelledby="navbarDropdownMenuLink">
                        <li><router-link class="nav-link" to="/">Action</router-link></li>
                        <li><router-link class="nav-link" to="/">Another Action</router-link></li>
                        <li><router-link class="nav-link" to="/">Something else here</router-link></li>
                    </ul>
                </li> -->
            </ul>
        </nav>
    </div>

</div>
</template>

<script>

import Toast from "@/components/Toast"

export default {
    name: "nav-bar",
    components:{
        Toast
    },
    data(){
        return{
            showToast: false,
            visible: false,
            sticky_nav_on: true,
        }
    },
    methods: {
        admin_logout(){
            setTimeout(() => this.triggerToast(), 500);
            this.$store.commit('logout');
        },
        toggleMenu(){
            var x = document.getElementsByClassName("full-nav");
            x[0].classList.toggle('active');
        },
        triggerToast() {
                this.showToast = true;       
                setTimeout(() => this.showToast = false, 5000);
        },
        scrollTop: function () {
            this.intervalId = setInterval(() => {
                if (window.pageYOffset === 0) {
                clearInterval(this.intervalId);
                }
                window.scroll(0, window.pageYOffset - 1000);
            }, 20);
        },
        scrollListener: function () {
            let navbar = document.getElementById("navigation-bar");
            if( window.scrollY > 168 ){
                this.visible = true;
                if (navbar.classList.contains("sticky")){
                    // do nothing
                }
                else {
                    navbar.classList.add("sticky");
                }
            }
            if ( window.scrollY < 168 ) {
                this.visible = false;
                navbar.classList.remove("sticky");
            }
        },
    },
    mounted: function () {
        window.addEventListener("scroll", this.scrollListener);
    },
    beforeUnmount: function () {
        window.removeEventListener("scroll", this.scrollListener);
    },
}

</script>

<style scoped>

.nav {
    background-color: #000000;
    border-bottom:3px solid var(--theme-primary-dark);
    padding: 20px 0;
}
.nav a,
.nav-link {
    margin: 0 10px;
}
#navbar{
    position: relative;
}
#navbar a.router-link-exact-active{
    color: var(--theme-primary-light);
    border-bottom: 1px solid var(--theme-primary-dark);
}
.nav-item .nav-link.disabled{
    color:var(--theme-darkest-gray);
    opacity: 0.5;
}
ul.nav a:hover,
.dropdown .nav-link:hover,
.nav-link.active, 
.dropdown,
.dropdown .btn,
.dropdown .btn:hover,
.dropdown .btn:active,
.dropdown .btn:focus,
.dropdown-menu .dropdown-item,
.container .dropdown .dropdown-menu a:hover
{
    color: var(--theme-primary-light);
}
.dropdown .dropdown-menu a{
    color: var(--theme-whiter);
    min-width: 250px;
}
.dropdown-menu a:hover {
    color: var(--theme-primary-light) !important;
    font-weight: 500;
}
.nav a,
.dropdown .nav-link,
.dropdown .nav-link:focus{
    color: var(--theme-primary-dark);
}
.dropdown-menu .dropdown-item:hover {
    background: var(--theme-black);
}
.nav-item .dropdown-menu {
    background-color: var(--theme-blacker);
}

#navbar .top-banner {
    background: linear-gradient(to bottom, #000000 0%, #800000 250%);
    padding: 10px 0;
    position: relative;
display: flex;
justify-items: center;
align-content: center;
justify-content: center;
}

#navbar .top-banner img {
    position: relative;
    top: 10px;
}

#navbar .top-banner a.router-link-exact-active,
#navbar .top-banner a.router-link-active {
    border: none;
}

.dropdown-menu a.router-link-exact-active,
.dropdown-menu a.router-link-active  {
    background-color: #000000;
    border: none !important;
}

.dropdown-menu a.router-link-exact-active:hover {
    cursor: default;
}

.login-dash-container{
    position: absolute;
    width: 100%;
    display: flex;
    top: 15px;
    right: 30px;
    justify-content: flex-end;
    z-index: 85;
    text-align: right;
}
.login-dash-container.Logged-In{
    width: 100vw;
    display: flex;
    right: 0;
    justify-content: space-between;
    align-items: center;
    z-index: 85;
    text-align: center;
    padding: 0 40px;
}
.login-dash-container .fas{
    font-size: 20px;
    color: white;
    opacity: 0.1;
    margin: 0;
    transition: all 0.3s;
}
.login-dash-container .fas:hover{
    opacity: 0.6;
}
.login-dash-container .LoggedIn{
    display: flex;
    flex-direction: row;
    align-items: center;
}
.login-dash-container .LoggedIn p{ 
    font-size: 16px !important;
    margin-bottom: 0;
    color: var(--theme-primary-dark);
}
.login-dash-container.Logged-In a{
    color: var(--theme-primary-dark);
    font-size: 16px !important;
    text-decoration: none;
    margin: 0;
    transition: all 0.3s;
}
.login-dash-container.Logged-In a:hover{
    color: var(--theme-primary-light);
}
.login-dash-container.Logged-In a.logout{
    margin-left: 40px;
    cursor: pointer;
}
.nav.mobile{
    padding-left: 20px;
    display: none;
}
.sticky{
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 99999999;
    height: 100%;
}

@media only screen and (max-width:768px){
    .nav{
        flex-direction: column;
    }
    #navbar a.router-link-exact-active{
        border-bottom: none;
    }
    .nav.mobile{
        display: block;
        border-bottom: 0;
    }
    .full-nav{
        padding: 0;
        height: 0;
        animation: slide-menu-close 0.6s ease-in-out;
        overflow: hidden;
        display: block;
    }
    .full-nav.active{
        height: 100%;
        height: 200px;
        animation: slide-menu-open 0.6s ease-in-out;
    }
    
    @keyframes slide-menu-open {
        0%{
            height: 0px;
        }
        100%{
            height: 200px;
        }
    }
    @keyframes slide-menu-close {
        0%{
            height: 200px;
        }
        100%{
            height: 0px;
        }
    }
    .login-dash-container.Logged-In a,
    .login-dash-container.Logged-In p{
        font-size: 12px !important;
    }
    .login-dash-container.Logged-In{
        flex-direction: column;
        align-items: flex-end;
        transform: translate(25px, 0px);
        text-align: right;
    }
    .mobile-box{
        display: flex;
        flex-direction: column;
    }
}

</style>