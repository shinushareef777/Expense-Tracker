import "./assets/main.css";

import { createApp } from "vue";
import App from "./App.vue";
// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import router from "./router/expense_routes";
import mitt from "mitt";


const app = createApp(App);

const vuetify = createVuetify({
  components,
  directives,
});

const emitter = mitt();

app.provide("eventBus", emitter);

app.use(router);
app.use(vuetify);
app.mount("#app");
