<template lang="html">
  <div id="app">
    <p>Thank you for participating in this study!</p>
    <p><router-link to="/">Start another test</router-link></p>
    <p>{{store.response}}</p>
  </div>
</template>

<script>
export default {
  name: 'ThankYou',
  props: ['store'],
};
</script>

<style lang="css">
</style>
