<template>
  <div id="app">
    <Toner :depth="4" :breadth="5" />
  </div>
</template>

<script>
import Toner from './components/Toner';

export default {
  name: 'App',
  components: {
    Toner,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
