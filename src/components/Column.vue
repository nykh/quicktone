<template lang="html">
  <div class="column">
    <div  v-for="n in breadth"
            :key="n-1"
            :index="n-1"
            :class="{ circle: true, selected: isSelected(n-1) }"
            @click="colUpdate(n-1)"/>
  </div>
</template>

<script>
export default {
  name: 'Column',
  props: ['index', 'breadth', 'colSelectedId'],
  computed: {
    selectedId: {
      get() { return this.colSelectedId; },
      set(val) {
        this.$emit('colupdate', val);
      },
    },
  },
  methods: {
    isSelected(i) {
      return i === this.selectedId;
    },
    colUpdate(n) {
      this.selectedId = n;
    },
  },
};
</script>

<style lang="css">
* {
  --radius: 10px;
  --diameter: calc(var(--radius) * 2);
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
