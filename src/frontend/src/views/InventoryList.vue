<template>
  <h1>Inventar</h1>
  <v-row class="mt-4">
    <!--
    cols="12": 12/12 (volle Breite)
    sm="6"   : 6/12 (2 Spalten)
    md="4"   : 4/12 (3 Spalten)
    lg="3"   : 3/12 (4 Spalten)
    -->
    <v-col v-for="item in items" cols="12" sm="6" md="4" lg="3">
      <v-card :class="{ 'opacity-50': item.isBorrowed }" class="d-flex flex-column fill-height">
        <v-card-title class="d-flex align-center">
          {{ item.name }}
          <v-spacer />
          <v-chip :color="item.isBorrowed ? 'error' : 'success'" size="small">
            {{ item.isBorrowed ? 'Ausgeliehen' : 'Verfügbar' }}
          </v-chip>
        </v-card-title>
        <v-card-text>
          <div>Kategorie: {{ item.category }}</div>
          <div class="line-clamp"> Beschreibung: {{ item.description }}</div>
        </v-card-text>
        <v-card-actions>
          <v-btn variant="text" @click="showDetails(item.id)">
            Details
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>

  <v-dialog v-model="dialogOpen" max-width="500px">
    <v-card v-if="selectedItem" :title="selectedItem.name">
      <v-card-text>
        ID: {{ selectedItem.id }}<br>
        Kategorie: {{ selectedItem.category }}<br>
        Zustand: {{ selectedItem.state }}<br>
        Ausgeliehen: {{ selectedItem.isBorrowed ? 'Ja' : 'Nein' }}<br>
        Beschreibung: {{ selectedItem.description }}
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" variant="elevated" :disabled="selectedItem.isBorrowed"
          @click="borrowItem(selectedItem.id)">
          {{ selectedItem.isBorrowed ? 'Bereits verliehen' : 'Ausleihen' }}
        </v-btn>
        <v-btn variant="text" @click="dialogOpen = false">
          Schließen
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-snackbar v-model="showError" color="error" timeout="5000" location="bottom" variant="elevated">
    {{ errorMessage }}

    <template v-slot:actions>
      <v-btn variant="text" @click="showError = false">
        Schließen
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../api.ts'

interface Item {
  state: string
  name: string
  category: string
  isBorrowed: boolean
  description: string
  id: number
}

const items = ref(<Item[]>[])
const showError = ref(false)
const errorMessage = ref('')
const dialogOpen = ref(false)
const selectedItem = ref<Item | null>(null)

onMounted(async () => {
  getInventoryList();
})

async function getInventoryList() {
  try {
    const response = await api.get('/api/items')
    items.value = response.data
    console.log(response.data)
  } catch (error: any) {
    if (error.response) {
      errorMessage.value = "Fehler: " + error.response.status + " - " + error.response.data?.detail
    } else {
      errorMessage.value = "Fehler: " + error.message
    }
    console.error(errorMessage.value)
    showError.value = true
  }
}

async function showDetails(id: number) {
  try {
    const response = await api.get(`/api/items/${id}`)
    selectedItem.value = response.data
    dialogOpen.value = true
  } catch (error: any) {
    if (error.response) {
      errorMessage.value = "Fehler: " + error.response.status + " - " + error.response.data?.detail
    } else {
      errorMessage.value = "Fehler beim Laden der Details: " + error.message
    }
    console.error(errorMessage.value)
    showError.value = true
  }
}

async function borrowItem(id: number) {
  try {
    await api.put(`/api/items/${id}/borrow`)
    dialogOpen.value = false
    await getInventoryList()
  }
  catch (error: any) {
    if (error.response) {
      errorMessage.value = "Fehler beim Ausleihen: " + error.response.status + " - " + error.response.data?.detail
    } else {
      errorMessage.value = "Fehler beim Ausleihen: " + error.message
    }
    console.error(errorMessage.value)
    showError.value = true
  }
}


</script>