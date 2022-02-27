<template>
  <a @click="scrollTop" v-show="visible" class="bottom-right">
    <slot></slot>
  </a>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
    };
  },
  methods: {
    scrollTop: function () {
      this.intervalId = setInterval(() => {
        if (window.pageYOffset === 0) {
          clearInterval(this.intervalId);
        }
        window.scroll(0, window.pageYOffset - 1000);
      }, 20);
    },
    scrollListener: function () {
      this.visible = window.scrollY > 150;
      if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        this.visible = false;
      }
    },
  },
  mounted: function () {
    window.addEventListener("scroll", this.scrollListener);
  },
  beforeUnmount: function () {
    window.removeEventListener("scroll", this.scrollListener);
  },
};
</script>

<style scoped>
.bottom-right {
  position: fixed;
  bottom: 20px;
  right: 20px;
  cursor: pointer;
  z-index: 500;
}
.bottom-right:hover {
  color: rgba(128, 0, 0, 1);
}
</style>