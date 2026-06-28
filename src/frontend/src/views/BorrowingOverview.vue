<template>
  <h1>Ausleihen</h1>

  <v-row class="mt-4">
  <v-col v-for="item in items" cols="12" sm="6" md="4" lg="3">
    <v-card class="d-flex flex-column fill-height">
      <v-card-title class="d-flex align-center">
        {{ item.item_name }}
      </v-card-title>
      <v-card-text>
        <div>Ausleihdatum: {{ item.borrowing_date }}</div>
        <div>Abgabetermin: {{ item.due_date }}</div>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="returnItem(item.item_id)">
          Zurückgeben
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-col>
  </v-row>

  <v-snackbar v-model="showSnackbar" :color="snackbarColor" timeout="5000" location="bottom" variant="elevated">
    {{ snackbarMessage }}

    <template v-slot:actions>
      <v-btn variant="text" @click="showSnackbar = false">
        <v-icon>mdi-window-close</v-icon>
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../api.ts'

interface Item {
  borrowing_date: string
  due_date: string
  return_date: string
  item_name: string
  item_id: number
}
const items = ref(<Item[]>[])

const showSnackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('success')

// Liste holen
onMounted(async () => {
  getBorrowList();
})

async function getBorrowList() {
  try {
    const response = await api.get('/api/borrowings/all/details/')
    items.value = response.data
    console.log(response.data)
  } catch (error: any) {
    snackbarColor.value = 'error'
    if (error.response) {
      snackbarMessage.value = "Fehler: " + error.response.status + " - " + error.response.data?.detail
    } else {
      snackbarMessage.value = "Fehler: " + error.message
    }
    console.error(snackbarMessage.value)
    showSnackbar.value = true
  }
}

// Rückgabe
async function returnItem(id: number) {
   try {
    await api.put(`/api/items/return/${id}`)

    await getBorrowList();
    snackbarColor.value = 'success'
    snackbarMessage.value = 'Gegenstand wurde erfolgreich zurückgegeben!'
    showSnackbar.value = true
  }
  catch (error: any) {
    snackbarColor.value = 'error'
    if (error.response) {
      snackbarMessage.value = "Fehler bei Rückgabe: " + error.response.status + " - " + error.response.data?.detail
    } else {
      snackbarMessage.value = "Fehler beim Rückgabe: " + error.message
    }
    console.error(snackbarMessage.value)
    showSnackbar.value = true
  }
}

</script>