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
                    <h1>About Me</h1>
                    <p class="personal-details"><span class="red">26 years</span> | <span class="red">Massillon, Ohio</span></p>
                    <div class="section">
                        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales velit in ipsum ultrices fringilla. Morbi non sollicitudin enim. Curabitur rhoncus luctus urna, lacinia suscipit massa tempus ut. Vivamus non justo elit. Nulla quis imperdiet ligula, non commodo dolor. Nullam elementum ac enim congue aliquam. Donec ipsum mi, convallis non nibh eget, imperdiet ultricies lectus. Etiam placerat arcu sapien, eu placerat nibh posuere ut. Donec orci neque, tristique eu nunc sit amet, aliquet lacinia ante. Sed tempus enim sit amet lectus sagittis ornare. Vestibulum quis lectus imperdiet felis sodales bibendum. Morbi nec sem urna. Phasellus a lectus et lectus egestas sagittis. Cras egestas facilisis nisi ac porttitor. Etiam iaculis bibendum lacus quis euismod.</p> 
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