<template lang="html">
    <NavBar></NavBar>
    <div id="about-body">
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
                            <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales velit in ipsum ultrices fringilla. Morbi non sollicitudin enim. Curabitur rhoncus luctus urna, lacinia suscipit massa tempus ut. Vivamus non justo elit. Nulla quis imperdiet ligula, non commodo dolor. Nullam elementum ac enim congue aliquam. Donec ipsum mi, convallis non nibh eget, imperdiet ultricies lectus. Etiam placerat arcu sapien, eu placerat nibh posuere ut. Donec orci neque, tristique eu nunc sit amet, aliquet lacinia ante. Sed tempus enim sit amet lectus sagittis ornare. Vestibulum quis lectus imperdiet felis sodales bibendum. Morbi nec sem urna. Phasellus a lectus et lectus egestas sagittis. Cras egestas facilisis nisi ac porttitor. Etiam iaculis bibendum lacus quis euismod.</p> 
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
                                        <p class="GPA">3.178</p>
                                        <p class="GPA-Detail">cumulative</p>
                                        <p class="GPA">3.667</p>
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
                                    <p class="all-course-work">View All Coursework</p>
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
                                <h5>OuterBox Solutions</h5>
                                <p>WORK</p>
                            </div>
                            <div class="job">
                                <h5>MEOC</h5>
                                <p>WORK</p>
                            </div>
                            <div class="job">
                                <h5>Amherst Meadows</h5>
                                <p>WORK</p>
                            </div>
                            <div class="job">
                                <h5>Brewster Parke</h5>
                                <p>WORK</p>
                            </div>
                            <div class="job">
                                <h5>Hospitality House</h5>
                                <p>WORK</p>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
    <FooterLarge style="margin-top: 80px"></FooterLarge>
</template>

<script lang="js">
import NavBar from "@/components/NavBar.vue";
import FooterLarge from "@/components/Footer-Large.vue";

export default {
    name: 'about',
    components: {
        NavBar,
        FooterLarge
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