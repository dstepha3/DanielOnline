<template>
    <div id="app">
      <NavBar></NavBar>
      <div class="coming-soon">
        <h1>CONTENT <br/>COMING SOON</h1>
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

