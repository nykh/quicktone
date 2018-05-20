<template lang="html">
  <div id="app">
    <p>Thank you for participating in this study!</p>
    <p><router-link to="/">Start another test</router-link></p>
    <p>{{store.results}}</p>
    <p>{{store.response}}</p>
    <ToneView v-for="i in range(0, store.results.length)"
      :key="'test' + i" :title="'Test ' + (i+1)"
      :mainLine="store.results[i]" :compareLines="store.response[i]"></ToneView>
  </div>
</template>

<script>
import ToneView from './ToneView';

export default {
  name: 'ThankYou',
  props: ['store'],
  components: {
    ToneView,
  },
  methods: {
    range(start, end) {
      return Array.from(new Array(end - start), (_, i) => i + start);
    },
  },
};
</script>

<style lang="css">
</style>
