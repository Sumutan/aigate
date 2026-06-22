<template>
  <div class="min-h-screen bg-[#F8FAFC]">
    <!-- Nav -->
    <nav class="fixed top-0 left-0 right-0 z-50 bg-white/80 backdrop-blur-md border-b border-[#E2E8F0]">
      <div class="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-[#818cf8] to-[#6366f1] flex items-center justify-center text-white font-bold text-sm">A</div>
          <span class="text-xl font-bold text-[#1E293B]">AIGate</span>
        </div>
        <div class="hidden md:flex items-center gap-8 text-sm text-[#64748B]">
          <a href="#features" class="hover:text-[#2563EB] transition">功能</a>
          <a href="#models" class="hover:text-[#2563EB] transition">模型</a>
          <a href="#pricing" class="hover:text-[#2563EB] transition">定价</a>
          <a href="#api" class="hover:text-[#2563EB] transition">API</a>
          <a href="/login" class="bg-[#2563EB] text-white px-5 py-2 rounded-lg hover:bg-[#1D4ED8] transition">登录</a>
        </div>
      </div>
    </nav>

    <!-- Hero -->
    <section class="pt-32 pb-20 px-6">
      <div class="max-w-4xl mx-auto text-center">
        <h1 class="text-5xl md:text-6xl font-extrabold text-[#1E293B] leading-tight">
          企业级AI模型网关
        </h1>
        <p class="mt-6 text-xl text-[#64748B] max-w-2xl mx-auto" style="margin-inline:auto">
          统一接口，聚合多源大模型，兼容OpenAI协议，开箱即用
        </p>
        <div class="mt-10 flex gap-4 justify-center">
          <a href="/login" class="bg-[#2563EB] text-white px-8 py-3 rounded-xl text-lg font-semibold hover:bg-[#1D4ED8] transition shadow-lg shadow-blue-200">立即开始</a>
          <a href="#api" class="border border-[#E2E8F0] text-[#1E293B] px-8 py-3 rounded-xl text-lg font-semibold hover:border-[#2563EB] hover:text-[#2563EB] transition">查看文档</a>
        </div>
      </div>
    </section>

    <!-- Quick Start Code -->
    <section class="pb-20 px-6">
      <div class="max-w-3xl mx-auto">
        <CodeBlock :html="pythonCode" :raw="pythonRaw" />
      </div>
    </section>

    <!-- Features -->
    <section id="features" class="py-20 px-6 bg-white">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-[#1E293B]">核心功能</h2>
        <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="p-8 rounded-2xl border border-[#E2E8F0] hover:shadow-lg transition">
            <div class="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center text-[#2563EB] text-2xl mb-4">⚡</div>
            <h3 class="text-xl font-semibold text-[#1E293B]">统一接口</h3>
            <p class="mt-3 text-[#64748B]">OpenAI协议兼容，一行代码切换模型供应商，无需修改业务代码</p>
          </div>
          <div class="p-8 rounded-2xl border border-[#E2E8F0] hover:shadow-lg transition">
            <div class="w-12 h-12 bg-purple-50 rounded-xl flex items-center justify-center text-[#6366F1] text-2xl mb-4">🔒</div>
            <h3 class="text-xl font-semibold text-[#1E293B]">安全可控</h3>
            <p class="mt-3 text-[#64748B]">企业级权限管理，Token配额控制，用量审计追踪，数据不外泄</p>
          </div>
          <div class="p-8 rounded-2xl border border-[#E2E8F0] hover:shadow-lg transition">
            <div class="w-12 h-12 bg-green-50 rounded-xl flex items-center justify-center text-[#16A34A] text-2xl mb-4">📊</div>
            <h3 class="text-xl font-semibold text-[#1E293B]">智能调度</h3>
            <p class="mt-3 text-[#64748B]">多渠道负载均衡，自动故障转移，按组分配模型资源</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Models -->
    <section id="models" class="py-20 px-6">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-[#1E293B]">支持模型</h2>
        <p class="mt-4 text-center text-[#64748B]">聚合全球顶尖大模型，按需选用</p>
        <div class="mt-12 grid grid-cols-2 md:grid-cols-4 gap-4">
          <div v-for="model in models" :key="model" class="p-4 bg-white rounded-xl border border-[#E2E8F0] text-center text-sm font-medium text-[#1E293B] hover:border-[#2563EB] transition">
            {{ model }}
          </div>
        </div>
      </div>
    </section>

    <!-- Pricing -->
    <section id="pricing" class="py-20 px-6 bg-white">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-[#1E293B]">灵活定价</h2>
        <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="plan in plans" :key="plan.name" class="p-8 rounded-2xl border border-[#E2E8F0] hover:shadow-lg transition" :class="plan.highlight ? 'ring-2 ring-[#2563EB]' : ''">
            <h3 class="text-xl font-semibold text-[#1E293B]">{{ plan.name }}</h3>
            <div class="mt-4">
              <span class="text-4xl font-extrabold text-[#1E293B]">{{ plan.price }}</span>
              <span class="text-[#64748B]">/月</span>
            </div>
            <ul class="mt-6 space-y-3">
              <li v-for="feature in plan.features" :key="feature" class="text-sm text-[#64748B] flex items-center gap-2">
                <span class="text-[#2563EB]">✓</span> {{ feature }}
              </li>
            </ul>
            <a href="/login" class="mt-8 block text-center py-3 rounded-xl font-semibold transition" :class="plan.highlight ? 'bg-[#2563EB] text-white hover:bg-[#1D4ED8]' : 'border border-[#E2E8F0] text-[#1E293B] hover:border-[#2563EB]'">立即开始</a>
          </div>
        </div>
      </div>
    </section>

    <!-- API -->
    <section id="api" class="py-20 px-6">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-3xl font-bold text-center text-[#1E293B]">快速接入</h2>
        <p class="mt-4 text-center text-[#64748B]">兼容OpenAI SDK，只需替换base_url即可使用</p>
        <div class="mt-12 space-y-8">
          <div>
            <h3 class="text-lg font-semibold text-[#1E293B] mb-4">Python SDK</h3>
            <CodeBlock :html="pythonCode" :raw="pythonRaw" />
          </div>
          <div>
            <h3 class="text-lg font-semibold text-[#1E293B] mb-4">cURL</h3>
            <CodeBlock :html="curlCode" :raw="curlRaw" />
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="py-12 px-6 bg-[#1E293B]">
      <div class="max-w-6xl mx-auto text-center text-[#94A3B8] text-sm">
        <p>&copy; 2026 AIGate. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import CodeBlock from '../components/CodeBlock.vue'

const baseUrl = 'http://token.sunki.asia:1002/v1'

const pythonRaw = `from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",
    base_url="${baseUrl}"
)

response = client.chat.completions.create(
    model="DeepSeek-V3.2-Pro",
    messages=[
        {"role": "user", "content": "你好"}
    ]
)

print(response.choices[0].message.content)`

const curlRaw = `curl ${baseUrl}/chat/completions \\
  -H "Authorization: Bearer your-api-key" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "DeepSeek-V3.2-Pro",
    "messages": [{"role": "user", "content": "你好"}]
  }'`

const pythonCode = `<span class="keyword">from</span> openai <span class="keyword">import</span> OpenAI

client = OpenAI(
    api_key=<span class="string">"your-api-key"</span>,
    base_url=<span class="string">"${baseUrl}"</span>
)

response = client.chat.completions.<span class="func">create</span>(
    model=<span class="string">"DeepSeek-V3.2-Pro"</span>,
    messages=[
        {<span class="string">"role"</span>: <span class="string">"user"</span>, <span class="string">"content"</span>: <span class="string">"你好"</span>}
    ]
)

<span class="func">print</span>(response.choices[<span class="placeholder">0</span>].message.content)`

const curlCode = `<span class="keyword">curl</span> ${baseUrl}/chat/completions \\
  -H <span class="string">"Authorization: Bearer your-api-key"</span> \\
  -H <span class="string">"Content-Type: application/json"</span> \\
  -d <span class="string">'{
    "model": "DeepSeek-V3.2-Pro",
    "messages": [{"role": "user", "content": "你好"}]
  }'</span>`

const models = [
  'DeepSeek-V3.2-Pro', 'GLM-5-Pro', 'GPT-5', 'GPT-4o',
  'Claude 4 Sonnet', 'Gemini 2.5 Pro', 'Qwen3-Max', 'Llama 4',
  'Mistral Large', 'Yi-Lightning', 'Doubao-Pro', 'Moonshot-v1',
  'DeepSeek-R1', 'GPT-5-mini', 'Claude 4 Haiku', 'Gemini 2.5 Flash'
]

const plans = [
  {
    name: '体验版',
    price: '免费',
    features: ['基础模型访问', '每日限额调用', '社区支持', 'API密钥管理'],
    highlight: false
  },
  {
    name: '专业版',
    price: '¥99',
    features: ['全部模型访问', '无限调用次数', '优先技术支持', '高级权限管理', '用量分析看板'],
    highlight: true
  },
  {
    name: '企业版',
    price: '定制',
    features: ['私有化部署', 'SLA保障', '专属客户经理', '定制模型接入', '安全审计日志'],
    highlight: false
  }
]
</script>
