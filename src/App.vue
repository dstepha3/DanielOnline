<template>
    <div id="app">
      <NavBar></NavBar>
      <div id="body">
        <router-view/>
      </div>
    </div>
</template>

<script>
import NavBar from "./components/NavBar";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

