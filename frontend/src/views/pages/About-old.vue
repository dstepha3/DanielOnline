<template lang="html">
    <NavBar></NavBar>
    <div id="about-body" class="fade-in">
        <div class="container">
            <div class="row">
                <div class="sidebar sticky col-sm-4">
                    <img src="@/assets/images/About/headshot-aug21.jpg">
                    <h3>Daniel A. Stephan II</h3>
                    <p class="job-title">Frontend Web Developer Intern</p>
                    <nav class="jump-section">
                        <p @click="scrollToElement($refs.skills)">Skills</p>
                        <p @click="scrollToElement($refs.education)">Education</p>
                        <p @click="scrollToElement($refs.experience)">Experience</p>
                        <p><span @click="downloadResume">Download Resume</span></p>
                    </nav>
                </div>
                
                <div class="content col-sm-8">
                    <div class="row about">
                        <h1>About Me</h1>
                        <p class="personal-details"><span class="red">26 years</span> | <span class="red">Massillon, Ohio</span></p>
                        <div class="section">
                            <p>My name is Daniel Stephan, and I am a senior at Kent State University seeking my Bachelor's of Computer Science in Information Security. I am currently a SEO Frontend Web Developer Intern at Outerbox Solutions. I was previously employed at East of Chicago as a General Manager. I've also worked several years as an STNA in long-term care nursing facilities.</p>

                            <!-- <p>I am a very detail oriented with a strong sense of leadership. I prefer to work independently, however I am a big team player. Moving forward, I would like to begin my career within the computer industry to continue my education with a more hands on approach. I don't think you would be disappointed to have me on your team.</p>  -->
                        </div> 
                        <a ref="skills"></a> <!-- ref placed her so renders properly -->
                    </div>
                    <div class="row skills">
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
                        <a ref="education"></a> <!-- ref placed her so renders properly -->
                    </div>
                    <div class="row education">
                        <div class="heading education">
                            <i class="fa fa-graduation-cap"></i>
                            <h2>Education</h2>
                        </div>
                            <div class="bachelors" style="margin-top: 20px;">
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
                                        <p class="GPA">3.195</p>
                                        <p class="GPA-Detail">cumulative</p>
                                        <p class="GPA">3.669</p>
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
                            <hr style="margin-bottom: 80px" />
                            <div class="associates flex">
                                <div class="align-left" style="flex-basis: 60%; margin-right: 10px">
                                    <h3>Associates's of Science</h3>
                                    <div class="degree-info">
                                        <p class="location">Class of 2019 &bull; <span class="fairless">Kent State University</span> &bull; North Canton, Ohio</p>
                                    </div>
                                </div>
                                <div class="align-center" style="flex-basis: 40%; margin-left: 10px">
                                    <h6 style="margin-top: -15px">GPA</h6>
                                    <p class="GPA">2.757</p>
                                </div>
                            </div>
                            <hr style="margin-top:40px; margin-bottom: 80px" />
                            <div class="diploma flex">
                                <div class="align-left" style="flex-basis: 60%; margin-right: 10px">
                                    <h3>High School Diploma</h3>
                                    <div class="degree-info">
                                        <p class="location">Class of 2013 &bull; <span class="fairless">Fairless High School</span> &bull; Navarre, Ohio</p>
                                    </div>
                                </div>
                                
                                <div class="align-center" style="flex-basis: 40%; margin-left: 10px">
                                    <h6 style="margin-top: -15px">GPA</h6>
                                    <p class="GPA">3.600</p>
                                </div> 
                            </div>
                        <a ref="experience"></a> <!-- ref placed her so renders properly -->
                    </div>
                    <div class="row experience">
                        <div class="heading">
                            <i style="margin-bottom: 20px" class="fa fa-certificate"></i>
                            <h2>Experience</h2>
                        </div>
                        <div class="jobs-container">
                            <div class="job">
                                <h5 style="margin-bottom: 5px;">OuterBox Solutions</h5>
                                <p>SEO Frontend Web Developer Intern &bullet; <span class="dark-red">Copley, Ohio</span></p>
                                <p class="dates">June 2021 - <em>present</em></p>
                            </div>
                            <div class="job">
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
                            <div class="job">
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
                            <div class="job">
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
                            <div class="job">
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
        </div>
    </div>
    <FooterLarge style="margin-top: 80px"></FooterLarge>
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

  #about-body .sidebar {
    border-left: 3px solid var(--theme-primary-dark);
    border-bottom: 3px solid var(--theme-primary-dark);
    border-right: 3px solid var(--theme-primary-dark);
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 40px;
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

  #about-body .content p {
    color: var(--theme-dark-gray);
  }

  #about-body .content .red {
    color: var(--theme-primary-light);
  }

  #about-body .content p > span.red:first-child {
    padding-right: 15px;
  }

  #about-body .content p > span.red:last-child {
    padding-left: 15px;
  }

  #about-body .sidebar img {
    width: 90%;
    object-fit: cover;
    border-radius: 50%;
    border: 2px solid var(--theme-primary-dark);
    margin-bottom: 20px;
  }

  #about-body .sidebar h3{
    color: var(--theme-lightest-gray);
    margin-bottom: 0;
  }

  #about-body .row h2 {
    color: var(--theme-lightest-gray);
    padding: 0;
    padding: 0 20px;
    margin-bottom: 40px;
    border-bottom: 1px solid var(--theme-black);
    display: inline-block;
  }

  #about-body .jump-section {
    margin-top: 10px;
  }

  #about-body .jump-section p,
  #about-body .jump-section a {
    margin-bottom: 5px;
    padding: 0;
    color: var(--theme-warning-dark);
    font-family: var(--text);
  }

  #about-body .jump-section p:hover,
  #about-body .jump-section a:hover {
    cursor: pointer;
    color: var(--theme-primary-light);
    font-weight: 500;
  }

  #about-body .job-title {
    color: var(--theme-primary-light);
    opacity: .8;
  }

  #about-body .personal-details {
    margin: 20px 0;
  }

  #about-body .content .row {
    padding-bottom: 40px;
    border-bottom: 1px solid var(--theme-black );
    margin-bottom: 40px;
  }

  #about-body .content > .row:last-child {
    border: none;
  }

  #about-body .content .contained {
    border: 1px solid var(--theme-primary-dark);
    padding: 30px 20px;
    flex-basis: 33%;
    max-height: 97%;
    text-align: center;
  }

  #about-body .content h5 {
    color: var(--theme-primary-dark);
  }

  #about-body .content h6 {
    color: var(--theme-primary-dark);
    margin: 20px 0 20px;
    border-bottom: 1px solid var(--theme-black);
  }

  #about-body .content .contained p {
    font-size: 14px !important;
  }

  #about-body .content i {
    color: var(--theme-primary-light);
    font-size: 32px;
  }

  #about-body .content .heading {
    text-align: center;
  }

  #about-body .content .heading i {
    color: var(--theme-primary-dark);
    margin-bottom: 10px;
    font-size: 48px;
    display: block;
  }

  #about-body .content .row .flex > .contained:nth-child(2){
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

  #about-body .education .Awards-Detail {
    margin: 10px 0 !important;
  }

  #about-body .education .all-course-work {
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
    color: var(--theme-dark-gray);
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
    color: var(--theme-black) !important;
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

    #about-body .sidebar h3{
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