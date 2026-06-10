<template>
  <v-app>
    <v-main>
      <h1>Test</h1>
      <h3>Dialog</h3>
      <v-btn color="primary" @click="openDialog()">
        Zeige Dialog
      </v-btn>

      <v-dialog width="500" v-model="dialogActive">
        <v-card title="Dialog">
          <v-card-text>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
            dolore magna aliqua.
          </v-card-text>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn text="Schließen" @click="dialogActive = false"></v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-checkbox label="Zähltext anzeigen" v-model="showCountTextChecked"></v-checkbox>
      <div v-if="showCountTextChecked">Du hast den Dialog {{ dialogCount }}x aufgerufen.</div>

      <!--my4: Margin Top/Bottom: 4/16-->
      <v-divider class="my-4"></v-divider>
      <h3>Liste</h3>

      <v-row>
        <v-col cols="11"><v-text-field v-model="newItemText" label="Neues Item"></v-text-field></v-col>
        <v-col cols="1"><v-btn block @click="addItem()">+</v-btn></v-col>
      </v-row>
      <div>Eingegeben: {{ newItemText }}</div>

      <v-list>
        <v-list-item v-for="item in items">
          -> {{ item }}
        </v-list-item>
      </v-list>

    </v-main>
  </v-app>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const dialogActive = ref(false)
var dialogCount = ref(0)
var showCountTextChecked = ref(true)

var newItemText = ref("")
var items = ref<string[]>([])

function openDialog() {
  dialogCount.value++
  dialogActive.value = true
}

function addItem() {
  if (newItemText.value.trim() === '') return // nichts eingegeben

  items.value.push(newItemText.value)
  newItemText.value = '' // Reset
}

</script>