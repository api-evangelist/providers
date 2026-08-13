---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: 'LLMBoost is MangoBoost''s enterprise LLM inference server. It serves the OpenAI REST API on /v1 so an existing OpenAI client migrates with a base-URL change: POST /v1/chat/completions, POST /v1/complet'
  name: Mango LLMBoost Inference Server API
  slug: llmboost-inference
- description: The Mango SDK development package (libmango-dev) provides the C/C++ user API, libraries and example applications for programming MangoBoost DPU devices. Documented API groups are Common, Device Contex
  name: Mango SDK Device API (libmango)
  slug: mango-sdk
- description: MangoBoost ships an Open Programmable Infrastructure (OPI) gRPC bridge that translates standard OPI storage API calls into MangoBoost SDK / SPDK RPC calls on the DPU, so NVMe-oF initiator (NTI) and ta
  name: Mango OPI Storage Bridge gRPC API
  slug: opi-storage-bridge
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/opiproject/opi-mangoboost-bridge/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/opiproject/opi-mangoboost-bridge/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/opiproject/opi-mangoboost-bridge/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mangoboost-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/mangoboost-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mangoboost-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mangoboost-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mangoboost-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mangoboost-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mangoboost-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mangoboost-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mangoboost-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mangoboost-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.mangoboost.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sdk.mangoboost.io/
- group: docs
  title: ''
  type: Documentation
  url: https://llmboost.mangoboost.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sdk.mangoboost.io/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://llmboost.mangoboost.io/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.mangoboost.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.mangoboost.io/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MangoBoost
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mangoboost.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mangoboost.io/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://www.mangoboost.io/careers
- group: company
  title: ''
  type: News
  url: https://www.mangoboost.io/media/news
- group: other
  title: ''
  type: Publications
  url: https://www.mangoboost.io/resources/publications
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mangoboost/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/mangoboost_inc
created: '2026-08-04'
description: 'MangoBoost, Inc. builds full-stack Data Processing Unit (DPU) hardware and AI-infrastructure software for data centers. Founded in 2022 and headquartered in Seattle with operations in Canada and Korea, the company ships the Mango BoostX DPU family (RoCE AI / RDMA, NVMe-oF initiator and target, TCP Offload Engine), the Mango SDK — a C/C++ device library (libmango), CLI tools (mango-ctl, mango-smi) and an OPI-compliant gRPC storage bridge — and Mango LLMBoost, an enterprise LLM inference server that exposes a drop-in OpenAI-compatible REST API on customer-owned AMD Instinct GPUs. Its developer surface is self-hosted rather than SaaS: the LLMBoost server is distributed as a container plus the llmboost_hub (lbh) Python CLI, and the DPU is programmed through libmango and OPI gRPC on the card.'
image: https://cdn.sanity.io/images/hx87iaks/production/044e3e87d4c32dc3c01996e772f4b3f7c08b873e-376x61.png
layout: provider
modified: '2026-08-04'
name: MangoBoost
nav: Providers
network: true
overview: 'MangoBoost publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Infrastructure, and Data Center.


  MangoBoost''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 28.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 72.2
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 28.7
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mangoboost/refs/heads/main/screenshots/mangoboost-2026-08-07T171949.png
security:
- kind: authentication
  name: Mangoboost Authentication
  slug: mangoboost-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mangoboost Domain Security
  slug: mangoboost-domain-security
  summary_line: TLSv1.3
slug: mangoboost
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Infrastructure
- Data Center
- Semiconductors
- Hardware
- Storage
- Networking
- Inference
- GPU
- DPU
website: https://www.mangoboost.io/
---
