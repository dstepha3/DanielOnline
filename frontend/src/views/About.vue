<template lang="html">
    <NavBar></NavBar>
    <div id="about-body" class="fade-in">
        <div class="container">

          <div class="top-info flex">
            <div class="img-container">
              <img src="@/assets/images/About/grad_headshot.jpg">
            </div>
            <div style="flex-basis: 70%">
              <h3>Daniel A. Stephan II</h3>
              <p class="personal-details">
                <span class="red">Frontend Web Developer</span> | 
                <span class="red">26 years</span> | 
                <span class="red">Massillon, Ohio</span>
              </p>
              <div class="justify">
                <p>My name is Daniel Stephan. I graduated from Kent State University in 2021 with my Bachelor's of Computer Science concentrated in Information Security. I am currently an SEO Frontend Web Developer at Outerbox Solutions in Copley, Ohio. I was previously employed at East of Chicago Pizza as a General Manager. I've also worked several years as an STNA in long-term care nursing facilities.</p>
                <p>You can find more indepth information below or check out my <router-link class="link" to="faqs">FAQ page</router-link> to learn more. Alternatively, you can download my resume <a class="link" href="/">here</a>.</p>
              </div>
            </div>
          </div>

          <nav>
            <div class="nav nav-tabs about" id="nav-tab" role="tablist">
              <button class="nav-link active" id="nav-skills-tab" data-bs-toggle="tab" data-bs-target="#nav-skills" type="button" role="tab" aria-controls="nav-skills" aria-selected="true">Skills</button>
              <button class="nav-link" id="nav-education-tab" data-bs-toggle="tab" data-bs-target="#nav-education" type="button" role="tab" aria-controls="nav-education" aria-selected="false">Education</button>
              <button class="nav-link" id="nav-experience-tab" data-bs-toggle="tab" data-bs-target="#nav-experience" type="button" role="tab" aria-controls="nav-experience" aria-selected="false">Experience</button>
            </div>
          </nav>

          <div class="tab-content" id="nav-tabContent">

            <div class="tab-pane fade show active" id="nav-skills" role="tabpanel" aria-labelledby="nav-skills-tab">
              <div class="skills">
                <div class="heading">
                    <i style="margin-bottom: 20px" class="fa fa-certificate"></i>
                    <h2>Skills</h2>
                </div>
                <div class="flex">
                    <div class="contained">
                        <i class="fa fa-code"></i>
                        <h6>Frontend</h6>
                        <p>HTML5</p>
                        <p>CSS &bull; SCSS</p>
                        <p>JavaScript</p>
                        <p>VueJS</p>
                    </div>
                    <div class="contained">
                        <i class="fa fa-microchip"></i>
                        <h6>Software</h6>
                        <p>Windows &bull; Mac &bull; Linux</p>
                        <p>Visual Studio Code &bull; XCode</p>
                        <p>Terminal</p>
                        <p>VMWare &bull; Git/Github</p>
                        <p>SSH &bull; FTP &bull; Bash</p>
                    </div>
                    <div class="contained">
                        <i class="fa fa-database"></i>
                        <h6>Backend</h6>
                        <p>C &bull; C++</p>
                        <p>Python</p>
                        <p>Flask</p>
                        <p>mySQL</p>
                    </div>
                  </div>
              </div>
            </div>

            <div class="tab-pane fade" id="nav-education" role="tabpanel" aria-labelledby="nav-education-tab">
              <div class="heading education">
                <i class="fa fa-graduation-cap"></i>
                <h2>Education</h2>
              </div>

<div id="carouselEducation" class="carousel slide" data-bs-ride="carousel" data-bs-interval="0" >
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselEducation" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Bachelors"></button>
    <button type="button" data-bs-target="#carouselEducation" data-bs-slide-to="1" aria-label="Associates"></button>
    <button type="button" data-bs-target="#carouselEducation" data-bs-slide-to="2" aria-label="High School Diploma"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active" >
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="bachelors education">
          <div class="align-left">
              <h3>Bachelor's of Computer Science</h3>
              <div class="degree-info">
                  <p class="concentration">Concentrated in Information Security</p>
                  <p class="location">Class of 2021 &bull; <span class="kent">Kent State University</span> &bull; Kent, Ohio</p>
              </div>
          </div>
          <div class="gpa-and-awards flex align-center">
              <div class="left">
                  <h6>GPA</h6>
                  <p class="GPA">3.210</p>
                  <p class="GPA-Detail">cumulative</p>
                  <p class="GPA">3.654</p>
                  <p class="GPA-Detail">major</p>
              </div>
              <div class="right">
                  <div>
                      <h6>Awards &amp; Honors</h6>
                  </div>
                  <p class="Awards">Dean's List</p>
                  <p class="Awards-Detail">Fall 2019 <span style="color: var(--theme-black)">&bull;</span> Spring 2020</p>
                  <p class="Awards-Detail">Fall 2020</p>
              </div>
          </div>
          <div class="align-center">
              <h6>Relevant Course Work</h6>
              <div class="coursework flex">
                  <div class="left">
                      <p>Software Engineering</p>
                      <p>Digital Forensics</p>
                  </div>
                  <div class ="right">
                      <p>Web Programming</p>
                      <p>Intro to Database Systems</p>
                  </div>
              </div>
              <button type="button" class="btn all-course-work" data-bs-toggle="modal" data-bs-target="#courseworkModal">
                  View All Coursework
              </button>
            </div>
        </div>
      </div>
    </div>
    <div class="carousel-item" >
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="associates education flex">
          <div class="align-left" style="flex-basis: 60%; margin-right: 60px">
              <h3>Associates's of Science</h3>
              <div class="degree-info">
                  <p class="location">Class of 2019 &bull; <span class="fairless">Kent State University</span> &bull; North Canton, Ohio</p>
              </div>
          </div>
          <div class="align-center" style="flex-basis: 40%; margin-left: 30px">
              <h6 style="margin-top: -15px">GPA</h6>
              <p class="GPA">2.757</p>
          </div>
        </div>
      </div>
    </div>
    <div class="carousel-item">
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="diploma education flex">
          <div class="align-left" style="flex-basis: 60%; margin-right: 60px">
              <h3>High School Diploma</h3>
              <div class="degree-info">
                  <p class="location">Class of 2013 &bull; <span class="fairless">Fairless High School</span> &bull; Navarre, Ohio</p>
              </div>
          </div>
          
          <div class="align-center" style="flex-basis: 40%; margin-left: 30px">
              <h6 style="margin-top: -15px">GPA</h6>
              <p class="GPA">3.600</p>
          </div> 
        </div>
      </div>
    </div>
  </div>

  <button class="carousel-control-prev" type="button" data-bs-target="#carouselEducation" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>

  <button class="carousel-control-next" type="button" data-bs-target="#carouselEducation" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>        
            
            </div>

            <div class="tab-pane fade" id="nav-experience" role="tabpanel" aria-labelledby="nav-experience-tab" style="margin-bottom: 40px;">
              <div class="experience">
                  <div class="heading">
                      <i style="margin-bottom: 20px" class="fa fa-certificate"></i>
                      <h2>Experience</h2>
                  </div>

<div id="carouselExperience" class="carousel slide" data-bs-ride="carousel" data-bs-interval="0" >
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExperience" data-bs-slide-to="0" class="active" aria-current="true" aria-label=""></button>
    <button type="button" data-bs-target="#carouselExperience" data-bs-slide-to="1" aria-label=""></button>
    <button type="button" data-bs-target="#carouselExperience" data-bs-slide-to="2" aria-label=""></button>
    <button type="button" data-bs-target="#carouselExperience" data-bs-slide-to="3" aria-label=""></button>
    <button type="button" data-bs-target="#carouselExperience" data-bs-slide-to="4" aria-label=""></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active" >
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
          <div class="jobs-container">
            <div class="job align-left">
                <h5 style="margin-bottom: 5px;">OuterBox Solutions</h5>
                <p>SEO Frontend Web Developer &bullet; <span class="dark-red">Copley, Ohio</span></p>
                <p class="dates">June 2021 - <em>present</em></p>
            </div>
          </div>
      </div>
    </div>
    <div class="carousel-item" >
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="jobs-container">
          <div class="job align-left">
              <h5>East of Chicago Pizza</h5>
              <p>General Manager &bullet; <span class="dark-red">Massillon, Ohio</span></p>
              <p class="dates">August 2016 - June 2021</p>
              <ul>
                <li>Ensure employees perform a variety of tasks</li>
                <li>Prepare food and package for distribution</li>
                <li>Stock supplies and order inventory</li>
                <li>Charging customers for purchases</li>
                <li>Money handling, credit cards and POS use</li>
                <li>Greet customers and problem solve complaints.</li>
                <li>Delivery Driver experience</li>
              </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="carousel-item">
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="jobs-container">
          <div class="job align-left">
              <h5>Amherst Meadows Care Center</h5>
              <p>State Tested Nursing Assistant &bullet; <span class="dark-red">Massillon, Ohio</span></p>
              <p class="dates">November 2017 - November 2018</p>
              <ul>
                <li>Assists with direct patient care under the supervision of the RN or other medical professionals.</li>
                <li>Provide patients with help walking, exercising, and moving in and out of bed.</li>
                <li>Position, feed, bathe, dress and assist patients with grooming and other tasks.</li>
                <li>Observe patients' conditions, measure and record food and liquid intake and output and vital signs, and report changes to professional staff.</li>
              </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="carousel-item">
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="jobs-container">
          <div class="job align-left">
              <h5>Brewster Parke Senior Living Community</h5>
              <p>State Tested Nursing Assistant &bullet; <span class="dark-red">Brewster, Ohio</span></p>
              <p class="dates">April 2015 - July 2016</p>                                
              <ul>
                <li>Assists with direct patient care under the supervision of the RN or other medical professionals.</li>
                <li>Provide patients with help walking, exercising, and moving in and out of bed.</li>
                <li>Position, feed, bathe, dress and assist patients with grooming and other tasks.</li>
                <li>Observe patients' conditions, measure and record food and liquid intake and output and vital signs, and report changes to professional staff.</li>
              </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="carousel-item">
      <div class="carousel-caption d-none d-md-block" style="margin-top: 20px;">
        <div class="jobs-container">
          <div class="job align-left">
              <h5>Hospitality House</h5>
              <p>State Tested Nursing Assistant &bullet; <span class="dark-red">Massillon, Ohio</span></p>
              <p class="dates">July 2012 - February 2015</p>                                
              <ul>
                <li>Assists with direct patient care under the supervision of the RN or other medical professionals.</li>
                <li>Provide patients with help walking, exercising, and moving in and out of bed.</li>
                <li>Position, feed, bathe, dress and assist patients with grooming and other tasks.</li>
                <li>Observe patients' conditions, measure and record food and liquid intake and output and vital signs, and report changes to professional staff.</li>
              </ul>
          </div>
        </div>
      </div>
    </div>
  </div>

  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExperience" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>

  <button class="carousel-control-next" type="button" data-bs-target="#carouselExperience" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div> 

              </div>
            </div>
          </div>
        </div>
    </div>
    <FooterLarge style="margin-top: 120px"></FooterLarge>
    <courseworkModal></courseworkModal>
</template>

<script lang="js">
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";
import courseworkModal from "@/components/Modals/About/Coursework-modal.vue";

export default {
    name: 'about',
    components: {
        NavBar,
        FooterLarge,
        courseworkModal
    },
    methods: {
        scrollToElement(elementRef) {
            elementRef.scrollIntoView({ behavior: "smooth", block: "start" });
        },
        downloadResume: () => {
            window.open('https://drive.google.com/file/d/1hvYlA2TQjh-5ExP_3pLJYxC9USZZfMGT/view?usp=sharing');
        }
    }
}

</script>

<style scoped>
#about-body .flex {
  display: flex;
}

#about-body .content .flex {
  justify-content: space-around;
  margin: 0 0 20px;
}

#about-body  .top-info {
  border: 3px solid var(--theme-primary-dark);
  height: 100%;
  display: flex;
  align-items: center;
  text-align: left;
  padding: 60px;
  margin: 40px 0;
}

#about-body .top-info .img-container{
  flex-basis: 30%;
  margin-right: 60px;
}

#about-body .top-info img {
  width: 100%;
  object-fit: cover;
  object-position: center;
  border-radius: 15%;
  border: 2px solid var(--theme-primary-dark);
}

  #about-body p {
    color: var(--theme-white);
  }

  #about-body .red {
    color: var(--theme-primary-light);
  }

  #about-body p > span.red:nth-child(2) {
    padding-right: 15px;
    padding-left: 15px;
  }

  #about-body p > span.red:first-child {
    padding-right: 15px;
  }
  #about-body p > span.red:last-child {
    padding-left: 15px;
  }

  #about-body .personal-details {
    margin: 0 0 20px;
  }
  #about-body .justify {
    text-align: justify;
  }

  #carouselEducation .carousel-item{
    min-height: 800px;
    background:none;
    transition: none;                
  }
  #carouselExperience .carousel-item{
    min-height: 525px;
    background:none;
    transition: none;                
  }
  .carousel-caption{
    bottom: unset;
    top: 0;
  }
  .carousel-control-next, .carousel-control-prev{
    align-items: flex-start;
    top: -120px;
  }
  .carousel-control-next {
    justify-content: flex-end;
  }
  .carousel-control-prev{
    justify-content: flex-start;
  }
  .tab-pane{
    margin: 60px 0;
  }
  .nav-tabs{
    border-bottom: 1px solid var(--theme-primary-dark)
  }
  .nav-tabs .nav-item .nav-link, .nav-tabs .nav-link {
    color: var(--theme-primary-dark);
    font-family: var(--title);
    font-size: 30px;
    padding: 7px 60px 0;
    margin: 0 30px;
    cursor: pointer;
  }
  .nav-tabs .nav-item .nav-link:hover, .nav-tabs .nav-link:hover {
    color: var(--theme-primary-light);
    cursor: pointer;
    border: 1px solid var(--theme-primary-dark);
    border-bottom: none;
  }

  .nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
    color: var(--theme-primary-light);
    background-color: #0d0d0d;
    border-color: var(--theme-primary-dark);
    border-bottom: none;
    cursor: default;
  }
  .nav.about{
    justify-content: space-evenly;
  }

  #about-body .content {
    padding: 60px;
  }

  #about-body .content h1 {
    font-size: 80px !important;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--theme-black );
    color: var(--theme-lightest-gray);
    margin-bottom: 20px;
  }




  #about-body  .top-info h3{
    color: var(--theme-lightest-gray);
    margin-bottom: 0;
  }

  #about-body h2 {
    color: var(--theme-lightest-gray);
    padding: 0;
    padding: 0 20px;
    margin-bottom: 40px;
    border-bottom: 1px solid var(--theme-black);
    display: inline-block;
  }

  #about-body .job-title {
    color: var(--theme-primary-light);
    opacity: .8;
  }



  #about-body .content .row {
    padding-bottom: 40px;
    border-bottom: 1px solid var(--theme-black );
    margin-bottom: 40px;
  }

  #about-body .content > .row:last-child {
    border: none;
  }

  #about-body .contained {
    border: 1px solid var(--theme-primary-dark);
    padding: 30px 20px;
    flex-basis: 33%;
    max-height: 97%;
    text-align: center;
  }

  #about-body h5 {
    color: var(--theme-primary-dark);
  }

  #about-body  h6 {
    color: var(--theme-primary-dark);
    margin: 20px 0 20px;
    border-bottom: 1px solid var(--theme-black);
  }

  #about-body .contained p {
    font-size: 14px !important;
  }

  #about-body i {
    color: var(--theme-primary-light);
    font-size: 32px;
  }

  #about-body .heading {
    text-align: center;
  }

  #about-body  .heading i {
    color: var(--theme-primary-dark);
    margin-bottom: 10px;
    font-size: 48px;
    display: block;
  }

  #about-body .flex > .contained:nth-child(2){
    margin: 0 30px;
  }






  #about-body .education h3 {
    color: var(--theme-primary-dark);
    margin-bottom: 0;
    font-size: 50px !important;
    line-height: .7;
  }

  #about-body .education .degree-info {
     color: var(--theme-white);
     line-height: .5;
     margin: 10px 0;
     display: inline-block;
  }

  #about-body .education .concentration{
     color: var(--theme-white);
     margin-bottom: 20px;
     font-size: 20px !important;
  } 

  #about-body .education .year {
    color: var(--theme-darkest-gray);
    margin-bottom: 20px;
  }

  #about-body .education .GPA,
  #about-body .education .Awards {
    color: var(--theme-white);
    font-size: 28px !important;
    line-height: .9;
    margin-bottom: 10px;
  }

  #about-body .education .GPA-Detail,
  #about-body .education .Awards-Detail {
    color: var(--theme-warning-dark);
    font-size: 18px !important;
    line-height: .9;
    margin-top: 5px;
    margin-bottom: 30px;
    text-transform: uppercase;
  }
  .gpa-and-awards  {
    margin: 40px 0;
  }
  .gpa-and-awards .left, .gpa-and-awards .right,
  .coursework .left, .coursework .right{
    flex-basis: 50%;
    margin: 0 60px;
  }

  #about-body .education .Awards-Detail {
    margin: 10px 0 !important;
  }

  #about-body .education .all-course-work {
    margin-top: 60px;
    color: var(--theme-warning-dark);
    line-height: .5;
    font-family: var(--text);
  }
  #about-body .education .all-course-work:hover {
    color: var(--theme-warning-light);
    line-height: .5;
    font-family: var(--text);
  }

  #about-body .education hr {
    margin: 60px auto;
    color: var(--theme-darkest-gray);
    width: 85%;
  }

  #about-body .education .location {
    line-height: .1;
    font-size: 14px !important;
    margin-bottom: 30px;
  }

  #about-body .kent,
  #about-body .fairless {
    color: var(--theme-warning-dark);
  }

  .experience h5 {
    line-height: 0.7;
    margin-bottom: 5px;
  }

.experience {
  margin: 20px 0;
}

  .experience .job {
    margin: 60px 0;
  }

  .job p {
    margin-bottom: 0;
  }

  div.job:nth-child(1){
    margin-top: 0;
  }

  .job ul {
    margin-top: 20px;
    font-size: 16px !important;
    padding-left: 0;
    color: var(--theme-white);
    list-style-type: none;
    list-style-position: inside;
    
  }

  .job ul li {
    margin-bottom: 15px;
    border-left: 1px solid var(--theme-warning-dark);
    padding-left: 15px;
  }

  .job ul li::marker {
    font-size: 10px;
  }

  .job .dates {
    color: var(--theme-darkest-gray) !important;
  }

  .job ul > li:last-child{
    padding-bottom: 0;
  }

  .dark-red {
    color: var(--theme-warning-dark);
  }

  @media screen and (max-width: 768px){
    #about-body .flex {
        display: block;
    }

    #about-body  top-info h3{
        font-size: 45px !important;
    }

    #about-body .content {
        padding: 60px 20px;
    }


    #about-body .content .row .flex > .contained:nth-child(2){
        margin: 30px 0;
    }

    #about-body .education h3 {
        line-height: .8;
    }

    #about-body .education .degree-info {
        line-height: 1.2;
    }

    #about-body .education .concentration{
        color: var(--theme-white);
        margin-bottom: 20px;
        font-size: 20px !important;
    } 

    #about-body .education .year {
        color: var(--theme-darkest-gray);
        margin-bottom: 20px;
    }

    #about-body .education .GPA,
    #about-body .education .Awards {
        color: var(--theme-white);
        font-size: 28px !important;
        line-height: .9;
        margin-bottom: 0;
    }

    #about-body .education .GPA-Detail,
    #about-body .education .Awards-Detail {
        color: var(--theme-warning-dark);
        font-size: 18px !important;
        line-height: .9;
        margin-top: 5px;
        margin-bottom: 30px;
        text-transform: uppercase;
    }


    #about-body .education .all-course-work {
        line-height: 1;
    }

    #about-body .course-work .left {
        margin-right: 0;
    }

    #about-body .course-work .right {
        margin-top: 20px;
        margin-left: 0;
    }

    #about-body .gpa-and-awards .left{
        margin-right: 0;
        margin-bottom: 40px;
    }
    #about-body .gpa-and-awards .right{
        margin-top: 40px;
        margin-bottom: 40px;
        margin-left: 0;
    }

    #about-body .education .location {
        line-height: 1.2;
        font-size: 14px !important;
        margin-bottom: 30px;
    }




}
</style>