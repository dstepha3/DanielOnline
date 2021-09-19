<template>
    <div id="app" v-if="show">
      <router-view  v-slot="{ Component }">
     
          <component :is="Component" />
   
      </router-view>

    </div>
</template>

<script>

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

export default {
  name: 'App',
  data() {
    return {
      show: false
    }
  },
  mounted() {
    this.show = true; // might need this.$nextTick
  }
}
</script>


<style scoped>
#app {
	opacity: 1;
	animation-name: fadeInOpacity;
	animation-iteration-count: 1;
	animation-timing-function: ease-in;
	animation-duration: 1s;
}

@keyframes fadeInOpacity {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}
</style>

