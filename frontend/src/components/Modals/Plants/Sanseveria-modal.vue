<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="snakeModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Sanseveria</h3>
      </div>
      <div class="plant-modal-body">
          <div class="content">
            <p>TSHSHSHSHSHHHFHHHSHHS.. imma snakeee.</p>
          </div>
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="birdsnest-tab" data-bs-toggle="tab" data-bs-target="#birdsnest" type="button" role="tab" aria-controls="birdsnest" aria-selected="false">Bird's Nest</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="cylindrica-tab" data-bs-toggle="tab" data-bs-target="#cylindrica" type="button" role="tab" aria-controls="cylindrica" aria-selected="true">Cylindrica</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="laurentii-tab" data-bs-toggle="tab" data-bs-target="#laurentii" role="button" aria-expanded="false">Laurentii</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="moonshine-tab" data-bs-toggle="tab" data-bs-target="#moonshine" role="button" aria-expanded="false">Moonshine</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="silver-flame-tab" data-bs-toggle="tab" data-bs-target="#silver-flame" role="button" aria-expanded="false">Silver Flame</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="cylindrica-star-tab" data-bs-toggle="tab" data-bs-target="#cylindrica-star" role="button" aria-expanded="false">Starfish</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="whale-tab" data-bs-toggle="tab" data-bs-target="#whale" role="button" aria-expanded="false">Whale Fin</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="zeylanica-tab" data-bs-toggle="tab" data-bs-target="#zeylanica" role="button" aria-expanded="false">Zeylanica</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="default" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container" style="margin-top: -5px">
                    <img height="250" src="@/assets/images/plants/sansevieria.jpg">
                </div>
            </div>
            <div class="tab-pane fade" id="birdsnest" role="tabpanel" aria-labelledby="birdnest-tab">
                Bird's Nest
            </div>
            <div class="tab-pane fade" id="cylindrica" role="tabpanel" aria-labelledby="cylindrica-tab">
                Cylindrica
            </div>
            <div class="tab-pane fade" id="cylindrica-star" role="tabpanel" aria-labelledby="cylindrica-star-tab">
                Starfish
            </div>
            <div class="tab-pane fade" id="laurentii" role="tabpanel" aria-labelledby="laurentii-tab">
                Laurentii
            </div>
            <div class="tab-pane fade" id="whale" role="tabpanel" aria-labelledby="whale-tab">
                Whale Fin
            </div>
            <div class="tab-pane fade" id="moonshine" role="tabpanel" aria-labelledby="moonshine-tab">
                Moonshine
            </div>
            <div class="tab-pane fade" id="silver-flame" role="tabpanel" aria-labelledby="silver-flame-tab">
                Silver Flame
            </div>
            <div class="tab-pane fade" id="zeylanica" role="tabpanel" aria-labelledby="zeylanica-tab">
                Zeylanica
            </div>
        </div>

      </div>
      <div class="modal-footer">
          <div>
            <button type="button" style="display: inline" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            <div style="display: inline" data-tooltip="View Sources"
       data-tooltip-location="right">
            <i class="fas fa-search"></i>
            </div>
          </div>
        <ul class="nav nav-pills" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="care-tab" type="button" role="tab" aria-controls="care" aria-selected="false">PLANT CARE</button>
            </li>
            <li v-if="cuttingsAvailable" class="nav-item" role="presentation">
                <button class="nav-link active" @click="goToRequest()" id="cuttings-tab" type="button" role="tab" aria-controls="cuttings" aria-selected="false">REQUEST CUTTINGS</button>
            </li>
            <li v-else class="nav-item" role="presentation">
                <button class="nav-link disabled" @click="goToRequest()" id="cuttings-tab" type="button" role="tab" aria-controls="cuttings" aria-selected="false">CUTTINGS NOT AVAILABLE</button>
            </li>
        </ul>
      </div>
    </div>
  </div>
</div>

</template>

<script>

export default {
    name: "snake-modal",
    data: function () {
        return {
        cuttingsAvailable: false
        }
    },
    methods: {
    goToRequest() {
      let route = this.$router.resolve({ path: "/plants/request" });
      window.open(route.href);
    },
  }
}

</script>
