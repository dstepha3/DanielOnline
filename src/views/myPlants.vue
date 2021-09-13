<template lang="html">
    <NavBar></NavBar>
    <div id="my-plants-body">
        <h1>My Plants</h1>
        <p class="top-content">During the pandemic...</p>
        <div class="plant-search-container">
            <div class="form-group">
                <i class="fas fa-search fa-lg"></i>
                <input class="form-control" id="plantSearch" @keyup="myFunction()" type="text" placeholder="Looking for Something Specific?">
            </div>
            <div class="category row">
                <a class="btn btn-danger">Indoor</a>
                <a class="btn btn-danger">Outdoor</a>
            </div>
     
            <div id="plant-container">
                <div class="row">
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#epipremnumModal"><div class="plant card">
                            <img src="@/assets/images/plants/pothos1.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">epipremnum</h5>
                                <p class="card-text">pothos</p>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#palmsModal"><div class="plant card">
                            <img src="@/assets/images/plants/IMG_3917.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Palms</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#snakeModal"><div class="plant card">
                            <img src="@/assets/images/plants/sansevieria.jpg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Sanseveria</h5>
                            </div>
                        </div></a>
                    </div>
                </div>

                <div class="row">
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#succulentsModal"><div class="plant card">
                            <img src="@/assets/images/plants/succulents-cropped.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Succulents</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#philoModal"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">PHILODENDERON</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#zzModal"><div class="plant card">
                            <img src="@/assets/images/plants/zz-cropped.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">ZZ</h5>
                            </div>
                        </div></a>
                    </div>
                </div>

                <div class="row">
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#gardenModal"><div class="plant card">
                            <img src="@/assets/images/plants/garden-cropped.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">garden</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#scindapsusModal"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">scindapsus</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#dracaenaModal"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">dracaena</h5>
                            </div>
                        </div></a>
                    </div>
                </div>

                <div class="row">
                    <div class="col">
                        <a class="nav-link disabled" data-bs-toggle="modal" data-bs-target="#rhaphModal"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">rhaphidophora</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#aglaModal"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">aglaonema</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a data-bs-toggle="modal" data-bs-target="#ficusModal"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">ficus</h5>
                            </div>
                        </div></a>
                    </div>
                </div>  

                <div class="row">
                    <div class="col">
                        <a class="nav-link disabled" data-bs-toggle="modal" data-bs-target="#marantaModal"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Maranta</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a class="nav-link disabled" data-bs-toggle="modal" data-bs-target="#calatheaModal"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Calathea</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <!-- <a class="nav-link disabled" href="#"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder2.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Untitled</h5>
                            </div>
                        </div></a> -->
                    </div>
                </div>  

            <!-- ROW TEMPLATE 
                <div class="row">
                    <div class="col">
                        <a class="nav-link disabled" href="#"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Untitled</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a class="nav-link disabled" href="#"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Untitled</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a class="nav-link disabled" href="#"><div class="plant card disabled">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-title">Untitled</h5>
                            </div>
                        </div></a>
                    </div>
                </div>  
            -->

            </div>
        </div>
    </div>
    <FooterLarge></FooterLarge>

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

export default {
    name: 'myPlants',
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
        calatheaModal
    },
    methods: {
        myFunction() {
            console.log("start.");
            var input, filter, cards, cardContainer, title, i, rows, j ;
            input = document.getElementById("plantSearch");
            filter = input.value.toUpperCase();
            cardContainer = document.getElementById("plant-container");
            cards = cardContainer.getElementsByClassName("card");
            rows = cardContainer.getElementsByClassName("row");
            for (i = 0; i < cards.length; i++) {
                title = cards[i].querySelector(".card-body h5.card-title");
                if (title.innerText.toUpperCase().indexOf(filter) > -1){
                    title.style.marginLeft = "30px";
                    cardContainer.style.marginTop = "3rem";
                    cards[i].style.display = "block ruby";
                    cards[i].style.margin = "0 0 4rem 0";
                    for (j = 0; j < rows.length; j++) {
                        rows[j].style.flexDirection = "column";
                        rows[j].style.margin = "0 50% 0 0";
                    }
                } else {
                    cards[i].style.display = "none";  
                }

                if (input.value == ""){
                    console.log("its empty")
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

        }
    }
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
}
.fa-search{
    position: relative;
    top: 12px;
    margin-left: 30px;
    padding-right: 30px;

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
    margin-top: 40px;
    justify-content: space-evenly;
}

.category .btn {
    flex-basis: 30%;
}

.btn-danger{
    background-color: var(--theme-primary-dark);
}

.btn-danger:hover{
    opacity: 0.75;
}




</style>