<script setup lang="ts">
import { reactive, ref, onMounted, onUnmounted } from 'vue'
import FloatingWindow from './FloatingWindow.vue'
import GridOverlay from './GridOverlay.vue'

const windows = reactive([
  {
    id: 1,
    title: 'Window 1',
    content: 'This is window 1',
    x: 80,
    y: 80,
    width: 340,
    height: 220,
    z: 1
  },
  {
    id: 2,
    title: 'Window 2',
    content: 'This is window 2',
    x: 220,
    y: 180,
    width: 320,
    height: 200,
    z: 2
  }
])

const gridSize = 40
const draggingAny = ref(false)

const bringToFront = (id: number): void => {
  const maxZ = Math.max(...windows.map((w) => w.z))
  const win = windows.find((w) => w.id === id)
  if (win) win.z = maxZ + 1
}

const handleDragging = (isDragging: boolean): void => {
  draggingAny.value = isDragging
}

// --- Add reactivity for window size ---
const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)

const updateWindowSize = (): void => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}

onMounted(() => {
  window.addEventListener('resize', updateWindowSize)
})
onUnmounted(() => {
  window.removeEventListener('resize', updateWindowSize)
})
</script>

<template>
  <div class="dashboard">
    <GridOverlay
      :grid-size="gridSize"
      :visible="draggingAny"
      :width="windowWidth"
      :height="windowHeight"
    />
    <FloatingWindow
      v-for="win in windows"
      :key="win.id"
      v-bind="win"
      :grid-size="gridSize"
      :dragging-any="draggingAny"
      :on-drag-state="handleDragging"
      @mousedown="bringToFront(win.id)"
      @focus="bringToFront(win.id)"
      @dragging="handleDragging"
    >
      <template #title>{{ win.title }}</template>
      <template #default>{{ win.content }}</template>
    </FloatingWindow>
  </div>
</template>

<style scoped>
.dashboard {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  background: rgba(30, 34, 44, 0.95);
}
</style>
