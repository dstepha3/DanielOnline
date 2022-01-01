
<template>
  <div class="fade-in">
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>


<style scoped>
div {
    display: flex;
    justify-content: center;
    text-align: center;
    align-content: center;
    align-items: center;
    height: 40vw;
}
p {
    font-size: 52px !important;
    color: var(--theme-primary-dark);
}
</style>