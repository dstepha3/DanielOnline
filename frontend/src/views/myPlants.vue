<template lang="html">

    <NavBar></NavBar>

    <div id="my-plants-body">

        <!-- Top Content -->
        <h1>My Plants</h1>
        <p class="top-content">During the pandemic...</p>

        <div class="plant-search-container">

            <div v-if=" !isLoadingPlants">
                <!-- Search Bar -->
                <div class="form-group">
                    <i class="fas fa-search fa-lg"></i>
                    <input class="form-control" id="plantSearch" @keyup="myFunction()" type="text" placeholder="Looking for Something Specific?">
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
            <transition name="fade">
                <div id="plant-container" v-if=" !isLoadingPlants ">
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
            </transition>

            <div id="container" v-if=" isLoadingPlants && !loadingError">
                <div id="render-spiner-container">
                    <div class="spinner-border" id="render-spinner" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <p id="loadingtext">Gathering my Plants</p>
                </div>
            </div>

            <div id="container" v-if=" !isLoadingPlants && loadingError">
                <div id="render-spiner-container">
                    <div class="spinner-border" id="render-spinner" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <p id="loadingtext">Gathering my Plants</p>
                </div>
            </div>

        </div>

        <!-- CTA -->
        <div class="row cta">
            <h3>Call Out Section</h3>
            <p>Did you know... blah blah blah..</p>
            <a href="#" class="cta-btn">Click Me</a>
        </div>

        
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

import axios from 'axios';

export default {
    name: 'myPlants',
    data() {
        return {
            plants: [],
            isLoadingPlants: false,
            loadingError: false,
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
        miscModal
    },
    methods: {
        myFunction() {
            console.log("start.");
            var input, filter, cards, cardContainer, title, i, rows, j;
            var no_results_message, counter;
            counter = 0;
            input = document.getElementById("plantSearch");
            filter = input.value.toUpperCase();
            cardContainer = document.getElementById("plant-container");
            cards = cardContainer.getElementsByClassName("card");
            rows = cardContainer.getElementsByClassName("row");
            no_results_message = document.getElementById("no-results-found");
            for (i = 0; i < cards.length; i++) {
                title = cards[i].querySelector(".card-body h5.card-title");
                if (title.innerText.toUpperCase().indexOf(filter) > -1){
                    title.style.marginLeft = "30px";
                    cardContainer.style.marginTop = "3rem";
                    cards[i].style.display = "block ruby";
                    cards[i].style.margin = "0 0 4rem 0";
                    counter++;
                    for (j = 0; j < rows.length; j++) {
                        rows[j].style.flexDirection = "column";
                        rows[j].style.margin = "0 50% 0 0";
                    }
                } else {
                    cards[i].style.display = "none";  
                    console.log(i);

                    if ( counter == 0){
                        no_results_message.style.display = "block";
                    } else {
                        no_results_message.style.display = "none";
                    }
                }

                if (input.value == ""){
                    cardContainer.style.marginTop = "3rem";
                    cards[i].style.display = "flex";
                    cards[i].style.margin = "0";
                    title.style.marginLeft = "0";
                
                    for (j = 0; j < rows.length; j++) {
                        rows[j].style.flexDirection = "row";
                        rows[j].style.margin = "3rem 0";
                    }
                }
                
            }
        },
        getMyPlants() {
            const path = 'http://localhost:5000/api/plants';
            axios.get(path)
                .then((res) => {
                    this.plants = res.data;
                    this.isLoadingPlants = false;
                })
                .catch((error) => {
                    console.error(error);
                    this.isLoadingPlants = false;
                    this.loadingErorr = true;
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

.top-content {
    margin-top: 30px;
    color: var(--theme-white);
}

.plant-search-container{
    border-top: 1px solid var(--theme-primary-light);
    margin: 80px 0;
    padding-top: 80px;
}

.form-group {
    display: flex;
    margin: 0 15%;
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


#plant-container a{
    color: var(--theme-primary-dark);
    text-decoration: none;
}

#plant-container .row{
    margin: 3rem 0;
}

.plant.card:hover{
        box-shadow: 0px 0px 15px 5px var(--theme-primary-light);
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
}

.plant.card{
    background: #000000;
    border: 1px solid var(--theme-primary-dark);
    cursor: pointer;
    opacity: 0.6;
    transition: 0.3s;
}
.card-img-top{
    max-height: 200px;
    object-fit: cover;
    border-bottom: 1px solid var(--theme-primary-dark);
}
.card-title{
    text-transform: uppercase;
}

.card-text{
    display: none;
    text-transform: uppercase;
}

.category{
    margin-top: 60px;
    justify-content: space-evenly;
}

.row.cta{
    background: rgba(175, 0, 0, 0.15);
    margin: 0 10% !important;
    color: var(--theme-white);
    justify-content: center;
    padding: 40px;
    border: 1px solid var(--theme-primary-dark);
    flex-direction: unset !important;
}

.row.cta > p:last-child{
    margin-bottom: 0;
}

.cta .cta-btn {
    margin-top: 20px;
    margin-bottom: 0;
    background: var(--theme-blackest);
    color: var(--theme-white) !important;
    border: 1px solid var(--theme-primary-dark);
    padding: 10px 30px;
    max-width: 200px !important;
    text-transform: uppercase;
    opacity: 0.7;
    font-weight: bolder;
    transition: 0.2s;
}
.cta .cta-btn:hover {
    background: #000000;
    color: var(--theme-whitest) !important;
    border: 1px solid var(--theme-primary-light);
    opacity: 1;
}

.nav-link{
  font-size: 20px !important;
  font-weight: bold;
  opacity: 0.75;
  padding-right: 60px;
  padding-left: 60px;
  background: #0d0d0d !important;
  border: 1px solid var(--theme-primary-dark);
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





</style>