<template>
  <nav
    class="navbar sticky-top bg-dark border-bottom border-body"
    data-bs-theme="dark"
  >
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Expense Tracker</router-link>
      <div>
        <router-link class="p-5" to="/home">Home</router-link>
        <router-link class="p-5" to="/add-expense">Add Expense</router-link>
        <a class="p-5" @click="openModal">Summary</a>
      </div>
    </div>
    <SummaryModal :summaryDialog="dialog" />
  </nav>
</template>

<script setup>
import SummaryModal from "./SummaryModal.vue";
import { ref } from "vue";

const dialog = ref(false)

const openModal = (() => {
 dialog.value=true
})
</script>
<style></style>
