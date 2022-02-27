<template lang="html">
    <div id="body" class="fade-in">
        <h1>Mix-n-Match</h1>

        <div class="game-container">
            <div class="game-info-container">
                <div class="game-info">
                    <div class="time-container">
                        <h3>Time</h3>
                        <span id="time">100</span>
                    </div>
                    <div class="flips-container">
                        <h3>Flips</h3>
                        <span id="flips">0</span>
                    </div>
                </div>
                <div class="cards-container">
                    <div class="card">
                        <div class="card-back card-face">

                        </div>
                        <div class="card-front card-face">
                        
                        </div>
                    </div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                    <div class="card"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="js">

export default {
    name: 'MatchingGame'
}

</script>

<style scoped>
  #body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    position: relative;
  }
  .game-container{
      margin-top: 20px;
      width: 800px;
      display: block;
  }
  .game-info{
      display: flex;
      justify-content: space-between;      
  }
  .time-container, .flips-container{
      display: flex;
      align-items: center;
  }
  .time-container h3, .flips-container h3{
      margin-right: 40px;
  }
  #time, #flips{
      font-size: 28px !important;
  }
  .card{
      background: url('https://wallpaperaccess.com/full/1899171.jpg');
      background-size: cover;
      background-position: center center;
      border: 1px solid #0d0d0d;
      height: 225px;
      width: 150px;
      cursor: pointer;
  }
  .cards-container{
      margin-top: 10px;
      display: grid;
      grid-template-columns: repeat(5, auto);
      grid-gap: 10px;
  }

  @media screen and (max-width: 768px){
      #body{
          text-align: center;
          padding-top: 120px;
      }
      h1{
          line-height: 0.9 !important;
      }
  }
</style>