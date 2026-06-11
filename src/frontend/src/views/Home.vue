<template>
  <h1>Home</h1>
  <v-btn color="primary" @click="Test">
    API GET Test
  </v-btn>

  <v-textarea
      v-model="itemsText"
      label="Backend Items"
      readonly
      rows="10"
      class="mt-4"
      variant="outlined"
  ></v-textarea>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import api from '../api.ts'

const itemsText = ref('')
async function Test() {
  try {
    const response = await api.get('/api/items')
    itemsText.value =JSON.stringify(response.data,null,2)
    console.log(response.data)
  } catch (error: any) {
      console.error("Status: " + error.response.status)
      console.error("Data Detail: " + error.response?.data.detail)
      itemsText.value = "Fehler-Status: " + error.response.status
  }
}

</script>