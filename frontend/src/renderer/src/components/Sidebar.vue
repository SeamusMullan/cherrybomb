<template>
  <aside class="sidebar">
    <div class="sidebar-top">
      <span class="sidebar-logo">
        <svg viewBox="0 0 32 32" width="28" height="28" fill="none">
          <circle cx="16" cy="16" r="16" fill="#FF4C60" />
          <text
            x="16"
            y="21"
            text-anchor="middle"
            font-size="14"
            fill="#fff"
            font-family="sans-serif"
            font-weight="bold"
          >
            CB
          </text>
        </svg>
      </span>
      <span class="sidebar-profile">
        <img src="https://i.pravatar.cc/32?u=cherrybomb" alt="Profile" />
      </span>
    </div>
    <nav class="tab-list">
      <button
        v-for="tab in tabs"
        :key="tab.id"
        :class="['tab-btn', { active: tab.id === activeTab }]"
        @click="selectTab(tab.id)"
      >
        <span v-if="tab.icon" class="tab-icon">{{ tab.icon }}</span>
        <span class="tab-label">{{ tab.label }}</span>
      </button>
    </nav>
    <slot />
  </aside>
</template>

<script setup lang="ts">
import { ref, defineEmits } from 'vue'

const emit = defineEmits(['update:activeTab'])

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
const selectTab = (id: string): void => {
  activeTab.value = id
  emit('update:activeTab', id)
}
</script>

<style scoped>
.sidebar {
  width: 220px;
  height: 100vh;
  background: #232634;
  color: #fff;
  display: flex;
  flex-direction: column;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.08);
  z-index: 10;
  padding-top: 0;
  position: fixed;
  left: 0;
  top: 0;
}
.sidebar-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 16px 8px 16px;
  min-height: 56px;
}
.sidebar-logo {
  display: flex;
  align-items: center;
}
.sidebar-profile img {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: 2px solid #35384a;
}
.tab-list {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 24px;
  overflow-y: auto;
  padding: 0 8px 8px 8px;
}
.tab-btn {
  background: none;
  border: none;
  color: #fff;
  text-align: left;
  padding: 12px 20px;
  font-size: 1rem;
  font-family: inherit;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  transition: background 0.15s;
}
.tab-btn.active,
.tab-btn:hover {
  background: #35384a;
}
.tab-icon {
  font-size: 1.2em;
  width: 1.5em;
  display: flex;
  align-items: center;
  justify-content: center;
}
.tab-label {
  flex: 1;
}
</style>
