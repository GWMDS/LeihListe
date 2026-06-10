<template>
  <v-app>
    <v-main>
      <h1>Home</h1>
      <v-btn color="primary" @click="Test">
        API GET Test
      </v-btn>
    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import api from '../api.ts'

async function Test() {
  try {
    const response = await api.get('/')
    console.log(response.data)
  } catch (error: any) {
    console.error("Status: " + error.response.status)
    console.error("Data Detail: " + error.response.data.detail)
  }
}

</script>