<template lang="html">
<div id="navbar">

    <div class="top-banner" v-if="display">
        <router-link to="/"><img src="@/assets/images/star-logo.png" width="105"></router-link>
    </div>

    <nav>
        <ul class="nav justify-content-center">
            <li class="nav-item">
                <router-link class="nav-link disabled" to="/code">Code</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link disabled" to="/plants">Plants</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/music">Music</router-link>
            </li>
            <li class="nav-item">
                <router-link class="nav-link" to="/about">About</router-link>
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
    name: "nav-bar",
    props : {
        display: {
            type: Boolean,
            default: true
        }
    }
}

</script>