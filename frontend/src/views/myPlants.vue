<template lang="html">

    <NavBar></NavBar>

    <div id="my-plants-body" class="fade-in">

        <!-- Top Content -->
        <div id="top-content-container">
            <h1>My Plants</h1>
            <p class="top-content">During the Coronavirus Pandemic, I decided to jump on the indoor plant bandwagon with the rest of the world. I never really had much experience with plants before and I had no idea if I even had a green thumb. My friend Shannon gave me my first plant - a Golden Pothos (<em>Epipremnum aureum</em>) and I began watching videos by <a href="https://planterina.com/">Amanda from Planterina</a> on <a href="https://www.youtube.com/c/Planterina">Youtube</a> to extend my knowledge into indoor gardening. Over the years I've grown my collection into the vast little jungle it is today. You can explore my collection below, learn how to care for plants and even request cuttings grown by me.<br/><br/>Check it out!</p>
        </div>

        <div class="banner-image"></div>

        <div class="plant-search-container">

            <div id="search-box" v-if=" !isLoadingPlants && !loadingError">
                <!-- Search Bar -->
                <div class="form-group">
                    <i class="fas fa-search fa-lg"></i>
                    <input class="form-control" id="plantSearch" @keyup="search()" type="text" placeholder="Looking for Something Specific?">
                </div>

            
                <!-- Category Selectors -->
                <div class="category row">
                    <ul class="nav nav-pills" id="IndoorTab" role="tablist">
                        <li class="nav-item" role="presentation">
                                <router-link class="nav-link active" to="/">INDOOR</router-link>
                        </li>
                    </ul>

                    <ul class="nav nav-pills" id="OutdoorTab" role="tablist">
                        <li class="nav-item" role="presentation">
                                <router-link class="nav-link active" to="/">OUTDOOR</router-link>
                        </li>
                    </ul>
                </div>
            </div>
     
            <!-- Plant Cards -->
            <div id="plant-container" v-if=" !isLoadingPlants && !loadingError ">
                <div class="row">
                    <div class="col-sm-6 col-md-4 my-4" v-for="plant in plants" :key="plant">
                        <a v-if="plant.active" data-bs-toggle="modal" :data-bs-target="plant.modal_id">
                            <div class="plant card">
                                <img :src="plant.img_src" class="card-img-top" alt="img">
                                <div class="card-body">
                                    <h5 class="card-title">{{ plant.name }}</h5>
                                </div>
                            </div>
                        </a>
                        <a v-if="!plant.active"  class="nav-link disabled">
                            <div class="plant card">
                                <img :src="plant.img_src" class="card-img-top" alt="img">
                                <div class="card-body">
                                    <h5 class="card-title">{{ plant.name }}</h5>
                                </div>
                            </div>
                        </a>
                    </div>
                </div>
            </div>
          

        
            <div id="loading-container" v-if=" isLoadingPlants && !loadingError">
                <div id="render-spiner-container">
                    <div class="spinner-border" id="render-spinner" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <p id="loadingtext">Gathering my Plants</p>
                </div>
            </div>
          

            <div id="error-container" v-if=" !isLoadingPlants && loadingError">
                    <p id="error-message">Unable to Load Plants</p>
            </div>

        </div>

        <!-- CTA -->
        <div class="row cta">
            <h3>Did You Know..</h3>
            <p>You can keep up with me and learn more about my plants?</p>
            <p>Learn more and read up on everything me!</p>
            <router-link to="/blog" class="cta-btn">Go To Blog</router-link>
        </div>

        
    </div>

    <div class="img-container">
        <img class="image" src="https://i.imgur.com/aCRP3jj.jpg">
        <div class="overlay"></div>
    </div>

    <FooterLarge></FooterLarge>

    <!-------------- Modals --------------->
    <epipremnumModal></epipremnumModal>
    <palmsModal></palmsModal>
    <snakeModal></snakeModal>
    <succModal></succModal>
    <philoModal></philoModal>
    <zzModal></zzModal>
    <myGardenModal></myGardenModal>
    <scindapsusModal></scindapsusModal>
    <dracaenaModal></dracaenaModal>
    <rhaphModal></rhaphModal>
    <aglaModal></aglaModal>
    <ficusModal></ficusModal>
    <marantaModal></marantaModal>
    <calatheaModal></calatheaModal>
    <miscModal></miscModal>
    <syngModal></syngModal>
    <!-------------------------------------->
</template>

<script lang="js">
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import epipremnumModal from "@/components/Modals/Plants/Epipremnum-modal.vue";
import palmsModal from "@/components/Modals/Plants/Palms-modal.vue";
import snakeModal from "@/components/Modals/Plants/Sanseveria-modal.vue";
import succModal from "@/components/Modals/Plants/Succulents-modal.vue";
import philoModal from "@/components/Modals/Plants/Philo-modal.vue";
import zzModal from "@/components/Modals/Plants/ZZ-modal.vue";
import myGardenModal from "@/components/Modals/Plants/myGarden-modal.vue";
import scindapsusModal from "@/components/Modals/Plants/Scindapsus-modal.vue";
import dracaenaModal from "@/components/Modals/Plants/Dracaena-modal.vue";
import rhaphModal from "@/components/Modals/Plants/Rhaph-modal.vue";
import aglaModal from "@/components/Modals/Plants/Aglaonema-modal.vue";
import ficusModal from "@/components/Modals/Plants/Ficus-modal.vue";
import marantaModal from "@/components/Modals/Plants/Maranta-modal.vue";
import calatheaModal from "@/components/Modals/Plants/Calathea-modal.vue";
import miscModal from "@/components/Modals/Plants/Misc-modal.vue";
import syngModal from "@/components/Modals/Plants/Syngonium-modal.vue";


import axios from 'axios';

export default {
    name: 'myPlants',
    data() {
        return {
            plants: [],
            isLoadingPlants: false,
            loadingError: false,
            isLoadingThumbs: true,
        };
    },
    components: {
        NavBar,
        FooterLarge,
        epipremnumModal,
        palmsModal,
        snakeModal,
        succModal,
        philoModal,
        zzModal,
        myGardenModal,
        scindapsusModal,
        dracaenaModal,
        rhaphModal,
        aglaModal,
        ficusModal,
        marantaModal,
        calatheaModal,
        miscModal,
        syngModal
    },
    methods: {
        search() {

        },
        getMyPlants() {
            const path = 'http://localhost:5000/api/plants';
            axios.get(path)
                .then((res) => {
                    this.plants = res.data;
                    setTimeout(() => this.isLoadingPlants = false, 3000);
                })
                .catch((error) => {
                    console.error(error);
                    setTimeout(() => this.isLoadingPlants = false, 3000);
                    setTimeout(() => this.loadingError = true, 3000);
                })
        }
    },
    created() {
        this.isLoadingPlants = true;
        this.getMyPlants();
    },
}

</script>

<style scoped>
#my-plants-body{
    margin: 80px 15%;
    text-align: center;
    color: var(--theme-primary-dark);
}

#top-content-container{
    border-bottom: 1px solid var(--theme-primary-dark);
    padding-bottom: 80px;
}

.top-content {
    margin-top: 30px;
    color: var(--theme-white);
    text-align: justify;
}

.top-content a {
    color: var(--theme-primary-dark);
    text-decoration: none;
}
.top-content a:hover {
    text-decoration: underline;
}

.banner-image{
    width: 100%;
    margin-top: 120px;
    margin-bottom: 120px;
    border: 1px solid var(--theme-blackest);

    /* Parallax */
    background-image: url("https://i.imgur.com/FXKK85o.jpg");
    min-height: 330px;
    background-position: center center;
    background-size: cover;
    background-repeat: no-repeat;
}



.plant-search-container{
    border-top: 1px solid var(--theme-primary-light);
    margin: 80px 0;
    padding-top: 80px;
}

.form-group {
    display: flex;
    margin: 0 15%;
    transition: fadase
}
.fa-search{
    position: relative;
    top: 12px;
    margin-left: 30px;
    padding-right: 30px;

}

#no-results-found{
    display: none;
    width: 100% !important;
    margin: 100px auto 0 !important;
}

#error-message{
    padding: 40px;
    border: 1px dashed var(--theme-primary-dark);
    margin-left: 20%;
    margin-right: 20%;
}

#search-box,
#plant-container,
#loading-container,
#error-container {
  animation: fadeIn 5s;
}
@keyframes fadeIn {
  0% {opacity:0;}
  100% {opacity:1;}
}


#plant-container a{
    color: var(--theme-primary-dark);
    text-decoration: none;
}

#plant-container .row{
    margin: 3rem 0;
}

.plant.card:hover{
    box-shadow: 0px 0px 20px 1px var(--theme-primary-light);
    border: 1px solid var(--theme-blackest);
    opacity: 1;
}

#plant-container .nav-link.disabled{
    padding: 0 !important;
}
.plant.card.disabled{
    opacity: 0.4;
}

.plant.card .card-img-top{
    max-height: 175px;
    border-radius: 20px 20px 0 0;
}

.plant.card{
    background: #000000;
    border: 1px solid var(--theme-primary-dark);
    cursor: pointer;
    opacity: 0.6;
    transition: 0.3s;
    border-radius: 20px;
}
.card-img-top{
    max-height: 200px;
    object-fit: cover;
    border-bottom: 1px solid var(--theme-primary-dark);
    border-radius: 20px 20px 0 0;
}
.card-title{
    text-transform: uppercase;
    cursor: pointer;
}

.card-text{
    display: none;
    text-transform: uppercase;
}

.category{
    margin-top: 60px;
    justify-content: space-evenly;
}

.nav-link{
  font-size: 20px !important;
  font-weight: bold;
  opacity: 0.75;
  padding-right: 60px;
  padding-left: 60px;
  background: #0d0d0d !important;
  border: 1px solid var(--theme-primary-dark);
  border-radius: 20px;
  opacity: 0.5 !important;
  transition: 0.5s;
}
.nav-link:hover{
    background: var(--theme-primary-dark) !important;
    opacity: 1 !important;
}

#IndoorTab{
    flex-basis: 35%;
    display: inline;
}

#OutdoorTab{
    flex-basis: 35%;
    display: inline;
}

#render-spiner-container{
    height: 100%;
    width: 100%;
    background: none;
    position: relative;
}
#render-spinner{
    opacity: 0.4;
}

#loadingtext{
    color: var(--theme-whitest);
    margin-top: 20px;
    font-size: 10px !important;
    font-weight: 900;
    text-transform: uppercase;
    animation-duration: 2s;
    animation-name: grow;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
    position: absolute;
    top: -11px;
}
#loadingtext:hover{
    cursor: default;
}

@keyframes grow {
    0% {
      transform: scale(1);
      opacity: 0.6;
    }
  
    50%{
      transform: scale(1.1);
      opacity: 1;
    }

    100%{
      transform: scale(1);
      opacity: 0.6;
    }
  }

.img-container .image{
    width: 100%;
    position: relative;
}
.img-container .overlay{
    background: linear-gradient(180deg, rgba(13,13,13,1) 1%, rgba(255,255,255,0) 100%);     
    position: absolute;
    top: 0;
    content: '';
    z-index: 99;
    height: 400px;
    width: 100%;
}
.img-container{
    position: relative;
    margin-top: 120px;
}




</style>