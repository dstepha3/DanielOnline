<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="scindapsusModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Scindapsus</h3>
      </div>
      <div class="plant-modal-body">
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="default" data-bs-toggle="tab" data-bs-target="#defaultScind" type="button" role="tab" aria-controls="defaultScind" aria-selected="false"><i class="fas fa-leaf"></i></button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="argyraeus-tab" data-bs-toggle="tab" data-bs-target="#argyraeus" type="button" role="tab" aria-controls="argyraeus" aria-selected="false">Argyraeus</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="exotica-tab" data-bs-toggle="tab" data-bs-target="#exotica" type="button" role="tab" aria-controls="exotica" aria-selected="true">Exotica</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="pictus-tab" data-bs-toggle="tab" data-bs-target="#pictus" type="button" role="tab" aria-controls="pictus" aria-selected="true">Pictus</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="trub-moonlight-tab" data-bs-toggle="tab" data-bs-target="#trub-moonlight" type="button" role="tab" aria-controls="trub-moonlight" aria-selected="true">Treubii Moonlight</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="defaultScind" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container">
                    <img style="width: 35%" src="@/assets/images/plants/plant-placeholder2.png">
                </div>
                <div class="content">
                  <p>Another one of my favs.</p>
                </div>
            </div>
            <div class="tab-pane fade" id="argyraeus" role="tabpanel" aria-labelledby="argyraeus-tab">
                Argyraeus
            </div>
            <div class="tab-pane fade" id="exotica" role="tabpanel" aria-labelledby="exotica-tab">
                Exotica
            </div>
            <div class="tab-pane fade" id="trub-moonlight" role="tabpanel" aria-labelledby="trub-moonlight-tab">
                Treubii Moonlight
            </div>
            <div class="tab-pane fade" id="pictus" role="tabpanel" aria-labelledby="pictus-tab">
                Pictus
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
    name: "scindapsus-modal",
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
