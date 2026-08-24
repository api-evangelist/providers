---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The HTTP server started by `furiosa-llm serve <ARTIFACT_PATH>`. It hosts a single model on RNGD NPUs and exposes an OpenAI-compatible surface - /v1/completions, /v1/chat/completions, /v1/responses (Op
  name: Furiosa-LLM OpenAI-Compatible Server
  slug: furiosa-llm-openai-server
- description: The REST and gRPC inference surface of Furiosa Model Server, serving TFLite/ONNX models on FuriosaAI NPUs. Implements the KServe/KFServing V2 Dataplane - server liveness and readiness, server and mode
  name: Furiosa Model Server - Predict API (KServe v2)
  slug: furiosa-server-predict-v2
- description: 'The model-management surface of Furiosa Model Server, implementing the Triton Inference Server Model Repository extension - POST /v2/repository/index to list the repository and each model''s readiness '
  name: Furiosa Model Server - Model Repository API
  slug: furiosa-model-repository-v2
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://furiosa.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.furiosa.ai/latest/en/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.furiosa.ai/latest/en/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.furiosa.ai/latest/en/furiosa_llm/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.furiosa.ai/latest/en/get_started/furiosa_llm.html
- group: operate
  title: ''
  type: Support
  url: https://furiosa-ai.atlassian.net/servicedesk/customer/portals
- group: operate
  title: ''
  type: Community
  url: https://forums.furiosa.ai/
- group: company
  title: ''
  type: Blog
  url: https://furiosa.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/furiosa-ai
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.furiosa.ai/latest/en/overview/roadmap.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.furiosa.ai/latest/en/whatsnew/index.html
- group: start
  title: ''
  type: SignUp
  url: https://lp.furiosa.ai/furiosa-access-program
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://furiosa.ai/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://furiosa.ai/contact
- group: build
  title: ''
  type: Packages
  url: packages/furiosa-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/furiosa-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/furiosa-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/furiosa-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/furiosa-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/furiosa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/furiosa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/furiosa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/furiosa-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/furiosa-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/furiosa-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/furiosa-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/furiosa-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/furiosa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/furiosa-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/furiosa-changelog.yml
created: '2026-08-16'
description: 'FuriosaAI is a South Korean semiconductor company that designs data-center AI inference chips and the software stack that runs on them. Its second-generation NPU, RNGD, implements a Tensor Contraction Processor architecture on TSMC 5nm and targets LLM, multi-modal and vision inference. The developer surface is software you run yourself rather than a hosted API: Furiosa-LLM ships an OpenAI-compatible server exposing chat, completions, responses, embeddings, score, rerank, models, tokenizer and Prometheus metrics endpoints, and the earlier Furiosa Model Server implements the KServe v2 Predict Protocol and the Triton Model Repository extension over REST and gRPC. Around that sit Python, Go and Rust packages, a furiosa-smi device CLI, container images, an APT/RPM package repository, and a Kubernetes cloud-native toolkit (device plugin, DRA driver, feature discovery, metrics exporter, NPU operator).'
image: https://furiosa.ai/favicon.ico
layout: provider
modified: '2026-08-16'
name: FuriosaAI
nav: Providers
network: true
overview: 'FuriosaAI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Furiosa Model Server - Predict API (KServe v2) and Furiosa Model Server - Model Repository API. Tagged areas include Artificial Intelligence, Machine-Learning, Inference, Semiconductors, and NPU.


  FuriosaAI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, signup flow, and 24 more developer resources.'
plans:
- name: Furiosa Plans Pricing
  plan_count: 0
  slug: furiosa-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Furiosa Rate Limits
  slug: furiosa-rate-limits
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 30.3
    contract_quality: 35.3
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 31.6
  previous_composite: 45.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/furiosa/refs/heads/main/screenshots/furiosa-2026-08-17T080944.png
security:
- kind: authentication
  name: Furiosa Authentication
  slug: furiosa-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Furiosa Domain Security
  slug: furiosa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: furiosa
tags:
- Artificial Intelligence
- Machine-Learning
- Inference
- Semiconductors
- NPU
- Hardware
- LLM
- Model Serving
- Kubernetes
- Developer Tools
- Compute
- Infrastructure
website: https://furiosa.ai/
---
