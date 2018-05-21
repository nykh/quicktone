<template lang="html">
  <div class="toneview">
    <h3>{{title}}</h3>
    <svg class="canvas"
      :width="(2 * xorigin) + ((len - 1) * xgap)"
      :height="(2 * yorigin) + ((ydim - 1) * ygap)">
      <g v-for="i in range(0, compareLines.length)" :key="'g' + i">
        <path :d="comparepaths[i]" :stroke="colors[i]"
              :opacity="compare_line_opacity" fill="none"/>
        <circle v-for="j in range(0, len)" :key="'cp' + i + ',' + j"
                :fill="colors[i]" :r="r" :opacity="compare_line_opacity"
                :cx="comparepts[i][0][j]" :cy="comparepts[i][1][j]" />
      </g>
      <path :d="mainpath" stroke="black" fill="none"/>
      <circle v-for="i in range(0, len)" :key="'mp' + i"
              fill="black" :r="r"
              :cx="mainpts[0][i]" :cy="mainpts[1][i]" />
    </svg>
  </div>
</template>

<script>
import { range } from '../assets/js/utils';

export default {
  name: 'ToneView',
  props: ['title', 'mainLine', 'compareLines'],
  created() {
    this.ydim = 5;
    this.len = this.mainLine.length;
    this.xorigin = 10;
    this.yorigin = 10;
    this.r = 2;
    this.xgap = 40;
    this.ygap = 25;
    this.colors = ['green', 'red', 'blue'];
    this.compare_line_opacity = 0.5;
  },
  computed: {
    mainpts() {
      return this.toCoord(this.mainLine);
    },
    mainpath() {
      return this.makePath(this.mainpts);
    },
    comparepts() {
      return this.compareLines.map(line => this.toCoord(line));
    },
    comparepaths() {
      return this.comparepts.map(coords => this.makePath(coords));
    },
  },
  methods: {
    toCoord(points) {
      return [range(0, points.length).map(x => (x * this.xgap) + this.xorigin),
        points.map(y => (y * this.ygap) + this.yorigin)];
    },
    makePath(coords) {
      let s = `M${this.xorigin} ${this.yorigin}`;
      const [xs, ys] = coords;
      s += ` M${xs[0]} ${ys[0]}`;
      for (let i = 1; i < coords[0].length; i += 1) {
        s += ` L${xs[i]} ${ys[i]}`;
      }
      return s;
    },
  },
};
</script>

<style lang="css">
.toneview h3 {
  margin-bottom: 0;
}

.toneview .canvas {
  background-color: white;
}
</style>
