<template lang="html">
    <div id="body" class="fade-in">
        <img class="logo" src="@/assets/images/star-logo.png" width="105">
        <h1>404 PAGE NOT FOUND</h1>
        <p>SORRY, WE CAN'T FIND THAT PAGE BUT THERE ARE OTHERS TO LOOK AT</p>
        <ul class="nav nav-pills" id="PlantTabs" role="tablist">
            

            <li class="nav-item" role="presentation">
                    <router-link class="nav-link active" to="/">GO HOME</router-link>
            </li>
        </ul>

    </div>
    <Footer></Footer>
</template>

<script lang="js">

import Footer from "@/components/Footer-Large.vue";


export default {
    name: 'notFound',
    components: {
        Footer
    }
}

</script>

<style scoped>
#body{
    min-height: 55vw;
}
h1{
    font-size: 150px !important;
    margin-top: 60px;
}
p{
    color: var(--theme-white);
    font-size: 32px !important;
    padding-bottom: 30px;
    margin-bottom: 50px;
    border-bottom: 1px solid var(--theme-black);
}
#care-tab{
  background-color: var(--theme-blackest) !important;
}
#care-tab:hover{
  background-color: var(--theme-primary-light) !important;
}
.nav-link{
  font-size: 20px !important;
  font-weight: bold;
  opacity: 0.75;
  padding-right: 60px;
  padding-left: 60px;
  background: #0d0d0d !important;
  opacity: 0.5 !important;
  transition: 0.5s;
}
.nav-link:hover{
    background: var(--theme-primary-dark) !important;
    opacity: 1 !important;
}
.logo {
    opacity: 0.5;
}
</style>