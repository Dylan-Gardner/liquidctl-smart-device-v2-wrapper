<template>
  <div class="about">
    <h1>Backend Resources Demo</h1>
    <p>Click on the links below to fetch data from the Flask server</p>
    <a href @click.prevent="getStatus">Run Script</a>
    <h4>Results</h4>
    <p>{{ result }}</p>
    <p>{{ error }}</p>
    <div class="small">
      <line-chart :chart-data="datacollection"></line-chart>
      <button @click="fillData()">Randomize</button>
    </div>
  </div>
</template>

<script>
import $backend from "../backend";
import LineChart from "../components/Chart.js";

export default {
  name: "about",
  components: {
    LineChart,
  },
  data() {
    return {
      result: "",
      error: "",
      datacollection: null,
    };
  },
  mounted() {
    this.fillData();
  },
  methods: {
    getStatus() {
      $backend
        .getStatus()
        .then((res) => {
          this.result = res.status;
        })
        .catch((error) => {
          this.error = error.message;
        });
    },
    fillData() {
      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#f87979",
            data: [this.getRandomInt(), this.getRandomInt()],
          },
          {
            label: "Data One",
            backgroundColor: "#f87979",
            data: [this.getRandomInt(), this.getRandomInt()],
          },
        ],
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    },
  },
};
</script>

<style lang="scss">
.small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
