<template>
  <div>
    <SummaryTable :headers="headers" :items="expenseSummary" />
  </div>
</template>

<script setup>
import axios from "axios";
import moment from "moment";
import { ref, onMounted } from "vue";
import SummaryTable from "./SummaryTable.vue";

const expenseSummary = ref([]);

const headers = [
  { title: "Month", key: "month" },
  { title: "Total", key: "total" },
  { title: "Maximum spent", key: "max_spent" },
];

async function getExpenseSummary() {
  try {
    response = await axios
      .get("http://127.0.0.1:4000/api/summary/month")
      .then((res) => (expenseSummary.value = res.data.results))
      .catch((err) => console.log("promoise error"));
  } catch (error) {}
}

onMounted(() => {
  getExpenseSummary();
});
</script>

<style></style>