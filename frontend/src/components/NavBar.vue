<template lang="html">
<div id="navbar">

    <div class="top-banner">
        <router-link to="/"><img src="@/assets/images/star-logo.png" width="105"></router-link>
    </div>

    <nav>
        <ul class="nav justify-content-center">
            <li class="nav-item">
                <router-link class="nav-link disabled" to="/">Home</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/about">About</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link disabled" to="/blog">Blog</router-link>
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
</template>

<script>

export default {
    name: "nav-bar"
}

</script>

<style scoped>

/* #navbar{
    position: sticky;
    top: 0;
} */

.nav {
    background-color: #000000;
    border-bottom:3px solid var(--theme-primary-dark);
    padding: 20px 0;
}
.nav a,
.nav-link {
    margin: 0 10px;
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
</style>