<template>
  <v-app>
    <v-main>
      <v-bottom-navigation>
        <router-link to="/">Home</router-link>
        <router-link to="/test">Test</router-link>
      </v-bottom-navigation>
      <router-view />
    </v-main>
  </v-app>
  
</template>

<script setup lang="ts">

</script>

<style scoped>

</style>
