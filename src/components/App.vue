<template>
  <div id="app">
    <h2>Test {{test_id}}/{{numTests}}</h2>
    <p>Please listen to the audio below and draw the line representing
      what you think the tone you heard is by adjusting the dots.</p>
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
import { leftpad } from '../assets/js/utils';

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
      const num = leftpad(String(this.test_id), 3, '0');

      // eslint-disable-next-line
      return require(`../assets/sounds/${num}.wav`);
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
      axios.post(Config.post_url, {
        data: this.results,
        questionaire: this.store.questionaire,
      }).then((res) => {
        this.store.results = this.results;
        this.store.response = res.data.data;
        this.$router.push('/thankyou');
      }).catch((e) => {
        this.errors.push(e);
      });
    },
  },
};
</script>

<style>
#app p {
  margin: auto;
  margin-top: 1rem;
  margin-bottom: 1rem;
  width: 50%;
}

#app Toner {
  margin: auto;
}
</style>
