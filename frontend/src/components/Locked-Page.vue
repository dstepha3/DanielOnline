<template lang="html">
    <transition name="slide">
        <Toast v-if="showSuccessToast" :message="$store.state.pageAuthSuccessMessage" :success="true" />
    </transition>
    <transition name="slide">
        <Toast v-if="showFailToast" :message="$store.state.pageAuthFailMessage" :fail="true" />
    </transition>

    <transition name="fade">
    <div class="locked" v-if="!$store.state.adminAuthPassed">
        <div class="passwordLockBox">
            <router-link to="/"><img class="logo" src="@/assets/images/star-logo.png" width="80" style="opacity: 0.5"></router-link>
            <p>Enter Password:</p>
            <form @submit.prevent="validate()">
                <input type="password" class="form-control" v-model="password" v-on:keyup.enter="submit">
                <input type="submit" value="Send" class="btn" style="color: var(--theme-white); background: var(--theme-primary-dark); width: 150px;"/>
            </form>
        </div>
    </div>
    </transition>
</template>

<script lang="js">

import Toast from "@/components/Toast"

export default {
    name: 'Locked-Components',
    components: {
        Toast,
    },
    data(){
        return {
            password: '',
            showSuccessToast: false,
            showFailToast: false,
        };
    },
    methods:{
        validate(){
            if (!this.$store.state.adminAuthPassed){
                if (this.password == this.$store.state.adminPassword){
                    setTimeout(() => { this.triggerToast('success'); }, 500 );
                    setTimeout(() => { this.$store.commit('toggleAdminPermission'); }, 1000 );
                }
                else{
                    this.triggerToast('fail');
                }
            }
        },
        triggerToast(mode) {
            if (mode == 'success'){
                this.showFailToast = false;
                this.showSuccessToast = true;       
            }     
            else {
                this.showFailToast = true;
            }

            setTimeout(() => this.showSuccessToast = false, 8000);
            setTimeout(() => this.showFailToast = false, 5000);
        },
    }
}

</script>

<style scoped>

  /**********     LOGIN SPECIFIC, TO REMOVE   ***************/
    .locked{
        position: absolute;
        z-index: 80;
        width: 100%;
        height: 100vh;
        background: rgba(0,0,0,0.95);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .passwordLockBox{
        background: rgba(48, 45, 45, 0.2);
        border: 1px solid rgba(175, 0, 0, 0.4);
        padding: 30px 60px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .passwordLockBox p{
        color: var(--theme-light-gray);
    }
    input.form-control:focus {
        box-shadow: none;
    }
    form{
        display: flex;
        flex-direction: row;
        align-items: center;
        margin-top: 10px;
    }
    form .btn{
        opacity: 0.6;
        padding: 5px 10px;
        margin: 1px 0;
        border-radius: 0;
    }

    .slide-enter-active {
        animation: slide-in .5s;
    }
    .slide-leave-active {
        animation: slide-in .5s reverse;
    }
    @keyframes slide-in {
        0% {
            transform: translateX(300px);
        }
        100% {
            transform: translateX(0);
        }
    }
    .fade-enter-active {
        animation: fade-on 2s;
    }
    .fade-leave-active {
        animation: fade-on 1s reverse;
    }
    @keyframes fade-on {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @media only screen and (max-width: 768px){
      .passwordLockBox{
          margin: 0;
          padding: 60px 45px;
      }
      .passwordLockBox form{
        flex-direction: column;
      }
      .passwordLockBox form .btn{
        margin: 20px 0;
        width: 100% !important;
      }
    }
/******************************************/
</style>