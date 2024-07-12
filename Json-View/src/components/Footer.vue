<template></template>

<script>
import { defineComponent, computed, onMounted, watch, ref, reactive, getCurrentInstance } from 'vue'
import { useStore } from "vuex"
import { useRouter, useRoute } from 'vue-router'
export default defineComponent({
    name: 'footer_page',
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

<style  lang="scss" scoped>
.footer {
  position: relative;
  width: 90%;
  // background-color: #0e1e38;
  padding: 0.1rem 5%;
  color: #fff;
  p {
    font-size: 0.13rem;
    color: #fafafa;
    white-space: nowrap;
    line-height: 1.3;
    text-align: left;
    @media screen and (max-width: 600px) {
      font-size: 12px;
    }
    @media screen and (max-height: 789px) {
      font-size: 12px;
    }
  }
  .footer_menu {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin: 0.05rem auto;
    a {
      padding: 0 0.16rem 0 0;
      color: #fff;
      font-size: 0.195rem;
      line-height: 1;
      @media screen and (max-height: 789px) {
        padding: 0 0.1rem 0 0;
      }
      svg {
        width: 32px;
        height: 32px;
        cursor: pointer;
        @media screen and (max-height: 789px) {
          width: 25px;
          height: 25px;
        }
      }
    }
  }
}
.footer_position {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
}
</style>

<i18n>
{
  "en": {
    "copy": "All rights reserved © 2022 Nebula AI."
  },
  "zh": {
    "copy": "©2022 Nebula AI. 保留所有权利"
  }
}
</i18n>