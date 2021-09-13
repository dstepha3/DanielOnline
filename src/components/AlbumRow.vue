<template lang="html">

<div style="margin-bottom: 60px; border-bottom: 2px solid var(--theme-primary-light)" id="carouselExampleControls" class="carousel slide carousel-fade" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/bitch-boy-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn purple" data-bs-toggle="modal" data-bs-target="#bitchboyModal">
            Listen to #BitchBoy
        </button>
      </div>
   </div>
    <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/paradise-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn pink" data-bs-toggle="modal" data-bs-target="#paradiseModal">
            Listen to Paradise
        </button>
      </div>
   </div>
    <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/highway-of-love-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn pink" data-bs-toggle="modal" data-bs-target="#highwayOfLoveModal">
            Listen to Highway of Love
        </button>
      </div>
   </div>
   <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/book-of-daniel-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn red" data-bs-toggle="modal" data-bs-target="#bookOfDanielModal">
            Listen to The Book of Daniel
        </button>
      </div>
   </div>
   <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/book-of-life-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn blue" data-bs-toggle="modal" data-bs-target="#bookOfLifeModal">
            Listen to The Book of Life
        </button>
      </div>
   </div>
   <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/love-me-all-night-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn red" data-bs-toggle="modal" data-bs-target="#loveMeAllNightModal">
            Listen to Love Me All Night
        </button>
      </div>
   </div>
   <div class="carousel-item">
      <img src="@/assets/images/album_covers/carousel/24-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn white" data-bs-toggle="modal" data-bs-target="#twentyFourModal">
            Listen to twentyfour
        </button>
      </div>
   </div>
   <div class="carousel-item active">
      <img src="@/assets/images/album_covers/carousel/no-love-left-carousel.png" class="d-block w-100">
      <div class="carousel-caption d-none d-md-block">
        <button type="button" class="ds-btn" data-bs-toggle="modal" data-bs-target="#noLoveLeftModal">
            Listen to No Love Left
        </button>
      </div>
   </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>

<bitchboy_modal></bitchboy_modal>
<paradise_modal></paradise_modal>
<highway_of_love_modal></highway_of_love_modal>
<book_of_daniel_modal></book_of_daniel_modal>
<book_of_life_modal></book_of_life_modal>
<love_me_all_night_modal></love_me_all_night_modal>
<twentyfour_modal></twentyfour_modal>
<no_love_left_modal></no_love_left_modal>

</template>

<script>
import bitchboy_modal from "@/components/Modals/Music/BitchBoy-modal.vue";
import paradise_modal from "@/components/Modals/Music/Paradise-modal.vue";
import highway_of_love_modal from "@/components/Modals/Music/HighwayOfLove-modal.vue";
import book_of_daniel_modal from "@/components/Modals/Music/BookOfDaniel-modal.vue";
import book_of_life_modal from "@/components/Modals/Music/BookOfLife-modal.vue";
import love_me_all_night_modal from "@/components/Modals/Music/LoveMeAllNight-modal.vue";
import twentyfour_modal from "@/components/Modals/Music/twentyfour-modal.vue";
import no_love_left_modal from "@/components/Modals/Music/NoLoveLeft-modal.vue";

export default {
    name: "album_row",
     components: {
       bitchboy_modal,
       paradise_modal,
       highway_of_love_modal,
       book_of_daniel_modal,
       book_of_life_modal,
       love_me_all_night_modal,
       twentyfour_modal,
       no_love_left_modal
    }
}

</script>

<style scoped>
.flex {
    display: flex;
}
.row {
    margin: 0 0 60px;
}
.album-container{
    flex-basis: 25%;
}
.album-container img{
    width: 100%;
}

.carousel-item{
  max-height: 705px;
}

.ds-btn {
    background: none;
    padding: 10px 100px;
    font-family: var(--text);
    color: var(--theme-whitest);
    font-weight:700;
    text-transform: uppercase;
    border-radius: 15px;
    border: 2px solid var(--theme-whitest);
    opacity: .9;
}
.ds-btn:hover {
    color: var(--theme-blackest);
    border: 2px solid var(--theme-blacker);
    opacity: .90;
    font-weight:900;
    box-shadow: 0px 0px 15px 5px var(--theme-white);
}
.ds-btn.red:hover {
    color: var(--theme-primary-light);
    border: 2px solid var(--theme-primary-light);
    box-shadow: 0px 0px 15px 5px var(--theme-primary-light);
}
.ds-btn.blue:hover {
    color: var(--theme-confirm);
    border: 2px solid var(--theme-confirm);
    box-shadow: 0px 0px 15px 5px var(--theme-confirm);
}
.ds-btn.pink:hover {
    color: #ff4dff;
    border: 2px solid #ff4dff;
    box-shadow: 0px 0px 15px 5px #ff4dff;
}
.ds-btn.purple:hover {
    color: purple;
    border: 2px solid purple;
    box-shadow: 0px 0px 15px 5px purple;
}
.ds-btn.white:hover {
    color: var(--theme-whitest);
}

@media screen and (max-width: 768px){
  .d-none{
    display: block !important;
  }
  .ds-btn {
    padding: 10px 57px;
    min-width: 100%;
  }
  .carousel-item .carousel-caption{
    bottom: 20%;
  }
  .carousel-item img{
    opacity: 0.10;
  }
  .carousel-control-prev,
  .carousel-control-next {
    top: 0;
  }
  .ds-btn.red {
    color: var(--theme-primary-light);
    border: 2px solid var(--theme-primary-light);
  }
  .ds-btn.blue {
      color: var(--theme-confirm);
      border: 2px solid var(--theme-confirm);
  }
  .ds-btn.pink {
      color: #ff4dff;
      border: 2px solid #ff4dff;
  }
  .ds-btn.purple{
      color: purple;
      border: 2px solid purple;
  }
  .carousel-item{
    max-height: 180px;
  }
}

</style>