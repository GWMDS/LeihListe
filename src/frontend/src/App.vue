<template>
  <v-app>
    <v-app-bar title="LeihListe">
      <v-btn @click="theme.toggle()"><v-icon size="x-large">mdi-theme-light-dark</v-icon></v-btn>
    </v-app-bar>
    <v-main>
      <v-container min-width="100%">
        <router-view />
      </v-container>
    </v-main>

    <v-bottom-navigation v-model="activeTab" color="primary">
      <v-btn to="/">Inventar <v-icon>mdi-home</v-icon></v-btn>
      <v-btn to="/overview">Übersicht <v-icon>mdi-format-list-bulleted</v-icon></v-btn>
      <v-btn to="/settings">Einstellungen <v-icon>mdi-cog</v-icon></v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useTheme } from 'vuetify'

const activeTab = ref('home')
const theme = useTheme()

</script>

<style></style>
