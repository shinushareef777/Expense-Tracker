<template>
  <!-- <div class="table-responsive expense-table">
    <table
      class="table table-sm table-bordered table-striped table-dark align-middle text-center"
    >
      <thead>
        <tr>
          <th scope="col" v-for="header in headers" :key="header.key">
            {{ header.title }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in expenseSummary" :key="item.date">
          <td>{{ item.date }}</td>
          <td>{{ item.total }}</td>
          <td>{{ item.max_spent }}</td>
          <td>{{ item.max_item }}</td>
        </tr>
      </tbody>
    </table>
  </div> -->
  <div>
    <SummaryTable :headers="headers" :items="expenseSummary"/>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import SummaryTable from "./SummaryTable.vue";

const expenseSummary = ref([]);

const headers = [
  { title: "Date", key: "date" },
  { title: "Total", key: "total" },
  { title: "Maximum spent", key: "max_spent" },
  { title: "Maximum spent item", key: "max_item" },
];

async function getExpenseSummary() {
  try {
    response = await axios
      .get("http://127.0.0.1:4000/api/summary/day")
      .then((res) => (expenseSummary.value = res.data.results))
      .catch((err) => console.log("promoise error"));
  } catch (error) {}
}

onMounted(() => {
  getExpenseSummary();
});
</script>

<style></style>
