<template>
  <div class="table-responsive expense-table">
    <table
      class="table table-sm table-bordered table-striped table-dark align-middle"
    >
      <thead class="text-center">
        <tr>
          <th scope="col" v-for="header in headers" :key="header.key">
            {{ header.title }}
          </th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="item in expenseList" :key="item.id">
          <td>{{ item.date }}</td>
          <td>{{ item.item }}</td>
          <td>{{ item.category_name }}</td>
          <td>{{ item.payment_method }}</td>
          <td>{{ item.price }}</td>
          <td style="width: 10%" class="align-middle text-center">
            <button
              @click="getExpense(item.id)"
              class="btn btn-outline-secondary btn-sm"
            >
              <router-link to="/add-expense">Edit</router-link>
            </button>
          </td>
          <td style="width: 10%" class="align-middle">
            <button
              @click="deleteExpense(item.id)"
              class="btn btn-outline-danger btn-sm"
            >
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <Pagination
      @next-page="gotNextPage"
      @previous-page="gotPreviousPage"
      @goto-page="gotoPageNum"
      :nextPage="nextPage"
      :prevPage="currentPageNum !== 1"
      :totalPages="totalPages"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, defineEmits, inject } from "vue";
import axios from "axios";
import Pagination from "./Pagination.vue";

const headers = [
  { title: "Date", key: "date" },
  { title: "Item", key: "item" },
  { title: "Category", key: "category_name" },
  { title: "Payment", key: "payment_method" },
  { title: "Price", key: "price" },
  { title: "", key: "edit" },
  { title: "", key: "delete" },
];

const emits = defineEmits();

const eventBus = inject("eventBus");

const expenseList = ref([]);
const currentPageNum = ref(1);
const totalPages = ref(1);
const nextPage = ref(true);

const gotPreviousPage = () => {
  getExpenseList(currentPageNum.value - 1);
  currentPageNum.value -= 1;
};

const gotNextPage = () => {
  getExpenseList(currentPageNum.value + 1);
  currentPageNum.value += 1;
};

const gotoPageNum = (num) => {
  getExpenseList(num);
  currentPageNum.value = num;
}

async function getExpenseList(pageNum) {
  try {
    let response = await axios.get(
      `/api/expenses?page=${pageNum}`
    );

    expenseList.value = response.data.results;
    totalPages.value = response.data.total_pages;
    nextPage.value = currentPageNum.value !== response.data.total_pages;
  } catch (error) {
    console.log("error", error);
  }
}

async function getExpense(id) {
  try {
    let response = await axios.get(`/api/expenses/${id}`);
    eventBus.emit("edit-expense", response.data);
  } catch (err) {}
}

async function deleteExpense(id) {
  try {
    await axios.delete(`/api/expenses/${id}`);
    getExpenseList(currentPageNum.value);
  } catch (error) {
    console.log(error);
  }
}

onMounted(() => {
  getExpenseList(1);
  console.log(expenseList.value, "expenseList.value");
});
</script>

<style>
/* Default styles for screens wider than 768px */
.expense-table {
  margin: 2em 4em 1em 4em;
}

/* Media query for screens smaller than 768px */
@media (max-width: 768px) {
  .expense-table {
    margin: 1em 2em 0.5em 2em;
  }
}

/* Media query for screens smaller than 576px */
@media (max-width: 576px) {
  .expense-table {
    margin: 0.5em 1em 0.25em 1em;
  }
}
</style>
