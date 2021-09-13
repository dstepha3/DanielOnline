<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="palmsModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Palms</h3>
      </div>
      <div class="plant-modal-body">
          <div class="content">
            <p>Palms are pretty. I love it.</p>
          </div>
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="majesty-tab" data-bs-toggle="tab" data-bs-target="#majesty" type="button" role="tab" aria-controls="majesty" aria-selected="false">Majesty</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="parlor-tab" data-bs-toggle="tab" data-bs-target="#parlor" type="button" role="tab" aria-controls="parlor" aria-selected="true">Parlor</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="ponytail-tab" data-bs-toggle="tab" data-bs-target="#ponytail" type="button" role="tab" aria-controls="ponytail" aria-selected="true">PonyTail</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="default" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container" style="margin-top: 5px">
                    <img src="@/assets/images/plants/palm2.jpg">
                </div>
            </div>
            <div class="tab-pane fade" id="majesty" role="tabpanel" aria-labelledby="majesty-tab">
                Majesty
            </div>
            <div class="tab-pane fade" id="parlor" role="tabpanel" aria-labelledby="parlor-tab">
                Parlor
            </div>
            <div class="tab-pane fade" id="ponytail" role="tabpanel" aria-labelledby="ponytail-tab">
                PonyTail
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
    name: "palm-modal",
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
