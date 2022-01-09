<template lang="html">
    <transition name="slide">
        <Toast v-if="showSuccessToast" :message="message" :success="true" />
    </transition>
    <transition name="slide">
        <Toast v-if="showFailToast" :message="message" :fail="true" />
    </transition>

    <div class="locked" v-if="!pageProtectedPassed">
        <div class="passwordLockBox">
            <router-link to="/"><img class="logo" src="@/assets/images/star-logo.png" width="80" style="opacity: 0.5"></router-link>
            <form @submit.prevent="validate()">
                <input type="text" class="form-control mb-3" v-model="username" placeholder="Username">
                <input type="password" class="form-control mb-4" v-model="password" v-on:keyup.enter="submit" placeholder="Password">
                <input type="submit" value="Send" class="btn" style="color: var(--theme-white); background: var(--theme-primary-dark); width: 150px;"/>
            </form>
        </div>
    </div>
    
    <div v-if="pageProtectedPassed">
        <div id="body" style="text-align: center; padding: 0 30px" class="fade-in">
            <h1>Admin Dashboard</h1>
        </div>
    </div>

</template>

<script lang="js">

import Toast from "@/components/Toast"

export default {
    name: 'AdminDashboard',
    components: {
        Toast
    },
    data(){
        return {
            pageProtectedPassed: false,
            username: '',
            password: '',
            showSuccessToast: false,
            showFailToast: false,
            message: '',
        };
    },
    methods: {
        validate(){
            if ((this.password == 'daniel-online') && (this.username == 'admin')){
                this.message = 'Login Successful';
                setTimeout(() => { this.triggerToast('success'); }, 500 );
                setTimeout(() => { this.pageProtectedPassed = true; }, 1000 );
            }
            else{
                this.message = 'Login Failed';
                this.triggerToast('fail');
            }
        },
        triggerToast(mode) {
            if (mode == 'success'){
                this.showSuccessToast = true;       
            }     
            else {
                this.showFailToast = true;
            }

            setTimeout(() => this.showSuccessToast = false, 10000);
            setTimeout(() => this.showFailToast = false, 5000);
        },
    }
}

</script>

<style scoped>
    .locked{
        position: absolute;
        z-index: 80;
        width: 100%;
        height: 100vh;
        background: rgba(0,0,0,0.9);
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
        flex-direction: column;
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
</style>