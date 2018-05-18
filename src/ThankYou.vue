<template lang="html">
  <div id="app">
    <h1>QuickTone!</h1>
    <p>Thank you for participating in this study!</p>
    <p><router-link to="/">Start another test</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'ThankYou',
};
</script>

<style lang="css">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
