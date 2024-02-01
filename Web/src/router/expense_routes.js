import { createRouter, createWebHistory } from "vue-router";
// Import your Vue components
import ExpenseList from "@/components/ExpenseList.vue"
import AddExpenseForm from "@/components/AddExpenseForm.vue"
import ExpenseSummaryByDate from "@/components/ExpenseSummaryByDate.vue"
import ExpenseSummaryByMonth from "@/components/ExpenseSummaryByMonth.vue"

// Create a router instance
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: ExpenseList },
    { path: "/home", component: ExpenseList },
    { path: "/add-expense", component: AddExpenseForm },
    { path: "/summary", component: ExpenseSummaryByDate },
  ],
});

export default router;
