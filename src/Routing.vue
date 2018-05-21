<template lang="html">
  <div id="routing">
    <h1>QuickTone!</h1>
    <router-view></router-view>
  </div>
</template>

<script>
import Vue from 'vue';
import VueRouter from 'vue-router';
import Questionaire from './components/Questionaire';
import App from './components/App';
import ThankYou from './components/ThankYou';

Vue.use(VueRouter);

const store = {
  results: [],
  response: [],
  questionaire: {},
};

export default {
  name: 'Routing',
  router: new VueRouter({
    routes: [
      { path: '/', component: Questionaire, props: { store } },
      { path: '/tests', component: App, props: { store } },
      { path: '/thankyou', component: ThankYou, props: { store } },
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

button {
  min-width: 5rem;
  color: #715b09;
  background-color: #eec223;
}
</style>
