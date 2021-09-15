<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="philoModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Philodenderon</h3>
      </div>
      <div class="plant-modal-body">
          <div class="content">
            <p>Philodenderon's are neat</p>
          </div>
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="birkin-tab" data-bs-toggle="tab" data-bs-target="#birkin" type="button" role="tab" aria-controls="birkin" aria-selected="false">Birkin</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="brasil-tab" data-bs-toggle="tab" data-bs-target="#brasil" type="button" role="tab" aria-controls="brasil" aria-selected="true">Brasil</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="monstera-tab" data-bs-toggle="tab" data-bs-target="#monstera" type="button" role="tab" aria-controls="monstera" aria-selected="true">Monstera Deliciosa</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="scandens-tab" data-bs-toggle="tab" data-bs-target="#scandens" type="button" role="tab" aria-controls="scandens" aria-selected="true">Scandens</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="default" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container" style="margin-top: 5px">
                    <img height="287" src="@/assets/images/plants/plant-placeholder2.png">
                </div>
            </div>
            <div class="tab-pane fade" id="birkin" role="tabpanel" aria-labelledby="birkin-tab">
                Birkin
            </div>
            <div class="tab-pane fade" id="brasil" role="tabpanel" aria-labelledby="brasil-tab">
                Brasil
            </div>
            <div class="tab-pane fade" id="monstera" role="tabpanel" aria-labelledby="monstera-tab">
                Monstera Deliciosa
            </div>
            <div class="tab-pane fade" id="scandens" role="tabpanel" aria-labelledby="scandens-tab">
                Scandens
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
    name: "philo-modal",
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
