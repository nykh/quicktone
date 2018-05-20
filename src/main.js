// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Routing from './Routing';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { Routing },
  template: '<Routing></Routing>',
});
