<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="epipremnumModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Epipremnum</h3>
      </div>
      <div class="plant-modal-body">
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="default" data-bs-toggle="tab" data-bs-target="#defaultPothos" type="button" role="tab" aria-controls="default" aria-selected="false"><i class="fas fa-leaf"></i></button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="cebublue-tab" data-bs-toggle="tab" data-bs-target="#cebu-blue" type="button" role="tab" aria-controls="cebu-blue" aria-selected="false">Cebu Blue</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="golden-tab" data-bs-toggle="tab" data-bs-target="#golden" type="button" role="tab" aria-controls="golden" aria-selected="true">Golden</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="jade-tab" data-bs-toggle="tab" data-bs-target="#jade" type="button" role="tab" aria-controls="jade" aria-selected="true">Jade</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="marblequeen-tab" data-bs-toggle="tab" data-bs-target="#marble-queen" type="button" role="tab" aria-controls="marble-queen" aria-selected="false">Marble Queen</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="njoy-tab" data-bs-toggle="tab" data-bs-target="#njoy" type="button" role="tab" aria-controls="njoy" aria-selected="false">N'Joy</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="neon-tab" data-bs-toggle="tab" data-bs-target="#neon" type="button" role="tab" aria-controls="neon" aria-selected="false">Neon</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="pearlsnjade-tab" data-bs-toggle="tab" data-bs-target="#pearlsnjade" type="button" role="tab" aria-controls="pearlsnjade" aria-selected="false">Pearls &amp; Jade</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="defaultPothos" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container" style="margin-top: 12px">
                    <img style="width: 35%" src="@/assets/images/plants/pothos1-cropped.jpeg">
                </div>
                <div class="content">
                    <p>The epipremnum is one of the greatest plants alive. They thrive not being cared for at all - in fact, the plant will more than quadrouple in size! Don't feed it, water it.. DON'T EVEN LOOK AT IT! You won't regret it, and the plant will definiately thank you! The plant is green, likes sun, but can live in the dark - Even surviving from basic overhead lighting!</p>
                </div>
            </div>
            <div class="tab-pane fade" id="golden" role="tabpanel" aria-labelledby="golden-tab">
                golden
            </div>
            <div class="tab-pane fade" id="cebu-blue" role="tabpanel" aria-labelledby="cebublue-tab">
                cebu blue
            </div>
            <div class="tab-pane fade" id="marble-queen" role="tabpanel" aria-labelledby="marblequeen-tab">
                marble queen
            </div>
            <div class="tab-pane fade" id="njoy" role="tabpanel" aria-labelledby="njoy-tab">
                n'joy
            </div>
            <div class="tab-pane fade" id="neon" role="tabpanel" aria-labelledby="neon-tab">
                neon
            </div>
            <div class="tab-pane fade" id="pearlsnjade" role="tabpanel" aria-labelledby="pearlsnjade-tab">
                pearls n jade
            </div>
            <div class="tab-pane fade" id="jade" role="tabpanel" aria-labelledby="jade-tab">
                jade
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
    name: "epipremnum-modal",
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
