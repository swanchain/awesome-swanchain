<template>

</template>
<script>
import { defineComponent, computed, onMounted, watch, ref, reactive, getCurrentInstance } from 'vue'
import { useStore } from "vuex"
import { useRouter, useRoute } from 'vue-router'
export default defineComponent({
    name: 'header_page',
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
.headerCont {
  min-height: 0.8rem;
  .header {
    height: 0.8rem;
    padding: 0 5%;
    // background-color: #0d1e39;
    // box-shadow: 0 1px 4px 0 rgba(35, 35, 35, 0.16);
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
    font-size: 0.16rem;
    -webkit-transition: position 0.4s, padding 0s;
    transition: position 0.4s, padding 0s;
    .logoImg {
      display: flex;
      align-items: center;
      width: auto;
      height: 0.3rem;
      cursor: pointer;
      img {
        display: block;
        height: 100%;
        width: auto;
        max-width: 100%;
        margin: auto;
      }
      span {
        margin: 5px 0 0;
        font-size: 0.17rem;
        font-weight: 600;
        color: #fafafb;
        letter-spacing: 5px;
      }
    }
    .header_right {
      display: flex;
      align-items: center;
      .lang_style {
        line-height: 0.4rem;
        font-size: 0.16rem;
        font-weight: 500;
        color: #fafafb;
        span {
          padding: 0 0.02rem;
          cursor: pointer;
          color: inherit;
          &:hover {
            font-weight: 600;
          }
        }
        .langChild {
          color: #007bff;
        }
      }
    }
  }
  .header_scroll {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    // box-shadow: 0 2px 4px rgba(16, 28, 79, 0.5);
    z-index: 999;
  }
}

@media screen and (max-width: 1024px) {
}
@media screen and (max-width: 441px) {
  .headerCont {
    .header {
      padding: 0 2%;
      .logoImg {
        width: 50%;
        height: auto;
        img {
          width: 100%;
          height: auto;
        }
      }
    }
  }
}
</style>
