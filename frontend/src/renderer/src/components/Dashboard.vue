<script setup lang="ts">
import { reactive, ref, onMounted, onUnmounted, computed } from 'vue'
import FloatingWindow from './FloatingWindow.vue'
import GridOverlay from './GridOverlay.vue'
import Sidebar from './Sidebar.vue'
import Header from './Header.vue'

// --- Tab state ---
const tabs = [
  { id: 'dashboard', label: 'Dashboard', icon: '📊' },
  { id: 'settings', label: 'Settings', icon: '⚙️' },
  { id: 'about', label: 'About', icon: 'ℹ️' },
  { id: 'tab1', label: 'Tab 1', icon: '🗂️' },
  { id: 'tab2', label: 'Tab 2', icon: '📝' },
  { id: 'tab3', label: 'Tab 3', icon: '📁' },
  { id: 'tab4', label: 'Tab 4', icon: '📦' },
  { id: 'tab5', label: 'Tab 5', icon: '🔧' },
  { id: 'tab6', label: 'Tab 6', icon: '🧩' },
  { id: 'tab7', label: 'Tab 7', icon: '🖼️' },
  { id: 'tab8', label: 'Tab 8', icon: '🎨' },
  { id: 'tab9', label: 'Tab 9', icon: '🧪' },
  { id: 'tab10', label: 'Tab 10', icon: '🛠️' },
  { id: 'tab11', label: 'Tab 11', icon: '🧬' },
  { id: 'tab12', label: 'Tab 12', icon: '🧭' },
  { id: 'tab13', label: 'Tab 13', icon: '🧲' },
  { id: 'tab14', label: 'Tab 14', icon: '🧱' },
  { id: 'tab15', label: 'Tab 15', icon: '🧯' }
]
const activeTab = ref('dashboard')
const activeTabLabel = computed(() => tabs.find((t) => t.id === activeTab.value)?.label || '')

// --- Windows and grid logic ---
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
const resizingAny = ref(false)

const bringToFront = (id: number): void => {
  const maxZ = Math.max(...windows.map((w) => w.z))
  const win = windows.find((w) => w.id === id)
  if (win) win.z = maxZ + 1
}

const handleDragging = (isDragging: boolean): void => {
  draggingAny.value = isDragging
}

const handleResizing = (isResizing: boolean): void => {
  resizingAny.value = isResizing
}

function autoArrangeWindows(): void {
  // Calculate area for windows
  const areaWidth = windowWidth.value - sidebarWidth.value
  // const areaHeight = windowHeight.value - headerHeight // not used
  const count = windows.length
  if (count === 0) return

  // Sort windows left-to-right, top-to-bottom by current y then x
  const sorted = [...windows].sort((a, b) => a.y - b.y || a.x - b.x)

  // Try to fit as many windows per row as possible, keeping their width
  let x = 40
  let y = 40
  let maxRowHeight = 0
  const padding = 24

  for (const win of sorted) {
    // If window would overflow, move to next row
    if (x + win.width > areaWidth) {
      x = 40
      y += maxRowHeight + padding
      maxRowHeight = 0
    }
    // Always set to a new value to force reactivity
    win.x = x + Math.random() * 0.001 // force change
    win.y = y + Math.random() * 0.001 // force change
    x += win.width + padding
    if (win.height > maxRowHeight) maxRowHeight = win.height
  }
}

// --- Sidebar resizing logic ---
const sidebarWidth = ref(220)
const minSidebarWidth = 120
const maxSidebarWidth = 400
const resizingSidebar = ref(false)
const sidebarResizeStart = ref({ x: 0, width: 220 })

const onSidebarResizeMouseDown = (e: MouseEvent): void => {
  resizingSidebar.value = true
  sidebarResizeStart.value = { x: e.clientX, width: sidebarWidth.value }
  document.body.style.cursor = 'ew-resize'
}

const onSidebarResizeMouseMove = (e: MouseEvent): void => {
  if (resizingSidebar.value) {
    const newWidth = sidebarResizeStart.value.width + (e.clientX - sidebarResizeStart.value.x)
    sidebarWidth.value = Math.max(minSidebarWidth, Math.min(maxSidebarWidth, newWidth))
  }
}

const onSidebarResizeMouseUp = (): void => {
  if (resizingSidebar.value) {
    resizingSidebar.value = false
    document.body.style.cursor = ''
  }
}

// --- Window size and grid area ---
const windowWidth = ref(window.innerWidth)
const windowHeight = ref(window.innerHeight)
const headerHeight = 56

const updateWindowSize = (): void => {
  windowWidth.value = window.innerWidth
  windowHeight.value = window.innerHeight
}

onMounted(() => {
  window.addEventListener('mousemove', onSidebarResizeMouseMove)
  window.addEventListener('mouseup', onSidebarResizeMouseUp)
  window.addEventListener('resize', updateWindowSize)
})
onUnmounted(() => {
  window.removeEventListener('mousemove', onSidebarResizeMouseMove)
  window.removeEventListener('mouseup', onSidebarResizeMouseUp)
  window.removeEventListener('resize', updateWindowSize)
})
</script>

<template>
  <div class="dashboard-layout">
    <Sidebar v-model:active-tab="activeTab" :style="{ width: sidebarWidth + 'px' }" />
    <div
      class="sidebar-resize-handle"
      :style="{
        position: 'absolute',
        top: '0',
        left: sidebarWidth + 'px',
        width: '5px',
        height: '100%',
        cursor: 'ew-resize',
        zIndex: 20
      }"
      @mousedown="onSidebarResizeMouseDown"
    ></div>
    <div class="main-area" :style="{ marginLeft: sidebarWidth + 'px' }">
      <Header :title="activeTabLabel" @auto-arrange="autoArrangeWindows" />
      <div class="dashboard-content">
        <GridOverlay
          :grid-size="gridSize"
          :visible="draggingAny || resizingAny"
          :width="windowWidth - sidebarWidth"
          :height="windowHeight - headerHeight"
          style="position: absolute; left: 0; top: 0"
        />
        <div class="windows-area">
          <FloatingWindow
            v-for="win in windows"
            :key="win.id"
            v-bind="win"
            :grid-size="gridSize"
            :dragging-any="draggingAny"
            :on-drag-state="handleDragging"
            :on-resize-state="handleResizing"
            :area-width="windowWidth - sidebarWidth"
            :area-height="windowHeight - headerHeight"
            :area-offset-x="0"
            :area-offset-y="0"
            @mousedown="bringToFront(win.id)"
            @focus="bringToFront(win.id)"
            @dragging="handleDragging"
            @resizing="handleResizing"
          >
            <template #title>{{ win.title }}</template>
            <template #default>{{ win.content }}</template>
          </FloatingWindow>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-layout {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}
.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}
.dashboard-content {
  position: relative;
  flex: 1;
  width: 100%;
  height: calc(100vh - 56px);
  background: rgba(30, 34, 44, 0.95);
  overflow: hidden;
}
.windows-area {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  pointer-events: auto;
}
.sidebar-resizer {
  background: rgba(255, 255, 255, 0.1);
}
.sidebar-resize-handle {
  background: transparent;
  transition: background 0.2s;
}
.sidebar-resize-handle:hover {
  background: rgba(255, 255, 255, 0.08);
}
</style>
