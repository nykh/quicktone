<template lang="html">
  <div>
    <div class="meta">
      <svg class="container" ref="svgcanvas"
           :width="2 * r + (depth - 1) * xgap" :height="2 * r + (breadth - 1) * ygap">
        <line v-for="m in range(0, depth - 1)" :key="'line' + m"
              class="connector" :x1="r + m * xgap" :x2="r + (m + 1) * xgap"
              :y1="r + results[m] * ygap" :y2="r + results[m+1] * ygap"/>
        <g v-for="m in range(0, depth)" :key="'g' + m">
          <circle  v-for="n in range(0, breadth)" :key="'c' + n"
            :class="{ circle: true, selected: isSelected(m, n) }"
            :r="r" :cx="r + m * xgap" :cy="r + n * ygap"
            @click="tonerUpdate(m, n)"/>
        </g>
      </svg>
      <hr>
    </div>
    <button class="clear" @click="clear">Clear</button>
    <button class="submit" @click="submit">Submit</button>
  </div>
</template>

<script>
import Vue from 'vue';

export default {
  name: 'Toner',
  props: ['depth', 'breadth'],
  created() {
    this.r = 10;
    this.xgap = 70;
    this.ygap = 50;
  },
  data() {
    const init = Math.floor(this.breadth / 2);
    return {
      results: new Array(this.depth).fill(init),
    };
  },
  methods: {
    clear() {
      const init = Math.floor(this.breadth / 2);
      for (let i = 0; i < this.depth; i += 1) {
        Vue.set(this.results, i, init);
      }
    },
    submit() {
      this.$emit('next', this.results.slice());
      this.clear();
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
.meta {
  margin: auto;
  max-width: 50%;
}

.container {
  margin: 10px;
}

.container .connector {
  stroke: black;
  stroke-width: 4;
}

.container .circle {
  fill: black;
}

.container .circle:hover {
  fill: yellow;
}

.container .selected {
  fill: red;
}

button.clear {
  color: black;
  background-color: #b0b0b0;
}
</style>
