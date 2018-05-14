<template>
  <div id="app">
    <h1>Welcome to QuickTone!</h1>
    <audio type="audio/mpeg" :src="sound_file" controls="controls">
      Your browser does not support the <code>audio</code> element.
    </audio>
    <Toner :depth="depth" :breadth="breadth"
      @next="next_or_submit"/>
  </div>
</template>

<script>
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
    };
  },
  computed: {
    sound_file() {
      if (Config.debug) {
        return require('./assets/001.mp3'); // eslint-disable-line global-require
      }
      const num = this.leftpad(String(this.test_id), 3, '0');

      // eslint-disable-next-line
      return require(`./assets/${num}.mp3`);
    },
  },
  methods: {
    next_or_submit() {

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
