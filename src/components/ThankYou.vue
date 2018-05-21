<template lang="html">
  <div id="app">
    <p>Thank you for participating in this study!</p>
    <p><router-link to="/">Start another test</router-link></p>
    <h2 v-if="store.results.length > 0">Results</h2>
    <div class="results" v-if="store.results.length > 0">
      <ToneView class="toneview" v-for="i in range(0, store.results.length)"
      :key="'test' + i" :title="'Test ' + (i+1)"
      :mainLine="store.results[i]" :compareLines="store.response[i]"></ToneView>
    </div>
  </div>
</template>

<script>
import ToneView from './ToneView';
import { range } from '../assets/js/utils';

export default {
  name: 'ThankYou',
  props: ['store'],
  components: {
    ToneView,
  },
  methods: {
    range,
  },
};
</script>

<style lang="css">
.results {
  display: flex;
  flex-flow: row wrap;
  margin: auto;
  width: 40%;
}

.results > .toneview {
  flex: 1;
}
</style>
