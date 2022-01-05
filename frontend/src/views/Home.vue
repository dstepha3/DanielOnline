<template lang="html">
    <div id="body" class="fade-in">
        <router-link to="/about" class="hidden">click</router-link>
        <h1>Welcome to DanielOnline</h1>
        <img style="margin-top: 40px;" src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Under_construction_animated.gif">
        <span class="coming-soon">Sorry, we're still under construction. <br/> Please come back later!</span>
    </div>
</template>

<script lang="js">

export default {
    name: 'home'
}

</script>

<style scoped>
  #body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 50vw;
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
  }
</style>