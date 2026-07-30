---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 99
  human_in_the_loop: 0
  name: Dp Agentic Access
  operation_count: 166
  slug: dp-agentic-access
  summary_line: 166 operations · 99 acting
api_count: 15
apis:
- description: 基于深度推理的科学问答（sigma-search，SSE 编排）。收费：创建会话 2 元/次。注意内部版本混用（sessions v4 / SSE v3 / history v4）。
  name: DP Technology (Bohrium) AI 科学小导师 (bohrium-mentor) API
  slug: dp-ai-bohrium-mentor-api
- description: 数据集管理 — 创建、上传、下载、版本控制。免费。
  name: DP Technology (Bohrium) 数据集 (bohrium-dataset) API
  slug: dp-bohrium-dataset-api
- description: personal/share 盘文件管理 — 列出、上传、下载、移动、复制、删除。v1 用于 personal/share，v2 file 仅用于 appJob。免费。
  name: DP Technology (Bohrium) 文件盘 (bohrium-file) API
  slug: dp-bohrium-file-api
- description: 容器镜像管理 — 查询、拉取、创建、删除镜像。免费。镜像地址位于 registry.dp.tech / registry.bohrium.dp.tech。
  name: DP Technology (Bohrium) 容器镜像 (bohrium-image) API
  slug: dp-bohrium-image-api
- description: 计算任务管理 — 提交、查询、终止、删除任务（提交主要经 bohr CLI）。任务运行按机时收费，价格见 Job 定价页。
  name: DP Technology (Bohrium) 计算任务 (bohrium-job) API
  slug: dp-bohrium-job-api
- description: 知识库管理 — 知识库/文件夹/文献/标签/笔记/召回/权限。网关转发至 literature-sage。免费（仅容量配额）。
  name: DP Technology (Bohrium) 知识库 (bohrium-knowledge-base) API
  slug: dp-bohrium-knowledge-base-api
- description: LKM — 知识节点检索、推理链检索、论文知识图谱、追溯 claim 依据、批量节点水合、提交反馈。收费（定价中，待补充）。
  name: DP Technology (Bohrium) 大知识模型 (bohrium-lkm) API
  slug: dp-bohrium-lkm-api
- description: 开发节点管理 — 创建、启停、删除容器/虚拟机。运行按机时收费，价格见 Node 定价页。
  name: DP Technology (Bohrium) 开发节点 (bohrium-node) API
  slug: dp-bohrium-node-api
- description: RAG 引擎关键词+语义检索。收费。响应可能为多行 JSON（流式，解析第一行）。
  name: DP Technology (Bohrium) 论文与专利搜索 (bohrium-paper-search) API
  slug: dp-bohrium-paper-search-api
- description: 项目管理 — 创建项目、管理成员、设置额度。免费（管理成本额度，非按调用计费）。
  name: DP Technology (Bohrium) 项目管理 (bohrium-project) API
  slug: dp-bohrium-project-api
- description: 学者搜索与画像 — 按姓名/机构检索，查看发文/引用/h-index/研究方向。免费。
  name: DP Technology (Bohrium) 学者搜索 (bohrium-scholar-search) API
  slug: dp-bohrium-scholar-search-api
- description: 科学百科 — 搜词条/关键词、浏览领域课程、看章节知识点、查主题知识图谱。免费（限时）。阅读链接指向 www.bohrium.com。
  name: DP Technology (Bohrium) 科学百科 (bohrium-sciencepedia) API
  slug: dp-bohrium-sciencepedia-api
- description: 科学工具库 — 按领域/子领域浏览、混合检索工具、查看详情与分类。免费。语言经 Content-Language 头或 body language 指定。
  name: DP Technology (Bohrium) 科学工具库 (bohrium-tools) API
  slug: dp-bohrium-tools-api
- description: 网页搜索 — 代理 searchapi.io 做开放互联网检索。免费。
  name: DP Technology (Bohrium) 网页搜索 (bohrium-web-search) API
  slug: dp-bohrium-web-search-api
- description: Uni-Parser — 提取文本、表格、图表、公式。收费：0.05 元/页（触发时扣）。figure 模块无权限时可能 403。
  name: DP Technology (Bohrium) PDF 解析 (bohrium-pdf-parser) API
  slug: dp-pdf-bohrium-pdf-parser-api
artifact_total: 19
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/dp-bohrium-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/dp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dp-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dp-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dp-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/dp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dp-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/dp-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dp-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dp-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/dp-bohrium-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dp-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dp-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bohrium.dp.tech/developer
- group: docs
  title: ''
  type: Documentation
  url: https://bohrium-doc.dp.tech/en/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bohrium-doc.dp.tech/en/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dptech-corp
- group: start
  title: ''
  type: SignUp
  url: https://www.bohrium.com/
- group: operate
  title: ''
  type: Support
  url: https://www.dp.tech/contact
- group: company
  title: ''
  type: Website
  url: https://dp.tech
created: '2026-07-17'
description: DP Technology (Deep Potential Technology, 深势科技) is a global pioneer of the "AI for Science" research paradigm, founded in 2018 with offices in Beijing, Shanghai, Shenzhen, and Yibin. Its Bohrium platform is a research cloud for microscale scientific computing and industrial design — compute jobs, development nodes, datasets, container images, projects, knowledge bases, large knowledge models, paper/patent/scholar search, PDF parsing, a scientific-tools library, and web search — all reachable through the Bohrium OpenAPI (Bearer AccessKey auth, base URL https://open.bohrium.com). DP Technology also founds and maintains the open-source DeepModeling molecular-simulation toolchain (DeePMD-kit, DP-GEN, dpdispatcher, dpdata) and ships a first-party Python SDK, agent SDK, CLI, and 17 official Agent Skills.
image: https://dp.tech/dp-favicon.png
layout: provider
mcp_servers:
- description: ''
  name: dp-mcp.yml
  slug: dp-mcpyml
modified: '2026-07-18'
name: DP Technology (Bohrium)
nav: Providers
network: true
overview: 'DP Technology (Bohrium) publishes 15 APIs on the [APIs.io](https://apis.io/) network, including AI 科学小导师 (bohrium-mentor) API, 数据集 (bohrium-dataset) API, 文件盘 (bohrium-file) API, and 12 more. Tagged areas include Company, AI for Science, Scientific Computing, Molecular Simulation, and Drug Discovery.


  DP Technology (Bohrium)''s developer surface includes authentication, CLI, documentation, API reference, signup flow, support, and 17 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 37.4
  delta: -0.1
  facets:
    commercial_clarity: 13.2
    contract_quality: 45.0
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dp/refs/heads/main/screenshots/dp-2026-07-25T212347.png
security:
- kind: authentication
  name: Dp Authentication
  slug: dp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dp Domain Security
  slug: dp-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: dp
tags:
- Company
- AI for Science
- Scientific Computing
- Molecular Simulation
- Drug Discovery
- Materials Science
- Research Cloud
- Machine Learning
- HPC
website: https://dp.tech
---
