<script setup lang="ts">
import { ref, onMounted, onUnmounted, watch, computed } from 'vue'
import { animate } from 'popmotion'

const props = defineProps({
  id: Number,
  title: String,
  x: Number,
  y: Number,
  width: Number,
  height: Number,
  z: Number,
  gridSize: { type: Number, default: 40 },
  draggingAny: Boolean,
  onDragState: Function,
  onResizeState: Function,
  // Add boundaries for movement
  areaWidth: { type: Number, default: window.innerWidth },
  areaHeight: { type: Number, default: window.innerHeight },
  areaOffsetX: { type: Number, default: 0 },
  areaOffsetY: { type: Number, default: 0 }
})

const emit = defineEmits(['focus', 'dragging', 'resizing'])

const pos = ref({ x: props.x ?? 100, y: props.y ?? 100 })
const size = ref({ width: props.width ?? 320, height: props.height ?? 200 })
const dragging = ref(false)
const resizing = ref(false)
const dragOffset = ref({ x: 0, y: 0 })
const resizeStart = ref({ x: 0, y: 0, width: 0, height: 0 })

const gridSnap = (val: number, grid: number): number => Math.round(val / grid) * grid
const clamp = (val: number, min: number, max: number): number => Math.max(min, Math.min(max, val))

// Animate a reactive object (pos or size) to target values
function animateTo(
  current: { x: number; y: number } | { width: number; height: number },
  target: Record<string, number>,
  onUpdate: (vals: Record<string, number>) => void,
  onComplete?: () => void
): void {
  const keys = Object.keys(target)
  const from = keys.reduce(
    (acc, key) => {
      acc[key] = current[key]
      return acc
    },
    {} as Record<string, number>
  )

  animate({
    from,
    to: target,
    duration: 260,
    ease: (t) => 1 - Math.pow(1 - t, 2), // easeOutQuad
    onUpdate: (vals) => {
      onUpdate(vals)
    },
    onComplete: () => {
      if (onComplete) onComplete()
    }
  })
}

const onMouseDown = (e: MouseEvent): void => {
  dragging.value = true
  dragOffset.value = { x: e.clientX - pos.value.x, y: e.clientY - pos.value.y }
  emit('focus')
  emit('dragging', true)
  if (props.onDragState) props.onDragState(true)
}

const onMouseMove = (e: MouseEvent): void => {
  if (dragging.value) {
    // Calculate boundaries
    const minX = props.areaOffsetX
    const minY = props.areaOffsetY
    const maxX = props.areaOffsetX + props.areaWidth - size.value.width
    const maxY = props.areaOffsetY + props.areaHeight - size.value.height
    // Clamp position
    pos.value.x = clamp(e.clientX - dragOffset.value.x, minX, maxX)
    pos.value.y = clamp(e.clientY - dragOffset.value.y, minY, maxY)
  } else if (resizing.value) {
    // Clamp resizing so window doesn't go out of bounds
    const minWidth = 200
    const minHeight = 120
    const maxWidth = props.areaWidth - (pos.value.x - props.areaOffsetX)
    const maxHeight = props.areaHeight - (pos.value.y - props.areaOffsetY)
    size.value.width = clamp(
      resizeStart.value.width + (e.clientX - resizeStart.value.x),
      minWidth,
      maxWidth
    )
    size.value.height = clamp(
      resizeStart.value.height + (e.clientY - resizeStart.value.y),
      minHeight,
      maxHeight
    )
  }
}

const onMouseUp = (): void => {
  if (dragging.value) {
    const snappedX = gridSnap(pos.value.x, props.gridSize)
    const snappedY = gridSnap(pos.value.y, props.gridSize)

    if (pos.value.x !== snappedX || pos.value.y !== snappedY) {
      animateTo(
        pos.value,
        { x: snappedX, y: snappedY },
        (interpolatedValues) => {
          pos.value.x = interpolatedValues.x
          pos.value.y = interpolatedValues.y
        },
        () => {
          dragging.value = false
        }
      )
    } else {
      dragging.value = false
    }
  } else if (resizing.value) {
    const snappedWidth = gridSnap(size.value.width, props.gridSize)
    const snappedHeight = gridSnap(size.value.height, props.gridSize)
    const finalWidth = Math.max(200, snappedWidth)
    const finalHeight = Math.max(120, snappedHeight)

    if (size.value.width !== finalWidth || size.value.height !== finalHeight) {
      animateTo(
        size.value,
        { width: finalWidth, height: finalHeight },
        (interpolatedValues) => {
          size.value.width = interpolatedValues.width
          size.value.height = interpolatedValues.height
        },
        () => {
          resizing.value = false
        }
      )
    } else {
      resizing.value = false
    }
  }
  if (resizing.value) {
    emit('resizing', false)
    if (props.onResizeState) props.onResizeState(false)
  }
  if (dragging.value) {
    emit('dragging', false)
    if (props.onDragState) props.onDragState(false)
  }
}

const onResizeMouseDown = (e: MouseEvent): void => {
  e.stopPropagation()
  resizing.value = true
  resizeStart.value = {
    x: e.clientX,
    y: e.clientY,
    width: size.value.width,
    height: size.value.height
  }
  emit('focus')
  emit('resizing', true)
  if (props.onResizeState) props.onResizeState(true)
}

onMounted(() => {
  window.addEventListener('mousemove', onMouseMove)
  window.addEventListener('mouseup', onMouseUp)
})
onUnmounted(() => {
  window.removeEventListener('mousemove', onMouseMove)
  window.removeEventListener('mouseup', onMouseUp)
})

watch(dragging, (val) => {
  emit('dragging', val)
  if (props.onDragState) props.onDragState(val)
})

watch(resizing, (val) => {
  emit('resizing', val)
  if (props.onResizeState) props.onResizeState(val)
})

watch(
  () => [props.x, props.y],
  ([newX, newY]) => {
    if (!dragging.value && typeof newX === 'number' && typeof newY === 'number') {
      if (pos.value.x !== newX || pos.value.y !== newY) {
        animateTo(pos.value, { x: newX, y: newY }, (vals) => {
          pos.value.x = vals.x
          pos.value.y = vals.y
        })
      }
    }
  }
)

watch(
  () => [props.width, props.height],
  ([newW, newH]) => {
    if (!resizing.value && typeof newW === 'number' && typeof newH === 'number') {
      if (size.value.width !== newW || size.value.height !== newH) {
        animateTo(size.value, { width: newW, height: newH }, (vals) => {
          size.value.width = vals.width
          size.value.height = vals.height
        })
      }
    }
  }
)

const style = computed(() => ({
  left: pos.value.x + 'px',
  top: pos.value.y + 'px',
  width: size.value.width + 'px',
  height: size.value.height + 'px',
  zIndex: props.z
}))
</script>

<template>
  <div class="floating-window" :style="style" tabindex="0" @mousedown="emit('focus')">
    <div class="window-titlebar" @mousedown.stop.prevent="onMouseDown">
      <slot name="title">Window</slot>
    </div>
    <div class="window-content">
      <slot />
    </div>
    <div class="resize-handle" @mousedown.stop.prevent="onResizeMouseDown"></div>
  </div>
</template>

<style scoped>
.floating-window {
  position: absolute;
  background: rgba(40, 44, 52, 0.85);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  border-radius: 16px;
  border: 1.5px solid rgba(255, 255, 255, 0.12);
  overflow: hidden;
  user-select: none;
  transition: box-shadow 0.2s;
  min-width: 200px;
  min-height: 120px;
  backdrop-filter: blur(8px) saturate(1.2);
}

.floating-window:focus {
  outline: 2px solid #6988e6;
  box-shadow:
    0 0 0 2px #6988e6,
    0 8px 32px 0 rgba(31, 38, 135, 0.37);
}

.window-titlebar {
  height: 38px;
  background: linear-gradient(90deg, rgba(60, 70, 100, 0.7) 0%, rgba(80, 90, 120, 0.5) 100%);
  color: #fff;
  font-weight: 600;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  padding: 0 18px;
  cursor: move;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  letter-spacing: 0.01em;
}

.window-content {
  padding: 18px;
  color: #eaeaea;
  font-size: 1rem;
  height: calc(100% - 38px);
  overflow: auto;
}

.resize-handle {
  position: absolute;
  right: 0;
  bottom: 0;
  width: 18px;
  height: 18px;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.08) 0%, rgba(80, 90, 120, 0.18) 100%);
  cursor: se-resize;
  border-bottom-right-radius: 14px;
}
</style>
