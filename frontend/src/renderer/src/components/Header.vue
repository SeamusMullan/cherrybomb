<template>
  <header class="header">
    <span class="title-text">{{ title }}</span>
  </header>
</template>

<script setup lang="ts">
import { defineProps } from 'vue'

defineProps<{ title: string }>()
</script>

<style scoped>
.header {
  width: 100%;
  height: 56px;
  background: #232634;
  color: #fff;
  display: flex;
  align-items: center;
  padding: 0 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  z-index: 20;
}
.title-text {
  font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  color: #fff;
}
</style>
