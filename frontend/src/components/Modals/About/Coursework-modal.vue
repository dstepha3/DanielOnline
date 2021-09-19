<template lang="html">

<!-- Modal -->
<div class="modal fade" id="courseworkModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">ALL COURSE WORK</h3>
        <div class="flex">
            <a href="#kentCoreContainer" style="margin-right: 20px;">Kent Core</a>
            <a href="#majorCoursesContainer" style="margin-left: 20px;">Major Courses</a>
        </div>
        <a href="http://www.kent.edu/"><div class="lightning-bolt"></div></a>
      </div>
      <div class="modal-body">
            <div id="kentCoreContainer">
                <h5>Kent Core</h5>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">Course</th>
                            <th scope="col">Title</th>
                            <th scope="col">Grade</th>
                            <th scope="col">Credits</th>
                            <th scope="col">Term</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="hoverRow" v-for="corecourse in kentCoreCourses" :key="corecourse">
                            <td>{{ corecourse.course }}</td>
                            <td>{{ corecourse.title }}</td>
                            <td>{{ corecourse.grade }}</td>
                            <td>{{ corecourse.credits }}</td>
                            <td>{{ corecourse.term }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div id="majorCoursesContainer">
                <h5>Major Courses</h5>
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th scope="col">Course</th>
                            <th scope="col">Title</th>
                            <th scope="col">Grade</th>
                            <th scope="col">Credits</th>
                            <th scope="col">Term</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="hoverRow" v-for="majorcourse in majorCourses" :key="majorcourse">
                            <td>{{ majorcourse.course }}</td>
                            <td>{{ majorcourse.title }}</td>
                            <td>{{ majorcourse.grade }}</td>
                            <td>{{ majorcourse.credits }}</td>
                            <td>{{ majorcourse.term }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="img-container">
                <img width="400" src="@/assets/images/About/kent-state-logo.png">
            </div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
    </div>
  </div>
</div>

</template>

<script>

import axios from 'axios';


export default {
    name: "coursework-modal",
    data() {
        return {
            kentCoreCourses: [],
            majorCourses: [],
            isLoadingCore: false,
            isLoadingMajor: false,
            loadingCoreError: false,
            loadingMajorError: false,
        };
    },
    methods: {
        getKentCore() {
            const path = 'http://localhost:5000/api/courses/kentcore';
            axios.get(path)
                .then((res) => {
                    this.kentCoreCourses = res.data;
                    this.isLoadingCore = false;
                })
                .catch((error) => {
                    console.error(error);
                    this.isLoadingCore = false;
                    this.loadingCoreError = true;
                })
        },
        getMajorCourses() {
            const path = 'http://localhost:5000/api/courses/majorcourses';
            axios.get(path)
                .then((res) => {
                    this.majorCourses = res.data;
                    this.isLoadingMajor = false;
                })
                .catch((error) => {
                    console.error(error);
                    this.isLoadingMajor = false;
                    this.loadingMajorError = true;
                })
        },
        getCourses(){
            this.getKentCore();
            this.getMajorCourses();
        },
    },
    created() {
        this.isLoadingCore = true;
        this.isLoadingMajor = true;
        this.getCourses();
    },
}

</script>

<style scoped>
h5 {
    color: var(--theme-whiter);
    margin-bottom: 0;
    text-align: center;
}
.table {
    --bs-table-bg: var(--theme-blackest);
    --bs-table-striped-color: var(--theme-light-gray);
    --bs-table-striped-bg: #1a1a1a;
    color: var(--theme-light-gray);
    border-color: unset;
    margin-top: 0;
}
.table td {
    padding: 20px .5rem;
}
.table .hoverRow:hover{
    --bs-table-bg: var(--theme-blacker);
    --bs-table-striped-color: var(--theme-blacker);
    color: var(--theme-whitest);
}
#kentCoreContainer {
    margin: 30px 0 80px;
}
#majorCoursesContainer{
    margin: 80px 0 30px;
}
.img-container{
    text-align: center;
    padding: 40px 0;
}
.modal-header{
    border-bottom: 1px solid #e6b800 !important;
}
.modal-header a{
    margin: 0;
    color: #e6b800;
    text-decoration: none;
    opacity: 0.5;
    line-height: 1.5;
    margin-bottom: 5px;
}
.modal-header a:hover{
    opacity: 1;
}
.modal-footer{
    border-top: 1px solid #e6b800 !important;
}
.modal-title {
    color: #003399 !important;
    line-height: 1 !important;
    font-size: 70px !important;
    opacity: 0.7;
}
button.btn-close {
    background-color: #003399 !important;
}
.lightning-bolt{
    background-image: url("data:image/svg+xml,%3Csvg id='Group_51' data-name='Group 51' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 59.071 89.1'%3E%3Cdefs%3E%3Cstyle%3E .cls-1 %7B fill: %23ffcd00; %7D .cls-2 %7B fill: %23fff; %7D %3C/style%3E%3C/defs%3E%3Cpath id='Path_59' data-name='Path 59' class='cls-1' d='M16.917,53.151H6.051L16.917,31.42H6.051L21.659.6h32.8L33.907,28.259H45.563L30.154,48.41h9.878L2.1,82.983Z' transform='translate(2.049 0.585)'/%3E%3Cpath id='Path_60' data-name='Path 60' class='cls-2' d='M54.132,2.568,33.388,30.029H45.044L29.634,50.18H38.92L8.3,78.234,21.139,52.551H10.273L21.139,30.82H10.273L24.7,2.568H54.132ZM59.071,0H22.917l-.79,1.383L7.9,29.634,6.124,33.19H16.99L7.9,51.366,6.124,54.922H16.99L5.927,77.049,0,89.1l9.878-9.088L40.5,52.156l4.741-4.346H34.573L47.02,31.61l3.161-3.951H38.327L56.107,3.951Z'/%3E%3C/svg%3E%0A");
    height: 50px;
    width: 50px;
    background-size: span;
    background-repeat: no-repeat;
    position: absolute;
    right: 50px;
    opacity: 0.5;
    top: 45px;
}
.lightning-bolt:hover{
    opacity: 1;
    cursor: pointer;
    animation: wiggle 2.5s infinite;
}

@keyframes wiggle {
    0% { transform: rotate(0deg); }
   10% { transform: rotate(5deg); }
   20% { transform: rotate(-5deg); }
   30% { transform: rotate(5deg); }
   40% { transform: rotate(-5deg); }
   50% { transform: rotate(5deg); }
   60% { transform: rotate(-5deg); }
   70% { transform: rotate(5deg); }
   80% { transform: rotate(-5deg); }
   90% { transform: rotate(5deg); }
  100% { transform: rotate(0deg); }
}

.flex{
    display: flex;
}

</style>
