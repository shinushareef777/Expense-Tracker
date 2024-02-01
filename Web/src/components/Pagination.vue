<template>
  <nav aria-label="Page navigation example">
    <ul  class="pagination black-ul">
      <li class="page-item" v-if="props.prevPage">
        <a
          @click="gotoPreviousPage"
          class="page-link"
          href="#"
          aria-label="Previous"
        >
          <span aria-hidden="true">&laquo;</span>
        </a>
      </li>
      <li class="page-item" v-for="v in props.totalPages">
        <a href="#" @click="gotoPage(v)" class="page-link">{{ v }}</a>
      </li>
      <li class="page-item" v-if="props.nextPage">
        <a @click="gotoNextPage" class="page-link" href="#" aria-label="Next">
          <span aria-hidden="true">&raquo;</span>
        </a>
      </li>
    </ul>
  </nav>
</template>
<script setup>
import { defineEmits, defineProps } from "vue";

const props = defineProps({
  nextPage: Boolean,
  prevPage: Boolean,
  totalPages: Number,
});

const emits = defineEmits();

const gotoNextPage = () => {
  emits("next-page");
};
const gotoPreviousPage = () => {
  emits("previous-page");
};

const gotoPage = (num) => {
  emits("goto-page", num);
};
</script>

<style scoped>
a{
  background-color: #222222 !important;
  border: 1px solid #282828;
}

a:hover{
  border: none;
  color: hsla(160, 100%, 37%, 1);
}
</style>
