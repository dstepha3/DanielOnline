<template>
    <div id="app">
      <NavBar></NavBar>
        <router-view/>
      <FooterLarge></FooterLarge>
    </div>
</template>

<script>
import NavBar from "./components/NavBar";
import FooterLarge from "@/components/Footer-Large.vue";

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

export default {
  name: 'App',
  components: {
    NavBar,
    FooterLarge
  }
}
</script>

