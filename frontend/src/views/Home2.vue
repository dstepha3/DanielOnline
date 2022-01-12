<template lang="html">
<NavBar />
    <div id="body" class="fade-in">
        
    </div>
</template>

<script lang="js">

import axios from "axios";
import NavBar from "@/components/NavBar.vue";

export default {
    name: 'home',
    data(){
        return{
            api: null,
        }
    },
    components:{
        NavBar
    },
    beforeCreate(){
        if(navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(position => {
                const api_key = '8bded61e127a445f9b87e776f831d609';
                this.api = `api.openweathermap.org/data/2.5/weather?lat=${position.coords.latitude}&lon=${position.coords.latitude}&appid=${api_key}`
                this.setWeather();
                this.$store.commit('gotWeather');
            })
            // do nothing
        }
    },
    methods:{
        setWeather(){
            console.log(this.api);
            axios
                .get(this.api)
                .then(response => (console.log(response)));
        }
    }
}

</script>

<style scoped>
  #body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    position: relative;
  }
  .coming-soon{
      color: var(--theme-primary-dark);
      font-family: var(--text);
      text-transform: uppercase;
      font-size: 20px;
      margin-top: 20px;
      text-align: center;
  }
  .hidden{
      color: #0d0d0d;
      width: 100%;
      position: absolute;
      top:0;
  }

  @media screen and (max-width: 768px){
      #body{
          text-align: center;
          padding-top: 120px;
      }
      h1{
          line-height: 0.9 !important;
      }
      .coming-soon{
          font-size: 16px;
      }
      img{
          opacity: 0.6;
      }
  }
</style>