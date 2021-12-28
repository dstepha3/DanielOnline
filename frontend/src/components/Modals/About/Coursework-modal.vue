<template lang="html">

<!-- Modal -->
<div class="modal fade" id="courseworkModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-xl modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h3 style="display:block" class="modal-title" id="staticBackdropLabel">ALL COURSE WORK</h3>
        <div class="flex" style="margin-top: 5px">
            <a v-if="!isLoadingCore && !loadingCoreError" href="#kentCoreContainer" style="margin-right: 20px;">Kent Core</a>
            <a v-if="!isLoadingMajor && !loadingMajorError" href="#majorCoursesContainer" style="margin-left: 20px;">Major Courses</a>
            <div id="loading-container" v-if="isLoadingMajor && !loadingMajorError && isLoadingCore && !loadingCoreError">
                <div id="render-spiner-container" style="margin-top: 0;">
                    <div class="spinner-border" id="render-spinner" style="color: #e6b800;" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
            </div>
        </div>
        <a href="http://www.kent.edu/"><div class="lightning-bolt"></div></a>
      </div>
      <div class="modal-body">
            <div id="kentCoreContainer">
                <h5>Kent Core</h5>
                <table class="table table-striped" v-if="!loadingCoreError && !isLoadingCore">
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
                <p class="error-message" v-if="loadingCoreError && !isLoadingCore ">Unable to Load Courses</p>
                <div id="loading-container" v-if="isLoadingCore && !loadingCoreError">
                    <div id="render-spiner-container">
                        <div class="spinner-border" id="render-spinner" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <p id="loadingtext">Gathering Courses</p>
                    </div>
                </div>
            </div>
            <div id="majorCoursesContainer">
                <h5>Major Courses</h5>
                <table class="table table-striped" v-if="!loadingMajorError && !isLoadingMajor">
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
                <p class="error-message" v-if="loadingMajorError && !isLoadingMajor">Unable to Load Courses.</p>
                <div id="loading-container" v-if="isLoadingMajor && !loadingMajorError">
                    <div id="render-spiner-container">
                        <div class="spinner-border" id="render-spinner" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <p id="loadingtext">Gathering Courses</p>
                    </div>
                </div>
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


export default {
    name: "coursework-modal",
    data() {
        return {
            kentCoreCourses: 
            [
    {
        'course': 'US 10097',
        'title': 'Destination Kent State: First Year Experience', 
        'grade': 'B',
        'credits': '1',
        'term': 'Fall 2013'
    },
    {
        'course': 'ENG 11011',
        'title': 'College Writing I', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2018'
    },
    {
        'course': 'ENG 21011',
        'title': 'College Writing II', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Spring 2019'
    },
    {
        'course': 'CS 10051',
        'title': 'Intro to Computer Science', 
        'grade': 'A',
        'credits': '4',
        'term': 'Spring 2018'
    },
    {
        'course': 'HIST 11051',
        'title': 'Modern World History', 
        'grade': 'B',
        'credits': '3',
        'term': 'Spring 2018'
    },
    {
        'course': 'HIST 12071',
        'title': 'Modern America', 
        'grade': 'C',
        'credits': '3',
        'term': 'Fall 2018'
    },
    {
        'course': 'THEA 11000',
        'title': 'The Art of Theatre', 
        'grade': 'C',
        'credits': '3',
        'term': 'Spring 2014'
    },
    {
        'course': 'PSYC 11761',
        'title': 'General Psychology', 
        'grade': 'C',
        'credits': '3',
        'term': 'Fall 2013'
    },
    {
        'course': 'SOC 12050',
        'title': 'Introduction to Sociology', 
        'grade': 'D',
        'credits': '3',
        'term': 'Spring 2014'
    },
    {
        'course': 'BSCI 20020',
        'title': 'Biological Structure and Function', 
        'grade': 'B',
        'credits': '5',
        'term': 'Fall 2013'
    },
    {
        'course': 'BSCI 20021',
        'title': 'Basic Microbiology', 
        'grade': 'B-',
        'credits': '3',
        'term': 'Fall 2014'
    },
    {
        'course': 'CHEM 10050',
        'title': 'Fundamentals of Chemistry', 
        'grade': 'C-',
        'credits': '3',
        'term': 'Fall 2013'
    },
    {
        'course': 'NURS 10050',
        'title': 'Intro to Professional Nursing', 
        'grade': 'A',
        'credits': '1',
        'term': 'Spring 2014'
    },
    {
        'course': 'MATH 11009',
        'title': 'Modeling Algebra', 
        'grade': 'D+',
        'credits': '4',
        'term': 'Fall 2013'
    },
    {
        'course': 'MATH 11010',
        'title': 'Algebra For Calculus', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2018'
    },
    {
        'course': 'MATH 11022',
        'title': 'Trigonometry', 
        'grade': 'C+',
        'credits': '3',
        'term': 'Spring 2019'
    },
    {
        'course': 'SPAN 18201',
        'title': 'Elementary Spanish I', 
        'grade': 'C',
        'credits': '4',
        'term': 'Spring 2018'
    },
    {
        'course': 'SPAN 18202',
        'title': 'Elementary Spanish II', 
        'grade': 'B+',
        'credits': '4',
        'term': 'Fall 2018'
    }
],
            majorCourses: 
            [
    {
        'course': 'CS 13001',
        'title': 'Computer Science I: Programming / Problem Solving', 
        'grade': 'A',
        'credits': '4',
        'term': 'Spring 2019'
    },
    {
        'course': 'CS 23001',
        'title': 'Computer Science II: Data Structures', 
        'grade': 'A',
        'credits': '4',
        'term': 'Fall 2019'
    },
    {
        'course': 'CS 23022',
        'title': 'Discrete Structures for Computer Science', 
        'grade': 'B-',
        'credits': '3',
        'term': 'Spring 2019'
    },
    {
        'course': 'CS 33007',
        'title': 'Introduction to Database System Design', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 33101',
        'title': 'Structure of Programming Languages', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 33211',
        'title': 'Operating Systems', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2020'
    },
    {
        'course': 'CS 33901',
        'title': 'Software Engineering', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2020'
    },
    {
        'course': 'CS 35101',
        'title': 'Computer Architecture', 
        'grade': 'B+',
        'credits': '3',
        'term': 'Fall 2019'
    },
    {
        'course': 'CS 35201',
        'title': 'Computer Communication Networks', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 44001',
        'title': 'Computer Science III: Programming Patterns', 
        'grade': 'YD',
        'credits': '4',
        'term': 'Spring 2021'
    },
    {
        'course': 'CS 46101',
        'title': 'Design and Analysis of Algorithms', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2021'
    },
    {
        'course': 'CS 44105',
        'title': 'Web Programming I', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'MATH 12002',
        'title': 'Analytic Geometry and Calculus I', 
        'grade': 'B',
        'credits': '5',
        'term': 'Fall 2019'
    },
    {
        'course': 'MATH 12003',
        'title': 'Analytic Geometry and Calculus II', 
        'grade': 'B-',
        'credits': '5',
        'term': 'Spring 2020'
    },
    {
        'course': 'MATH 22005',
        'title': 'Analytic Geometry and Calculus III', 
        'grade': 'A-',
        'credits': '4',
        'term': 'Summer 2021'
    },
    {
        'course': 'MATH 21001',
        'title': 'Linear Algebra', 
        'grade': 'B+',
        'credits': '4',
        'term': 'Fall 2021'
    },
    {
        'course': 'CS 43203',
        'title': 'Systems Programming', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2021'
    },
    {
        'course': 'CS 47205',
        'title': 'Information Security', 
        'grade': 'A',
        'credits': '3',
        'term': 'Spring 2020'
    },
    {
        'course': 'CS 47207',
        'title': 'Digital Forensics', 
        'grade': 'A',
        'credits': '3',
        'term': 'Fall 2020'
    },
    {
        'course': 'CS 47221',
        'title': 'Introduction to Cryptology', 
        'grade': 'A-',
        'credits': '3',
        'term': 'Fall 2021'
    },
    {
        'course': 'CS 49999',
        'title': 'Capstone Project', 
        'grade': 'A',
        'credits': '4',
        'term': 'Spring 2021'
    },
],
            isLoadingCore: false,
            isLoadingMajor: false,
            loadingCoreError: false,
            loadingMajorError: false,
        };
    }
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
    animation: fadeIn 0.75s;
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
    padding-bottom: 0 !important;
}
.modal-header .flex a{
    margin: 0;
    color: #e6b800;
    text-decoration: none;
    opacity: 0.5;
    line-height: 1.5;
    margin-bottom: 5px;
    animation: fadeIn 0.75s;
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
.error-message{
    text-align: center;
    margin-top: 5px;
    padding-top: 30px;
    border-top: 1px dashed #e6b800;
    animation: fadeIn 5s;
    color: #003399;
    opacity: 0.80;
}
@keyframes fadeIn {
  0% {opacity:0;}
  100% {opacity:0.80;}
}

#render-spiner-container{
    height: 100%;
    width: 100%;
    background: none;
    position: relative;
    margin-top: 40px;
}
#render-spinner{
    opacity: 0.4;
    color: #003399;
}

#loadingtext{
    color: var(--theme-whitest);
    margin-top: 20px;
    font-size: 10px !important;
    font-weight: 900;
    text-transform: uppercase;
    animation-duration: 2s;
    animation-name: grow;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
    position: absolute;
    top: -11px;
}
#loadingtext:hover{
    cursor: default;
}

#kentCoreContainer::before,
#majorCoursesContainer::before {
  content:"";
  display:block;
  height:50px; /* fixed header height*/
  margin:-50px 0 0; /* negative fixed header height */
}

@keyframes grow {
    0% {
      transform: scale(1);
      opacity: 0.6;
    }
  
    50%{
      transform: scale(1.1);
      opacity: 1;
    }

    100%{
      transform: scale(1);
      opacity: 0.6;
    }
  }

</style>
