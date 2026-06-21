<template>
  <v-app>
    <v-app-bar title="LeihListe" />
    <v-main>
      <v-container min-width="100%">
        <router-view />
      </v-container>
    </v-main>

    <v-bottom-navigation v-model="activeTab" color="primary">
      <v-btn to="/">Inventar <v-icon>mdi-home</v-icon></v-btn>
      <v-btn to="/overview">Übersicht <v-icon>mdi-format-list-bulleted</v-icon></v-btn>
      <v-btn to="/settings">Einstellungen <v-icon>mdi-cog</v-icon></v-btn>
      <v-btn to="/test">Test </v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const activeTab = ref('home')

</script>

<style></style>
