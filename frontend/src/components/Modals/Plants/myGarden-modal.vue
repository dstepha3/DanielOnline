<template lang="html">

<!-- Modal -->
<div class="plant modal fade" id="gardenModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">My Garden</h3>
      </div>
      <div class="plant-modal-body">
          <ul class="nav nav-pills mb-3" id="PlantTabs" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="default" data-bs-toggle="tab" data-bs-target="#defaultGarden" type="button" role="tab" aria-controls="default" aria-selected="false"><i class="fas fa-leaf"></i></button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="banana-tab" data-bs-toggle="tab" data-bs-target="#banana" type="button" role="tab" aria-controls="banana" aria-selected="false">Banana</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="banana-pepper-tab" data-bs-toggle="tab" data-bs-target="#banana-pepper" type="button" role="tab" aria-controls="banana-pepper" aria-selected="false">Banana Pepper</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="blackberry-tab" data-bs-toggle="tab" data-bs-target="#blackberry" type="button" role="tab" aria-controls="blackberry" aria-selected="true">Blackberry</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="green-pepper-tab" data-bs-toggle="tab" data-bs-target="#green-pepper" type="button" role="tab" aria-controls="green-pepper" aria-selected="true">Green Pepper</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="mango-tab" data-bs-toggle="tab" data-bs-target="#mango" type="button" role="tab" aria-controls="mango" aria-selected="true">Mango</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="strawberry-tab" data-bs-toggle="tab" data-bs-target="#strawberry" type="button" role="tab" aria-controls="strawberry" aria-selected="true">Strawberry</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="tomato-tab" data-bs-toggle="tab" data-bs-target="#tomato" type="button" role="tab" aria-controls="tomato" aria-selected="true">Tomato</button>
            </li>
        </ul>
        <div class="tab-content" id="TabContent">
            <div class="tab-pane fade show active" id="defaultGarden" role="tabpanel" aria-labelledby="default-tab">
                <div class="image-container">
                    <img style="width: 30%" src="@/assets/images/plants/garden-cropped.jpeg">
                </div>
                <div class="content">
                    <p>My Beautiful Garden.</p>
                </div>
            </div>
            <div class="tab-pane fade" id="banana-pepper" role="tabpanel" aria-labelledby="banana-pepper-tab">
                Banana Pepper
            </div>
            <div class="tab-pane fade" id="blackberry" role="tabpanel" aria-labelledby="blackberry-tab">
                Blackberry
            </div>
            <div class="tab-pane fade" id="strawberry" role="tabpanel" aria-labelledby="strawberry-tab">
                Strawberry
            </div>
            <div class="tab-pane fade" id="tomato" role="tabpanel" aria-labelledby="tomato-tab">
                Tomato
            </div>
            <div class="tab-pane fade" id="banana" role="tabpanel" aria-labelledby="banana-tab">
                Banana
            </div>
            <div class="tab-pane fade" id="mango" role="tabpanel" aria-labelledby="mango-tab">
                Mango
            </div>
            <div class="tab-pane fade" id="green-pepper" role="tabpanel" aria-labelledby="green-pepper-tab">
                Green Pepper
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
            <li v-if="produceAvailable" class="nav-item" role="presentation">
                <button class="nav-link active" @click="goToRequest()" id="produce-tab" type="button" role="tab" aria-controls="produce" aria-selected="false">REQUEST PRODUCE</button>
            </li>
            <li v-else class="nav-item" role="presentation">
                <button class="nav-link disabled" @click="goToRequest()" id="cuttings-tab" type="button" role="tab" aria-controls="produce" aria-selected="false">PRODUCE NOT AVAILABLE</button>
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
        produceAvailable: false
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
