<template>
  <div class="pa-15">
    <v-row class="pa-0 ma-0 justify-center">
      <v-col class="pa-0" cols="8">
        <v-text-field
          v-model="item"
          class="pa-0"
          label="Item"
          color="#3498db"
          base-color="#3498db"
          placeholder="Enter the item"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row class="pa-0 ma-0 justify-center">
      <v-col class="pa-0" cols="8">
        <v-text-field
          v-model="amount"
          class="pa-0"
          label="Amount"
          color="#3498db"
          base-color="#3498db"
          item-color="#3498db"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-row class="pa-0 ma-0 justify-center">
      <v-col class="pa-0" cols="8">
        <v-select
          v-model="seletedCategory"
          class="pa-0 select-menu"
          :items="categoryNames"
          label="Category"
          color="#3498db"
          base-color="#3498db"
          placeholder="Select Category"
          clearable
        ></v-select>
      </v-col>
    </v-row>
    <v-row class="pa-0 ma-0 justify-center">
      <v-col class="pa-0" cols="8">
        <v-select
          v-model="paymentMethod"
          class="pa-0"
          :items="paymentItems"
          label="Payment Method"
          color="#3498db"
          base-color="#3498db"
          placeholder="Select Category"
          clearable
        ></v-select>
      </v-col>
    </v-row>
    <v-row class="pa-0 ma-0 justify-center">
      <v-col class="pa-0" cols="8">
        <v-text-field
          label="Date of Expense"
          class="remove-placeholder"
          v-model="dateOfExpense"
          type="date"
          placeholder="Enter Date"
        >
        </v-text-field>
      </v-col>
    </v-row>
    <v-row class="pa-0 ma-0 justify-end">
      <v-col cols="3">
        <v-btn @click="save()" color="#121623" tonal>Save</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, computed, watchEffect, inject } from "vue";
import axios from "axios";
import moment from "moment";

defineProps({});

const eventBus = inject("eventBus");

const expenseId = ref(null);

const categories = ref([]);
const payments = ref([]);
const amount = ref("");
const item = ref("");
const seletedCategory = ref(null);
const seletedCategoryId = ref(null);
const seletedPaymentId = ref(null);
const paymentMethod = ref(null);
const dateOfExpense = ref(null);

async function getCategories() {
  try {
    const response = await axios.get("http://127.0.0.1:4000/api/categories");
    categories.value = response.data.results;
  } catch (error) {
    console.log(error);
  }
}

async function getPaymentMethod() {
  try {
    const response = await axios.get("http://127.0.0.1:4000/api/payments");
    payments.value = response.data.results;
  } catch (error) {
    console.log(error);
  }
}

const clearForm = () => {
  amount.value = "";
  item.value = "";
  seletedCategory.value = null;
  paymentMethod.value = null;
};

async function save() {
  let url = `http://127.0.0.1:4000/api/expenses`;
  let data = {
    item: item.value,
    price: amount.value,
    category: seletedCategoryId.value,
    payment: seletedPaymentId.value,
    date: moment(dateOfExpense.value).format("YYYY-MM-DD"),
  };
  try {
    if (!expenseId.value) {
      await axios
        .post(url, data)
        .then((res) => {
          clearForm();
        })
        .catch((err) => console.log(err));
    } else {
      await axios
        .put(url + `/${expenseId.value}`, data)
        .then((res) => clearForm())
        .catch((error) => console.log(error));
    }
  } catch (err) {
    console.log(err);
  }
}

const categoryNames = computed(() => {
  return categories.value.map((cat) => cat.name);
});

const paymentItems = computed(() => {
  return payments.value.map((pay) => pay.method);
});

watch([seletedCategory, paymentMethod], (newValues) => {
  const [catVal, payVal] = newValues;
  seletedCategoryId.value = (
    categories.value.find((category) => category.name === catVal) || {}
  ).id;
  seletedPaymentId.value = (
    payments.value.find((payment) => payment.method === payVal) || {}
  ).id;
});

onMounted(() => {
  getCategories();
  getPaymentMethod();
  eventBus.on("edit-expense", (data) => {
    amount.value = data.price;
    item.value = data.item;
    seletedCategory.value = data.category_name;
    paymentMethod.value = data.payment_method;
    dateOfExpense.value = data.date;
    expenseId.value = data.id;
  });
});

watchEffect(() => {
  // emitter.on('edit-expense', () => console.log('emitter.on'))
});
</script>

<style scoped>
</style>
