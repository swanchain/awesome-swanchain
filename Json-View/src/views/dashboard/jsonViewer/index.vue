<template>
  <section id="jsonViewer">
    <div class="title">JSON viewer component</div>
    <el-row class="json_body" justify="space-between">
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12">
        <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" class="demo-ruleForm" status-icon>
          <el-form-item label="" prop="jsonValue">
            <el-input v-model="ruleForm.jsonValue" :rows="10" type="textarea" placeholder="" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm(ruleFormRef)">
              Format
            </el-button>
            <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
          </el-form-item>
        </el-form>
      </el-col>
      <el-col :xs="24" :sm="24" :md="24" :lg="12" :xl="12">
        <json-viewer :value="jsonData.data" :expand-depth=5 copyable boxed sort></json-viewer>
      </el-col>
    </el-row>
  </section>
</template>

<script>
import { defineComponent, computed, onMounted, watch, ref, reactive, getCurrentInstance } from 'vue'
import { useStore } from "vuex"
import { useRouter, useRoute } from 'vue-router'
import JsonViewer from 'vue-json-viewer'
export default defineComponent({
  name: 'Json Viewer',
  components: {
    JsonViewer
  },
  setup () {
    const store = useStore()
    const bodyWidth = ref(document.body.clientWidth < 992)
    const system = getCurrentInstance().appContext.config.globalProperties
    const route = useRoute()
    const router = useRouter()
    const jsonData = reactive({
      data: {}
    })
    const ruleForm = reactive({
      jsonValue: ''
    })
    const validateInput = (rule, value, callback) => {
      if (!type(value)) {
        callback(new Error("Please enter a JSON string"));
      } else {
        callback();
      }
    }
    const rules = reactive({
      jsonValue: [
        { required: true, message: ' ', trigger: 'blur' },
        { validator: validateInput, trigger: "blur" }
      ]
    })
    const ruleFormRef = ref(null)

    const type = (str) => {
      if (typeof str == 'string') {
        try {
          var obj = JSON.parse(str);
          if (typeof obj == 'object' && obj) return true
          else return false;
        } catch (e) {
          return false
        }
      }
      return false
    }
    const submitForm = async (formEl) => {
      if (!formEl) return
      await ruleFormRef.value.validate(async (valid, fields) => {
        if (valid) {
          jsonData.data = JSON.parse(ruleForm.jsonValue)
        } else {
          console.log('error submit!', fields)
          jsonData.data = {}
          return false
        }
      })
    }
    const resetForm = (formEl) => {
      if (!formEl) return
      ruleFormRef.value.resetFields()
      jsonData.data = {}
    }
    onMounted(() => { })
    return {
      system,
      ruleForm,
      rules,
      ruleFormRef,
      jsonData,
      submitForm, resetForm
    }
  }
})
</script>

<style lang="scss" scoped>
#jsonViewer {
  padding: 0.2rem;
  max-width: 1460px;
  margin: auto;
  font-size: 18px;
  @media screen and (max-width: 1200px) {
    font-size: 16px;
  }
  .title {
    padding: 0.2rem 0 0.3rem;
  }
  :deep(.json_body) {
    display: flex;
    align-items: stretch;
    .el-col {
      .jv-container {
        min-height: 100%;
      }
    }
  }
}
</style>


<i18n>
{
  "en": {
    "step": "Step"
  },
  "zh": {
    "step": "步骤"
  }
}
</i18n>
