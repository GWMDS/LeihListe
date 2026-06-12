<template>
  <h1>Inventarliste</h1>
  <v-btn color="primary" @click="getInventoryList()" class="mt-4">
    Liste holen
  </v-btn>
  <v-row class="mt-4">
    <!--
    cols="12": 12/12 (volle Breite)
    sm="6"   : 6/12 (2 Spalten)
    md="4"   : 4/12 (3 Spalten)
    lg="3"   : 3/12 (4 Spalten)
    -->
    <v-col v-for="item in items" cols="12" sm="6" md="4" lg="3">
      <v-card :disabled="item.status">
        <v-card-title>{{ item.name }}</v-card-title>
        <v-card-text>
          ID: {{ item.id }}<br>
          Kategorie: {{ item.category }}<br>
          Zustand: {{ item.state }}<br>
          Status: {{ item.status }}<br>
          Beschreibung: {{ item.description }}
        </v-card-text>
        <v-card-actions>
          <v-btn>Details</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>

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
import { ref } from 'vue'
import api from '../api.ts'

interface Item {
  state: string
  name: string
  category: string
  status: boolean
  description: string
  id: number
}

const items = [
  {
    id: 0,
    name: "Laptop",
    category: "electronics",
    description: "Dell Latitude 5420",
    state: "new",
    status: false
  },
  {
    id: 1,
    name: "Java Buch",
    category: "books",
    description: "Einführung in Java",
    state: "used",
    status: false
  },
  {
    id: 2,
    name: "Beamer",
    category: "electronics",
    description: "HD-Projektor für Präsentationen",
    state: "borrowed",
    status: true
  },
  {
    id: 3,
    name: "Tastatur",
    category: "electronics",
    description: "Mechanische Tastatur",
    state: "used",
    status: false
  },
  {
    id: 4,
    name: "Maus",
    category: "electronics",
    description: "Kabellose Maus",
    state: "new",
    status: false
  },
  {
    id: 5,
    name: "Monitor",
    category: "electronics",
    description: "24 Zoll Full-HD Monitor",
    state: "used",
    status: false
  },
  {
    id: 6,
    name: "Netzteil",
    category: "electronics",
    description: "65W USB-C Netzteil",
    state: "new",
    status: false
  },
  {
    id: 7,
    name: "Whiteboard Marker",
    category: "office",
    description: "Set aus vier Farben",
    state: "new",
    status: false
  },
  {
    id: 8,
    name: "HDMI Kabel",
    category: "electronics",
    description: "2 Meter HDMI 2.1",
    state: "used",
    status: false
  },
  {
    id: 9,
    name: "Rucksack",
    category: "general",
    description: "Schwarzer Laptop-Rucksack",
    state: "used",
    status: false
  }
]
const showError = ref(false)
const errorMessage = ref('')

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

</script>