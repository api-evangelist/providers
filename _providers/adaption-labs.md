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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Adaption Labs Agentic Access
  operation_count: 11
  slug: adaption-labs-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 2
apis:
- description: Create, ingest, adapt, evaluate, and export datasets.
  name: Adaption Labs Datasets API
  slug: adaption-labs-datasets-api
- description: Presigned file-upload lifecycle for local-file ingestion.
  name: Adaption Labs Upload API
  slug: adaption-labs-upload-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adaption Adaptive Data Datasets API
  slug: open-adaption-labs-datasets-api
- collection_type: open
  name: Adaption Adaptive Data Datasets Upload API
  slug: open-adaption-labs-upload-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/adaption-labs-datasets-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.adaptionlabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adaptionlabs.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adaptionlabs.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adaptionlabs.ai/introduction/getting-started/index.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/adaption-labs-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adaption-labs-agentic-access.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/adaption-labs-datasets-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adaption-labs-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adaption-labs-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adaption-labs-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adaption-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaption-labs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://adaptionlabs.ai/enterprise
- group: build
  title: ''
  type: Packages
  url: packages/adaption-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adaption-labs-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adaption-labs-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adaption-labs-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaption-labs-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://adaptionlabs.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/sHhG8kwVav
- group: start
  title: ''
  type: SignUp
  url: https://adaptionlabs.ai/app/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adaptionlabs.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptionlabs.ai/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaption-labs-domain-security.yml
created: '2026-07-17'
description: Adaption Labs is a San Francisco AI research company, founded in 2025 by Sara Hooker and Sudip Roy (both formerly of Cohere), building adaptive AI systems that continuously learn from real-world interaction instead of scaling through ever-larger pretraining runs. Its Adaptive Data platform and the REST Adaption API let teams ingest, adapt, evaluate, and export model-ready training data, while AutoScientist automates the research loop behind model training and alignment. The Adaption API is available through a web app and an official Python SDK (pip install adaption). Backed by a $50M seed round led by Emergence Capital, with Threshold Ventures, Mozilla Ventures, Fifty Years, and others.
image: https://adaptionlabs.ai/opengraph-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: adaption-labs-mcp.yml
  slug: adaption-labs-mcpyml
modified: '2026-07-17'
name: Adaption Labs
nav: Providers
network: true
overview: 'Adaption Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Datasets API and Upload API. Tagged areas include Company, AI, Machine Learning, Training Data, and Datasets.


  Adaption Labs'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 19 more developer resources.'
random_paper: 119
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 14.6
    developer_ergonomics: 53.8
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adaption-labs/refs/heads/main/screenshots/adaption-labs-2026-07-25T181552.png
security:
- kind: authentication
  name: Adaption Labs Authentication
  slug: adaption-labs-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adaption Labs Domain Security
  slug: adaption-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adaption-labs
tags:
- Company
- AI
- Machine Learning
- Training Data
- Datasets
- LLM
- Adaptive Data
- SDK
website: https://www.adaptionlabs.ai/
---
