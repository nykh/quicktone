<template lang="html">
  <div id="questionaire">
    <p>Please answer the following questions.</p>
    <fieldset>
      <input id="learner" type="checkbox" v-model="learner">
      <label for="learner">Have you learned Chinese before?</label>
    </fieldset>
    <fieldset>
      <input id="englishspeaker" type="checkbox" v-model="englishspeaker">
      <label for="englishspeaker">Is English your first language?</label>
    </fieldset>
    <fieldset>
      <input id="drawtone" type="checkbox" v-model="drawtone">
      <label for="drawtone">Do you know how to draw Chinese tones?</label>
    </fieldset>
    <hr>
    <p>In the following pages, you will listen to one tone each time.<br>
      Draw the tone you hear by adjusting the dots in the square.</p>
    <button id="submit" @click="submit()">I am Ready!</button>
  </div>
</template>

<script>
export default {
  name: 'Questionaire',
  props: ['store'],
  data() {
    return {
      learner: false,
      englishspeaker: false,
      drawtone: false,
    };
  },
  methods: {
    submit() {
      this.store.questionaire = {
        learner: this.learner,
        englishspeaker: this.englishspeaker,
        drawtone: this.drawtone,
      };
      this.$router.push('/tests');
    },
  },
};
</script>

<style lang="css">
fieldset {
  border: 0px;
}
</style>
