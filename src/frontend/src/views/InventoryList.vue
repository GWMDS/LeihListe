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
      <v-card>
        <v-card-title>{{ item.name }}</v-card-title>
        <v-card-text>
          ID: {{ item.id }}<br>
          Kategorie: {{ item.category }}<br>
          State: {{ item.state }}<br>
          Status: {{ item.status }}<br>
          Beschreibung: {{ item.description }}
        </v-card-text>

        <v-card-actions>
          <v-btn>Details</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
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

const items = ref(<Item[]>[])
async function getInventoryList() {
  try {
    const response = await api.get('/api/items')
    items.value = response.data
    console.log(response.data)
  } catch (error: any) {
    if (error.response) {
      console.error("Fehler: " + error.response.status + " - " + error.response.data?.detail)
    } else {
      console.error("Fehler: " + error)
    }
  }
}

</script>