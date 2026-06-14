<template>
  <v-app>
    <v-app-bar title="LeihListe" />
    <v-main>
      <v-container min-width="100%">
        <router-view />
      </v-container>
    </v-main>

    <v-bottom-navigation>
      <v-btn to="/">Inv. Liste</v-btn>
      <v-btn to="/test">Test</v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script setup lang="ts">

</script>

<style></style>
