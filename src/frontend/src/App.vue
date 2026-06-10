<template>
  <v-app>
    <v-app-bar title="LeihListe" />
    <v-main>
      <v-container>
        <router-view />
      </v-container>
    </v-main>

    <v-bottom-navigation>
      <v-btn to="/">Home</v-btn>
      <v-btn to="/test">Test</v-btn>
    </v-bottom-navigation>
  </v-app>
</template>

<script setup lang="ts">

</script>

<style></style>
