<template>
  <div id="app">
    <h1>Welcome to QuickTone!</h1>
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
import Toner from './components/Toner';
import Config from './experiment.json';

export default {
  name: 'App',
  components: {
    Toner,
  },
  data() {
    return {
      numTests: Config.numTests,
      depth: Config.length,
      breadth: Config.width,
      test_id: 0,
      results: [],
      errors: [],
    };
  },
  computed: {
    sound_file() {
      const num = this.leftpad(String(this.test_id + 1), 3, '0');

      // eslint-disable-next-line
      return require(`./assets/${num}.mp3`);
    },
  },
  methods: {
    next_or_submit(result) {
      this.results.push(result);
      if (this.test_id + 1 >= this.numTests) {
        this.submit();
      } else {
        this.test_id += 1;
      }
    },
    submit() {
      axios.post(Config.post_url, { body: 1 })
        .then(() => {})
        .catch((e) => { this.errors.push(e); });
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#app Toner {
  margin: auto;
}
</style>
