<template lang="html">
  <div id="routing">
    <h1>QuickTone!</h1>
    <router-view></router-view>
  </div>
</template>

<script>
import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './components/App';
import ThankYou from './components/ThankYou';

Vue.use(VueRouter);

export default {
  name: 'Routing',
  router: new VueRouter({
    routes: [
      { path: '/', component: App },
      { path: '/thankyou', component: ThankYou },
    ],
  }),
};
</script>

<style lang="css">
@import 'assets/fonts/index.css';

* {
  font-family: 'Roboto Mono', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 1rem;
}
</style>
