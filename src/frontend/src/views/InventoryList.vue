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
          <v-row justify="space-between">
            <v-col cols="auto">
              <v-btn @click.stop="showDetails(item.id)">
                Details
              </v-btn>
            </v-col>
            <v-col cols="auto">
              <v-btn title="Bearbeiten">
                <v-icon size="large">mdi-pencil</v-icon>
              </v-btn>
              <v-btn title="Löschen" color="error" @click="triggerDelete(item)">
                <v-icon size="large">mdi-delete</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>

  <v-dialog v-model="deleteDialogOpen" max-width="400">
    <v-card>
      <v-card-title class="text-error">
        <v-icon start>mdi-alert-circle</v-icon>Gegenstand löschen?
      </v-card-title>
      <v-card-text>
        Sind Sie sicher, dass Sie den Gegenstand <strong>{{ itemToDelete?.name }}</strong> löschen möchten?
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn variant="text" @click="deleteDialogOpen = false">Abbrechen</v-btn>
        <v-btn color="error" variant="elevated" @click="confirmDelete">Löschen</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog v-model="dialogOpen" max-width="500px">
    <v-card v-if="selectedItem">
      <v-card-title>{{ selectedItem.name }}</v-card-title>
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
  state: string
  name: string
  category: string
  isBorrowed: boolean
  description: string
  id: number
}

const items = ref(<Item[]>[])
const showSnackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('success')
const dialogOpen = ref(false)
const selectedItem = ref<Item | null>(null)

onMounted(async () => {
  getInventoryList();
})

async function getInventoryList() {
  try {
    const response = await api.get('/api/items/')
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

async function showDetails(id: number) {
  try {
    const response = await api.get(`/api/items/${id}`)
    selectedItem.value = response.data
    dialogOpen.value = true
  } catch (error: any) {
    snackbarColor.value = 'error'
    if (error.response) {
      snackbarMessage.value = "Fehler: " + error.response.status + " - " + error.response.data?.detail
    } else {
      snackbarMessage.value = "Fehler beim Laden der Details: " + error.message
    }
    console.error(snackbarMessage.value)
    showSnackbar.value = true
  }
}

async function borrowItem(id: number) {
  try {
    await api.put(`/api/items/${id}/borrow`)
    dialogOpen.value = false
    await getInventoryList()
    snackbarColor.value = 'success'
    snackbarMessage.value = 'Gegenstand wurde erfolgreich ausgeliehen!'
    showSnackbar.value = true

  }
  catch (error: any) {
    snackbarColor.value = 'error'
    if (error.response) {
      snackbarMessage.value = "Fehler beim Ausleihen: " + error.response.status + " - " + error.response.data?.detail
    } else {
      snackbarMessage.value = "Fehler beim Ausleihen: " + error.message
    }
    console.error(snackbarMessage.value)
    showSnackbar.value = true
  }
}

const deleteDialogOpen = ref(false)
const itemToDelete = ref<any>(null)

function triggerDelete(item: Item) {
  console.log(item)
  itemToDelete.value = item
  deleteDialogOpen.value = true
}

async function confirmDelete() {
  if (!itemToDelete.value) return

  try {
    const id = itemToDelete.value.id
    await api.delete(`/api/items/${id}`)
    deleteDialogOpen.value = false

    await getInventoryList()
    snackbarColor.value = 'success'
    snackbarMessage.value = `Gegenstand "${itemToDelete.value.name}" wurde erfolgreich gelöscht.`
    showSnackbar.value = true
  } catch (error: any) {
    snackbarColor.value = 'error'
    if (error.response) {
      snackbarMessage.value = "Fehler beim Löschen: " + error.response.status + " - " + error.response.data?.detail
    }
    else {
      snackbarMessage.value = "Fehler beim Löschen: " + error.message
    }
    console.error(snackbarMessage.value)
    showSnackbar.value = true
  }
  finally {
    itemToDelete.value = null
  }
}

</script>