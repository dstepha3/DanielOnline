<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="zzModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">Zanzibar Zamiifolia</h3>
        <button type="button" style="display: inline" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="plant-modal-body">
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="default" data-bs-toggle="tab" data-bs-target="#defaultZZ" type="button" role="tab" aria-controls="default" aria-selected="false"><i class="fas fa-leaf"></i></button>
            </li>
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
            <div class="tab-pane fade show active" id="defaultZZ" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container" style="margin-top: 5px">
                    <img style="width: 50%" src="https://i.imgur.com/dumUrFl.jpg">
                </div>
                <div class="content">
                  <section>
                    <p>If you have a brown thumb, this plant is definitely for you. These plants originate from the hot &amp; dry lands of Africa, so you can image that they thrive from lack of water. You don't have to worry about missing a watering or going out of town for a couple weeks (maybe even months), because this guy will still be kicking by the time you get home.</p>
                    <p>One would think that because these guys are from Africa, they'd enjoy the sun - but it's actually the opposite. No - they won't in a pitch black room and it's pretty recommended that you shouldn't set your ZZ in the direct sun because you'll end up burning them. But ZZ's are able to survive in very low light environments. Their growth will not be as fast compared to if you place it in a higher light area, they won't die and that's a plus.</p>
                    <p>Check out the different varieties of ZZ Plants that I have in the tabs above and learn how to take care of them so you can raise one on your own!</p>
                  </section>
                  <img style="width: 75%" title="ZZ Plants originate from SE Africa" src="https://i.imgur.com/nG3c3uF.png">
                  <div class="info-row">
                    <div class="row">
                      <div class="col align-center">
                        <i class="fas fa-map-marker-alt location"></i>
                        <h4>SE AFRICA</h4>
                        <p>from Southern Kenya<br/> to Northeast South Africa</p>
                      </div>
                      <div class="col align-center">
                        <i class="fas fa-sun light"></i>
                        <div><h4>LOW LIGHT TOLERANT</h4></div>
                        <p>ZZ Plant's can tolerate low light,
                        <br/>but they thrive in bright indirect light</p>
                      </div>
                      <div class="col  align-center">
                        <i class="fas fa-burn water"></i>
                        <h4>DRAUGHT TOLERANT</h4>
                        <p>Water maybe once a month</p>
                        <p>They prefer to dry out completely before you give them a good soaking.</p>
                        <p>Overwater = Root Rot</p>
                      </div>
                      <div class="col align-center">
                        <i class="fas fa-temperature-low temperature"></i>
                        <h4>65° to 79°F</h4>
                        <p>They can survive in <br/>temperatures as low as 59°F</p>
                        <p>Hot temperatures lead to an<br/> increase in leaf production</p>
                      </div>
                    </div>
                  </div>
                  <div class="row cta" style="margin-bottom: 60px !important;">
                      <p>Did you know that the ZZ Plant was given it's established name <em>Zamioculcas zamiifolia</em> by Adolf Hitler?</p>
                      <p style="margin-bottom: 0;">Just kidding, his name was Adolf Engler. But that would have been crazy, huh?</p>
                      <span class="info-icon"><i class="fas fa-info-circle"></i></span>
                  </div>
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
    name: "zz-modal",
    data: function () {
        return {
        cuttingsAvailable: true
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

<style scoped>
.tab-content .content img{
  border-top: none;
  border-bottom: none;
  padding:0;
  margin: 60px auto;
  display:block;
}
.info-row{
  margin: 60px 0;
  padding-top: 60px;
  padding-bottom: 60px;
  border-top: 1px solid var(--theme-light-gray);
  border-bottom: 1px solid var(--theme-light-gray);
}
section{
  padding-bottom: 40px;
  margin-bottom: 60px;
  border-bottom: 1px solid var(--theme-light-gray);
}
.info-row .row > .col:nth-child(2),
.info-row .row > .col:nth-child(3){
  border-left: 1px solid var(--theme-light-gray);
  border-right: 1px solid var(--theme-light-gray);
}
.info-row i{
  font-size: 48px;
}
.info-row p{
  font-size: 15px !important;
}

.info-row .location{
  color: var(--theme-primary-dark);
}
.info-row .light{
  color: #e6b800;
}
.info-row .water{
  color: #003399;
}
.info-row .temperature{
  color: var(--theme-secondary);
}
.info-row .col h4{
  margin: 30px 0 15px;
  color: var(--theme-whitest);
  line-height: 1;
}
.info-row .col p {
  text-align: center;
}
.info-icon{
  position: absolute;
  top: -45px;
  font-size: 55px;
}

.info-icon i{
  background: var(--theme-primary-dark);
  color: var(--theme-blackest);
  border-radius: 50%;
}

.cta{
  position: relative;
}
</style>
