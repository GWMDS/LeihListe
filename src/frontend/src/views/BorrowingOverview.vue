<template>
  <h1>Ausleihen</h1>

  <v-row class="mt-4">
    <v-col v-for="item in items" cols="12" sm="6" md="4" lg="3">
      <v-card class="d-flex flex-column fill-height">
        <v-card-title class="d-flex align-center">
          <div class="text-truncate">{{ item.item_name }}</div>
          <v-spacer />
          <v-chip class="flex-shrink-0" color="error"
            v-if="(daysSinceLastDate(new Date(Date.now()), new Date(item.due_date)) > 0)">
            <v-icon>mdi-exclamation</v-icon>Verspätet
          </v-chip>
        </v-card-title>
        <v-card-text>
          <div>Ausleihdatum: {{ dateFormatter.format(new Date(item.borrowing_date)) }}</div>
          <div>Abgabetermin: {{ dateFormatter.format(new Date(item.due_date)) }}</div>

          <!--<div>Days over due_date: {{ daysSinceLastDate(new Date(Date.now()), new Date(item.due_date)) }}</div>-->
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

const dateFormatter = new Intl.DateTimeFormat("de-DE", {
  day: "2-digit",
  month: "2-digit",
  year: "numeric",
});

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

function daysSinceLastDate(currentDate: Date, previousDate: Date) {
  const timeDifference = currentDate.getTime() - previousDate.getTime()
  const daysDifference = Math.floor(timeDifference / (1000 * 60 * 60 * 24))
  return daysDifference
}

</script>