<template lang="html">
    <NavBar></NavBar>
    <div id="about-body">
        <div class="container">
            <div class="row">
                <div class="sidebar sticky col-4">
                    <img src="@/assets/images/About/headshot-aug21.jpg">
                    <h3>Daniel A. Stephan II</h3>
                    <p class="job-title">Frontend Web Developer Intern</p>
                </div>
                <div class="content col-8">
                    <div class="row about">
                        <h1>About Me</h1>
                        <p class="personal-details"><span class="red">26 years</span> | <span class="red">Massillon, Ohio</span></p>
                        <div class="section">
                            <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales velit in ipsum ultrices fringilla. Morbi non sollicitudin enim. Curabitur rhoncus luctus urna, lacinia suscipit massa tempus ut. Vivamus non justo elit. Nulla quis imperdiet ligula, non commodo dolor. Nullam elementum ac enim congue aliquam. Donec ipsum mi, convallis non nibh eget, imperdiet ultricies lectus. Etiam placerat arcu sapien, eu placerat nibh posuere ut. Donec orci neque, tristique eu nunc sit amet, aliquet lacinia ante. Sed tempus enim sit amet lectus sagittis ornare. Vestibulum quis lectus imperdiet felis sodales bibendum. Morbi nec sem urna. Phasellus a lectus et lectus egestas sagittis. Cras egestas facilisis nisi ac porttitor. Etiam iaculis bibendum lacus quis euismod.</p> 
                        </div> 
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
                                <div class="flex align-center">
                                    <div style="flex-basis: 50%; margin-right: 30px">
                                        <h6>GPA</h6>
                                        <p class="GPA">3.178</p>
                                        <p class="GPA-Detail">cumulative</p>
                                        <p class="GPA">3.667</p>
                                        <p class="GPA-Detail">major</p>
                                    </div>
                                    <div style="flex-basis: 50%; margin-left: 30px">
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
                                    <div class="flex">
                                        <div style="flex-basis: 50%; margin-right: 30px">
                                            <p>Software Engineering</p>
                                            <p>Digital Forensics</p>
                                        </div>
                                        <div style="flex-basis: 50%; margin-left: 30px">
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
                                    <p class="GPA">-</p>
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
    }
}

</script>