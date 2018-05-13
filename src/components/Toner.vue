<template lang="html">
  <div id="toner">
    <p>results: {{results}}</p>
    <div class="container">
      <div v-for="m in range(0, depth)" :key="m">
        <div  v-for="n in range(0, breadth)" :key="n"
                :class="{ circle: true, selected: isSelected(m, n) }"
                @click="tonerUpdate(m, n)"/>
      </div>
    </div>
    <button @click="clear">Clear</button>
  </div>
</template>

<script>
import Vue from 'vue';

export default {
  name: 'Toner',
  props: ['depth', 'breadth'],
  data() {
    return {
      results: new Array(this.depth).fill(Math.floor(this.breadth / 2)),
    };
  },
  methods: {
    clear() {
      const init = Math.floor(this.breadth / 2);
      for (let i = 0; i < this.depth; i += 1) {
        Vue.set(this.results, i, init);
      }
    },
    isSelected(m, n) {
      return n === this.results[m];
    },
    tonerUpdate(m, n) {
      Vue.set(this.results, m, n);
    },
    range(start, end) {
      return Array.from(new Array(end - start), (_, i) => i + start);
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

.circle {
  margin: var(--diameter) var(--radius) var(--diameter) var(--radius);
  width: var(--diameter);
  height: var(--diameter);
  border-radius: var(--radius);
  background: black;
}

.selected {
  background: red;
}

</style>
