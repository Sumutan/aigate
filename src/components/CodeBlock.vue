<template>
  <div class="relative group">
    <div class="code-block text-left" v-html="html"></div>
    <button @click="copy"
      class="absolute top-3 right-3 px-3 py-1.5 rounded-md text-xs font-medium transition
             opacity-0 group-hover:opacity-100 focus:opacity-100"
      :class="copied ? 'bg-green-500/20 text-green-300' : 'bg-white/10 text-gray-400 hover:bg-white/20 hover:text-white'">
      {{ copied ? '已复制' : '复制' }}
    </button>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({ html: String, raw: String })
const copied = ref(false)

const copy = async () => {
  try {
    await navigator.clipboard.writeText(props.raw)
  } catch {
    const ta = document.createElement('textarea')
    ta.value = props.raw
    ta.style.position = 'fixed'
    ta.style.opacity = '0'
    document.body.appendChild(ta)
    ta.select()
    document.execCommand('copy')
    document.body.removeChild(ta)
  }
  copied.value = true
  setTimeout(() => { copied.value = false }, 2000)
}
</script>
