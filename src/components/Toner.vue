<template lang="html">
  <div id="toner">
    <p>results: {{results}}</p>
    <div class="container">
      <Column v-for="n in depth"
        :key="n"
        :index="n-1"
        :colSelectedId.sync="results[n-1]"
        @colupdate="tonerUpdate(n-1, $event)"
        :breadth="breadth"/>
    </div>
    <button @click="clear">Clear</button>
  </div>
</template>

<script>
import Vue from 'vue';
import Column from './Column';

export default {
  name: 'Toner',
  props: ['depth', 'breadth'],
  data() {
    return {
      results: new Array(this.depth).fill(Math.floor(this.breadth / 2)),
    };
  },
  components: { Column },
  methods: {
    clear() {
      const init = Math.floor(this.breadth / 2);
      for (let i = 0; i < this.depth; i += 1) {
        Vue.set(this.results, i, init);
      }
    },
    tonerUpdate(m, n) {
      Vue.set(this.results, m, n);
    },
  },
};
</script>

<style>
* {
  --dim-m: 4;
  --dim-n: 5;
  --radius: 10px;
  --diameter: calc(var(--radius) * 2);
  --col-width: calc(var(--diameter) * 2);
  --full-width: calc(var(--col-width) * var(--dim-m));
  --full-height: calc((2 * var(--dim-n) + 1) * var(--diameter));
}

.container {
  position: absolute;
  left: 0; right: 0;
  display: flex;
  flex: auto;
  flex-direction: row;
  width: var(--full-width);
  height: var(--full-height);
  z-index: 2;
}
</style>
