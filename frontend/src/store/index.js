import { createStore } from "vuex";

export default createStore({
  state: {
    adminUsername: 'admin',
    adminPassword: 'daniel-online',
    adminAuthPassed: false,
    pageAuthSuccessMessage: 'Access Approved!',
    pageAuthFailMessage: 'Access Denied.',
    pageLogoutMessage: 'Goodbye.',
    toastMessage: null,
    toastMode: null,
  },
  mutations: {
    togglePagePermission(state){
        state.pageProtectedPassed = !state.pageProtectedPassed;
        state.toastMode = 'success';
        state.toastMessage = 'Access Approved!';
    },
    toggleAdminPermission(state){
        state.adminAuthPassed = !state.adminAuthPassed;
        state.toastMode = 'fail';
        state.toastMessage = 'Access Denied.';
    },
    logout(state){
        state.adminAuthPassed = false;
        state.toastMode = 'primary';
        state.toastMessage = 'Goodbye.';
    },
  }
});