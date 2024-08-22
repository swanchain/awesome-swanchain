<template>
    <div class="dashboard">
        <router-view v-slot="{ Component }">
            <transition name="appFade" mode="out-in">
                <keep-alive>
                    <component :is="Component" />
                </keep-alive>
            </transition>
        </router-view>
    </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'Dashboard'
})
</script>

<style lang="scss" scoped>
.dashboard {
  box-sizing: border-box;
  padding: 0;
  font-size: 0.2rem;
}

.appFade-enter-active,
.appFade-leave-active {
  transition: opacity 0.3s;
}
.appFade-enter,
.appFade-leave-to {
  opacity: 0;
}
</style>