<template>
  <header class="header">
    <span class="title-text">{{ title }}</span>
    <button class="auto-arrange-btn" title="Auto Arrange Windows" @click="$emit('autoArrange')">
      <svg width="22" height="22" viewBox="0 0 22 22" fill="none">
        <rect x="2" y="2" width="7" height="7" rx="2" fill="#fff" fill-opacity="0.8" />
        <rect x="13" y="2" width="7" height="7" rx="2" fill="#fff" fill-opacity="0.5" />
        <rect x="2" y="13" width="7" height="7" rx="2" fill="#fff" fill-opacity="0.5" />
        <rect x="13" y="13" width="7" height="7" rx="2" fill="#fff" fill-opacity="0.8" />
      </svg>
    </button>
  </header>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'

defineProps<{ title: string }>()
defineEmits(['autoArrange'])
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
  position: relative;
}
.title-text {
  font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
  font-size: 1.2rem;
  font-weight: 600;
  color: #fff;
}
.auto-arrange-btn {
  margin-left: auto;
  background: none;
  border: none;
  cursor: pointer;
  padding: 6px 10px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  transition: background 0.15s;
}
.auto-arrange-btn:hover {
  background: #35384a;
}
.auto-arrange-btn svg {
  display: block;
}
</style>
