<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="zzModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Zanzibar Zamiifolia</h3>
      </div>
      <div class="plant-modal-body">
          <div class="content">
            <p>ZZ's my favvv. </p>
          </div>
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="gem-tab" data-bs-toggle="tab" data-bs-target="#gem" type="button" role="tab" aria-controls="gem" aria-selected="false">Gem</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="raven-tab" data-bs-toggle="tab" data-bs-target="#raven" type="button" role="tab" aria-controls="raven" aria-selected="true">Raven</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="zenzi-tab" data-bs-toggle="tab" data-bs-target="#zenzi" type="button" role="tab" aria-controls="zenzi" aria-selected="true">Zenzi</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="default" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container" style="margin-top: 5px">
                    <img height="287" src="@/assets/images/plants/zz-cropped.jpeg">
                </div>
            </div>
            <div class="tab-pane fade" id="gem" role="tabpanel" aria-labelledby="gem-tab">
                Zanzibar Gem
            </div>
            <div class="tab-pane fade" id="raven" role="tabpanel" aria-labelledby="raven-tab">
                ZZ Raven
            </div>
            <div class="tab-pane fade" id="zenzi" role="tabpanel" aria-labelledby="zenzi-tab">
                ZZ Zenzi
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
    name: "zz-modal",
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
