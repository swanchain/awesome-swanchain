<template>
    <div class="wrapper" id="wrapper" ref="area">
        <div class="content">
            <router-view v-slot="{ Component }">
                <transition name="move" mode="out-in">
                    <keep-alive>
                        <component :is="Component" />
                    </keep-alive>
                </transition>
            </router-view>
        </div>
    </div>
</template>

<script>
import { defineComponent, computed, onMounted, watch, ref, reactive, getCurrentInstance } from 'vue'
import { useStore } from "vuex"
import { useRouter, useRoute } from 'vue-router'
export default defineComponent({
    name: 'Home',
    components: {},
    setup () {
        const store = useStore()
        const bodyWidth = ref(document.body.clientWidth < 992)
        const system = getCurrentInstance().appContext.config.globalProperties
        const route = useRoute()
        const router = useRouter()

        onMounted(() => { })
        watch(route, (to, from) => { })
        return {
            system
        }
    }
})
</script>

<style lang="scss" scoped>
.wrapper {
  .content {
    .el-backtop {
      background-color: #45a2ff;
    }
    .el-backtop,
    .el-calendar-table td.is-today {
      color: #fff;
    }
  }
  &::-webkit-scrollbar-track {
    background: #f7f7f7;
  }
  &::-webkit-scrollbar {
    width: 6px;
    background: #ccc;
  }
  &::-webkit-scrollbar-thumb {
    background: #ccc;
  }
}
</style>