<template lang="html">
    <div id="body" class="fade-in">

          <div class="container">
            <router-link to="/"><img class="logo" src="@/assets/images/star-logo.png" width="80" style="opacity: 0.5; margin-bottom: 20px;"></router-link>
            <h1>Super Speed Typing Test</h1>
            <div class="header">
                <div id="wpm">
                    <h6>WPM</h6>
                    <p>{{ wpm }}</p>
                </div>
                <div id="cpm">
                    <h6>CPM</h6>
                    <p>{{ cpm }}</p>
                </div>
                <div class="errors">
                    <h6>Errors</h6>
                    <p>{{ errors }}</p>
                </div>
                <div id="timer">
                    <h6>Time</h6>
                    <p>{{ time }}s</p>
                </div>
                <div class="accuracy">
                    <h6>Accuracy</h6>
                    <p>{{ accuracy }}%</p>
                </div>
            </div>

            <p class="instructions">{{ quote }}</p>
            <textarea id="input" class="form-control" placeholder="start typing here..."></textarea>
            <button class="restart-btn btn" style="color: var(--theme-white); background: var(--theme-primary-dark); width: 150px;" id="restart">Restart</button>
        </div>

    </div>
</template>

<script lang="js">

export default {
    name: 'home',
    data(){
        return{
            wpm: 0,
            cpm: 0,
            errors: 0,
            total_errors: 0,
            time: 0,
            TIME_LIMIT: 60,
            timeElapsed: 0,
            accuracy: 100,
            quotes_array: [
                "Push yourself, because no one else is going to do it for you.",
                "Failure is the condiment that gives success its flavor.",
                "Wake up with determination. Go to bed with satisfaction.",
                "It's going to be hard, but hard does not mean impossible.",
                "Learning never exhausts the mind.",
                "Excuse me sir, the sink is on fire.",
                "Look out below, here comes mama!",
                "I can't believe I just typed that.",
                "Wow, I can type pretty fast.",
                "You go girl.",
                "The only way to do great work is to love what you do."
            ],
            quote: "Click on the area below to start the game.",
            timer: null,
            quoteNo: 0,
            quote_text: [],
            characterTyped: 0,
            input_area: null
        }
    },
    mounted: function () {
        this.input_area = document.getElementById('input');
        this.input_area.addEventListener('focus', () => { this.startGame(); }, true);

        const resetListener = document.getElementById('restart');
        resetListener.addEventListener('click', () => { this.resetGame(); }, true);

        this.time = this.TIME_LIMIT;
    },
    computed: {
        setTimer(){
            return this.time;
        },
        setWPM(){
            return this.wpm;
        },
        setCPM(){
            return this.cpm;
        },
        setAccuracy(){
            return this.accuracy;
        },
        setErrors(){
            return this.errors;
        }
    },
    methods: {
        startGame() {
            this.resetGame();
            this.updateQuote();
            this.input_area.addEventListener('keyup', (e) => { this.processCurrentText(e.key); }, true);
            clearInterval(this.timer);
            this.timer = setInterval(this.updateTimer, 1000);
        },
        updateTimer(){
              if (this.time > 0) {
                    this.time--;
                    this.timeElapsed++;
                }
                else {
                    this.finishGame();
                }
        },
        updateQuote() {
            this.quote = this.quotes_array[this.quoteNo];

            this.quote_text = [];

            // separate each character and make an element 
            // out of each of them to individually style them
            this.quote.split('').forEach(char => {
                const charSpan = document.createElement('span')
                charSpan.innerText = char
                this.quote_text.push(charSpan)
            })

            // roll over to the first quote
            if (this.quoteNo < this.quotes_array.length - 1)
                this.quoteNo++;
            else
                this.quoteNo = 0;
        },
        processCurrentText(current_char) {
            // get current input text and split it
            let curr_input = this.input_area.value;
            let curr_input_array = curr_input.split('');

            // keeps track of total number of characters
            this.characterTyped = curr_input_array.length;


                // characters not currently typed
                if (current_char == null) {
                this.quote_text[this.characterTyped-1].classList.remove('correct_char');
                this.quote_text[this.characterTyped-1].classList.remove('incorrect_char');

                // correct characters
                } else if (current_char === this.quote_text[this.characterTyped-1]) {
                this.quote_text[this.characterTyped-1].classList.add('correct_char');
                this.quote_text[this.characterTyped-1].classList.remove('incorrect_char');

                } else if (current_char == 'backspace') {

                // incorrect characters
                } else {
                this.quote_text[this.characterTyped-1].classList.add('incorrect_char');
                this.quote_text[this.characterTyped-1].classList.remove('correct_char');

                // increment number of errors
                this.errors++;
                }
            
            console.log(this.quote_text[this.characterTyped-1])

            // update accuracy text
            let correctCharacters = (this.characterTyped - (this.total_errors + this.errors));
            let accuracyVal = ((correctCharacters / this.characterTyped) * 100);
            this.accuracy = Math.round(accuracyVal);

            // if current text is completely typed
            // irrespective of errors
            if (curr_input.length == this.quote.length) {
                this.updateQuote();

                // update total errors
                this.total_errors += this.errors;

                // clear the input area
                this.input_area.value = "";
            }
        },
        finishGame(){
            // stop the timer
            clearInterval(this.timer);

            // disable the input area
            this.input_area.disabled = true;
            this.input_area.style.display = "none";

            // show finishing text
            this.quote = "Click on restart to start a new game.";

            // display restart button
            const reset_btn = document.getElementById('restart');
            reset_btn.style.display = "block";

            // calculate cpm and wpm
            this.cpm = Math.round(((this.characterTyped / this.timeElapsed) * 60));
            this.wpm = Math.round((((this.characterTyped / 5) / this.timeElapsed) * 60));

            const timer_group = document.getElementById('timer');
            timer_group.style.display = "none";

            // display the cpm and wpm
            const cpm_group = document.getElementById('cpm');
            const wpm_group = document.getElementById('wpm');
            cpm_group.style.display = "block";
            wpm_group.style.display = "block";
        },
        resetGame() {
            const reset_btn = document.getElementById('restart');
            const cpm_group = document.getElementById('cpm');
            const wpm_group = document.getElementById('wpm');
            const timer_group = document.getElementById('timer');

            this.time = this.TIME_LIMIT;
            this.timeElapsed = 0;
            this.errors = 0;
            this.total_errors = 0;
            this.accuracy = 0;
            this.characterTyped = 0;
            this.quoteNo = 0;
            
            this.input_area.disabled = false;
            this.input_area.style.display = "block";

            this.input_area.value = "";
            this.quote = 'Click on the area below to start the game.';
            this.accuracy = 100;
            // error_text.textContent = 0;

            timer_group.style.display = "block";
            reset_btn.style.display = "none";
            cpm_group.style.display = "none";
            wpm_group.style.display = "none";
            }
    }
}

</script>

<style scoped>
  #body {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #0d0d0d;
    color: var(--theme-primary-dark);
    position: relative;
  }
  h6{
      margin-bottom: 10px;
      line-height: 1;
      color: var(--theme-white);
      font-size: 35px !important;
  }
  p{
      margin: 0;
      margin-bottom: 0 !important;
      font-size: 24px !important;
      line-height: 1;
      color: var(--theme-white);
  }

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.header {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    margin: 40px 0 60px;
}

#timer, .errors,
.accuracy, #cpm, #wpm {
    background-color: rgba(225, 0, 0, 0.3);
    margin:  0 10px;
    padding: 30px;
    border-radius: 30px;
    box-shadow: black 5px 8px 5px;
    flex-basis: 20%;
    text-align: center;
}

#cpm, #wpm  {
  display: none;
}

.instructions {
  font-size: 18px !important;
  box-shadow: black 5px 8px 5px;
  display: block;
}

textarea {
  max-width: 900px; 
  display: block;
  margin: 20px auto 0;
  background-color: rgba(248, 223, 222, 0.1);
  height: 80px;
  font-size: 1.5rem;
  font-weight: 600;
  padding: 20px;
  border: 0px;
  box-shadow: black 5px 8px 5px;
}
textarea[disabled]{
    background-color: rgba(248, 223, 222, 0.1);
}

.incorrect_char {
  color: red !important;
  text-decoration: underline !important; 
}

.correct_char {
  color: darkgreen !important;
}

.restart-btn {
  display: none;
}

  .btn{
    margin-top: 20px;
    opacity: 0.60;
    transition: all 0.3s;
  }
  .btn:hover{
    opacity: 1;
  }

  @media screen and (max-width: 768px){
      #body{
          text-align: center;
          padding-top: 120px;
      }
  }
</style>