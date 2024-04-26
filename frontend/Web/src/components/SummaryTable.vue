<template>
  <div class="table-responsive expense-table">
    <table
      class="table table-sm table-bordered table-striped table-dark align-middle text-center"
    >
      <thead>
        <tr>
          <th scope="col" v-for="header in props.headers" :key="header.key">
            {{ header.title }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in props.items" :key="item.date">
          <td v-for="(key, value) in item" v-if="value !== 'id'">
            {{ key }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const props = defineProps({
  headers: {
    type: Array,
    default: () => [],
  },
  items: {
    type: Array,
    default: () => [],
  },
});
</script>

<style></style>
