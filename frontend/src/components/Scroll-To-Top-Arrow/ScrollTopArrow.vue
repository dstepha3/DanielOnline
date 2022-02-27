<template>
  <ScrollTopComponent>
    <a class="btn btn-light" 
       data-tooltip="Jump to Top"
       data-tooltip-location="left">
      <i class="fas fa-arrow-up"></i>
    </a>
  </ScrollTopComponent>
</template>

<script>
import ScrollTopComponent from "./ScrollTopComponent";
export default {
  components: {
    ScrollTopComponent,
  },
};
</script>

<style>
.btn {
  border-radius: 50%;
  background-color: rgba(128, 0, 0, 0.9);
  border: 2px solid rgba(128, 0, 0, 0.9);
  line-height: 1;
  animation: fadeIn 0.5s;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
.fas {
  font-size: 22px;
  color: var(--theme-whitest);
  padding: 10px 5px;
}
.fas:hover {
  color: var(--theme-whitest);
}
.btn:hover {
  border: 2px solid rgba(88, 0, 0, 0.9);
  color: var(--theme-whitest);
  background-color: rgba(88, 0, 0, 0.9);
}
@media screen and (max-width: 768px){
  .fas{
    font-size: 15px;
  }
}
</style>