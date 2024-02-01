<script setup>
import NavBar from "./components/NavBar.vue";
</script>

<template>
  <div class="container-fluid nav-width">
    <NavBar />
    <router-view></router-view>
  </div>
</template>

<style scoped>
.nav-width {
  width: 100%;
  margin-bottom: 30px;
  padding: 0;
}
</style>
