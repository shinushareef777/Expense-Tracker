<template>
  <div class="summary-dialog">
    <v-row justify="center">
      <v-dialog v-model="dialog" scrollable width="300px">
        <v-card>
          <v-card-title>Select summarise by</v-card-title>
          <v-divider></v-divider>
          <v-card-text>
            <v-radio-group v-model="summaryBy" column>
              <v-radio label="Month" value="month"></v-radio>
              <v-radio label="Day" value="day"></v-radio>
            </v-radio-group>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
              Close
            </v-btn>
            <v-btn color="blue-darken-1" variant="text" @click="dialog = false">
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  summaryDialog: {
    type: Boolean,
    default: false,
  },
});
  
const dialog = ref(false);
watch(
  () => props.summaryDialog,
  (value) => {
    dialog.value = value;
  }
);

const summaryBy = ref("");
</script>

<style scoped></style>
