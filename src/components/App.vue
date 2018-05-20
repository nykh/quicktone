<template>
  <div id="app">
    <h2>Test {{test_id}}</h2>
    <p>Please listen to the audio below and draw the line representing
      what you think the tone you heard is.</p>
    <audio type="audio/mpeg" :src="sound_file" controls="controls">
      Your browser does not support the <code>audio</code> element.
    </audio>
    <Toner :depth="depth" :breadth="breadth"
      @next="next_or_submit($event)"/>
    <ul v-if="errors && errors.length">
      <li v-for="(error, key) of errors" :key="key">
        {{error.message}}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';
import Toner from './Toner';
import Config from '../experiment.json';

export default {
  name: 'App',
  props: ['store'],
  components: {
    Toner,
  },
  data() {
    return {
      numTests: Config.numTests,
      depth: Config.length,
      breadth: Config.width,
      test_id: 1,
      results: [],
      errors: [],
    };
  },
  computed: {
    sound_file() {
      const num = this.leftpad(String(this.test_id), 3, '0');

      // eslint-disable-next-line
      return require(`../assets/${num}.wav`);
    },
  },
  methods: {
    next_or_submit(result) {
      this.results.push(result);
      if (this.test_id >= this.numTests) {
        this.submit();
      } else {
        this.test_id += 1;
      }
    },
    submit() {
      axios.post(Config.post_url, { data: this.results })
        .then((res) => {
          this.store.results = this.results;
          this.store.response = res.data.data;
          this.$router.push('/thankyou');
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
    leftpad(_str, _len, _ch) {
      let str = String(_str);
      let i = 0;
      let len = _len;
      let ch = _ch;
      if (!ch && ch !== 0) ch = ' ';
      len -= str.length;
      while (i < len) {
        str = ch + str;
        i += 1;
      }
      return str;
    },
  },
};
</script>

<style>
#app p {
  margin: auto;
  margin-top: 1rem;
  margin-bottom: 1rem;
  width: 60%;
}

#app Toner {
  margin: auto;
}
</style>
