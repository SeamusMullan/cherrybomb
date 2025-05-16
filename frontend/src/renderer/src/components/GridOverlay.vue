<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps({
  gridSize: { type: Number, default: 40 },
  visible: { type: Boolean, default: false },
  width: { type: Number, default: window.innerWidth },
  height: { type: Number, default: window.innerHeight }
})

const cols = computed(() => Math.ceil(props.width / props.gridSize))
const rows = computed(() => Math.ceil(props.height / props.gridSize))
</script>

<template>
  <div v-if="visible" class="grid-overlay">
    <svg :width="width" :height="height" class="grid-svg">
      <g>
        <template v-for="r in rows" :key="`row-${r}`">
          <circle
            v-for="c in cols"
            :key="`${r}-${c}`"
            :cx="(c - 1) * gridSize"
            :cy="(r - 1) * gridSize"
            r="3"
            fill="#fff3"
          />
        </template>
      </g>
    </svg>
  </div>
</template>

<style scoped>
.grid-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 10;
}
.grid-svg {
  width: 100vw;
  height: 100vh;
  display: block;
}
</style>
