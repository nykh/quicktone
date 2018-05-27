<template lang="html">
  <fieldset>
    <label for="language">{{label}}</label>
    <input type="text" id="language" list="langs" :value="value"
      @input="$emit('input', $event.target.value) "/>
    <datalist id="langs">
      <option v-for="(k, i) in langs" :key="'lang-'+i" :value="k" />
    </datalist>
  </fieldset>
</template>

<script>
import langs from '../assets/langs.json';

export default {
  name: 'LangSel',
  props: ['label', 'value'],
  data() {
    return {
      langs,
    };
  },
};
</script>

<style>
input[type=text] {
  padding-left: 0.5em;
  text-align: left;
  border: 0px solid black;
  border-bottom-width: 1px;
  background-color: transparent;
}
</style>
