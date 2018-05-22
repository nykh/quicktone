<template lang="html">
  <div>
    <div id="questionaire">
      <p>Please answer the following questions.</p>
      <fieldset>
        <label for="learner">Have you learned Chinese before?</label>
        <input type="radio" name="L-yes" :value="true" v-model="learner">
        <label for="yes">Yes</label>
        <input type="radio" name="L-no" :value="false" v-model="learner">
        <label for="no">No</label>
      </fieldset>
      <transition name="fade">
        <fieldset v-if="learner" class="sub1" >
          <label for="years">For how many years?</label>
          <input id="years" type="number" style="max-width: 2em;"
                 v-model="years" min="0" max="99">
        </fieldset>
      </transition>
      <fieldset>
        <label for="englishspeaker">Is English your first language?</label>
        <input type="radio" name="en-yes" :value="true" v-model="englishspeaker">
        <label for="yes">Yes</label>
        <input type="radio" name="en-no" :value="false" v-model="englishspeaker">
        <label for="no">No</label>
      </fieldset>
      <transition name="fade">
        <LangSel class="sub1" v-if="!englishspeaker" v-model="language"
                 :label="'My first language is'" />
      </transition>
      <fieldset>
        <label for="drawtone">Do you know how to draw Chinese tones?</label>
        <input type="radio" name="d-yes" :value="true" v-model="drawtone">
        <label for="yes">Yes</label>
        <input type="radio" name="d-no" :value="false" v-model="drawtone">
        <label for="no">No</label>
      </fieldset>
      <hr>
    </div>
    <p>In the following pages, you will listen to one tone each time.<br>
      Draw the tone you hear by adjusting the dots in the square.</p>
    <button id="submit" @click="submit()">I am Ready!</button>
  </div>
</template>

<script>
import LangSel from './LangSel';

export default {
  name: 'Questionaire',
  props: ['store'],
  components: {
    LangSel,
  },
  data() {
    return {
      learner: false,
      years: 0,
      englishspeaker: true,
      language: '',
      drawtone: false,
    };
  },
  methods: {
    submit() {
      this.store.questionaire = {
        learner: this.learner,
        years: this.years,
        englishspeaker: this.englishspeaker,
        language: this.language,
        drawtone: this.drawtone,
      };
      this.$router.push('/tests');
    },
  },
};
</script>

<style lang="css">
#questionaire {
  margin: auto;
  max-width: 50%;
}

#questionaire > fieldset {
  text-align: left;
  border: 0px;
}

.sub1 {
  position: relative;
  left: 2em;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.8s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

input[type=number] {
  padding-left: 0.5em;
  text-align: left;
  border: 0px solid black;
  border-bottom-width: 1px;
  background-color: transparent;
}
</style>
