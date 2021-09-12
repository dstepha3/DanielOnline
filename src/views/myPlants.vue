<template lang="html">
    <NavBar></NavBar>
    <div id="my-plants-body">
        <h1>My Plants</h1>
        <p class="top-content">During the pandemic...</p>
        <div class="plant-search-container">
            <div class="form-group">
                <i class="fas fa-search fa-lg"></i>
                <input class="form-control" id="plantSearch" type="text" placeholder="Looking for Something Specific?">
            </div>
            <div class="category row">
                <a class="btn btn-danger">Indoor</a>
                <a class="btn btn-danger">Outdoor</a>
                <a class="btn btn-danger">Garden</a>
            </div>

            
            <div class="plant-container">
                <div class="row mt-5 mb-5">
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/pothos1.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">epipremnum</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/palm2.jpg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">Palms</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/sansevieria.jpg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">Sanseveria</h5>
                            </div>
                        </div></a>
                    </div>
                </div>

                <div class="row mt-5 mb-5">
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">Succulents</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">PHILODENDERON</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">ZZ</h5>
                            </div>
                        </div></a>
                    </div>
                </div>

                <div class="row mt-5 mb-5">
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/garden1.jpeg" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">garden</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">untitled</h5>
                            </div>
                        </div></a>
                    </div>
                    <div class="col">
                        <a href="#"><div class="plant card">
                            <img src="@/assets/images/plants/plant-placeholder.png" class="card-img-top" alt="img">
                            <div class="card-body">
                                <h5 class="card-text">untitled</h5>
                            </div>
                        </div></a>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <FooterLarge></FooterLarge>
</template>

<script lang="js">
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";

export default {
    name: 'myPlants',
    components: {
        NavBar,
        FooterLarge,

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


.plant-container a{
    color: var(--theme-primary-dark);
    text-decoration: none;
}

.plant.card:hover{
        box-shadow: 0px 0px 15px 5px var(--theme-primary-light);

}

.plant.card{
    background: #000000;
    border: 1px solid var(--theme-primary-dark);
}
.card-img-top{
    max-height: 200px;
    object-fit: cover;
    border-bottom: 1px solid var(--theme-primary-dark);
}
.card-text{
    text-transform: uppercase;
}

.category{
    margin-top: 40px;
    justify-content: space-evenly;
}

.category .btn {
    flex-basis: 25%;
}

.btn-danger{
    background-color: var(--theme-primary-dark);
}

.btn-danger:hover{
    opacity: 0.75;
}




</style>