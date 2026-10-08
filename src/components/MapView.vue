<script setup>
import { onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

onMounted(() => {
  const map = L.map('map').setView([46.2044, 6.1432], 13)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map)
})
</script>

<template>
  <div id="map"></div>
</template>

<style scoped>
#map {
  height: 600px;
  width: 100%;
}
</style>
