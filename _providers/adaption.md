---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Create, list, run, evaluate, download, and publish adaptive datasets.
  name: Adaption Datasets API
  slug: adaption-datasets-api
- description: Pre-signed direct-to-S3 upload lifecycle for file-sourced datasets.
  name: Adaption Upload API
  slug: adaption-upload-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaption-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.adaptionlabs.ai/
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
  url: https://docs.adaptionlabs.ai/introduction/getting-started
- group: company
  title: ''
  type: Blog
  url: https://adaptionlabs.ai/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.adaptionlabs.ai/app/auth
- group: start
  title: ''
  type: Login
  url: https://www.adaptionlabs.ai/app/auth
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/sHhG8kwVav
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adaptionlabs.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adaptionlabs.ai/privacy-policy
- group: build
  title: ''
  type: SDKs
  url: packages/adaption-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/adaption-packages.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/adaption-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adaption-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adaption-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adaption-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adaption-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adaption-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adaption-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adaption-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adaption-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adaption-well-known.yml
created: '2026-07-17'
description: Adaption (Adaption Labs) is a San Francisco AI research company building adaptive, continuously-learning AI systems rather than relying on ever-larger static models. Founded in 2026 by former Cohere leaders Sara Hooker and Sudip Roy, it exited stealth with a $50M seed round led by Emergence Capital. Its first product, Adaptive Data, exposes a REST API and official Python SDK to ingest, adapt, evaluate, and export model-ready training datasets — folding data-optimization techniques usually reserved for frontier labs into a self-serve workflow for everyday teams.
image: https://adaptionlabs.ai/opengraph-image.jpg?opengraph-image.28ce77cd.jpg
layout: provider
mcp_servers:
- description: ''
  name: adaption-mcp.yml
  slug: adaption-mcpyml
modified: '2026-07-17'
name: Adaption
nav: Providers
network: true
overview: 'Adaption publishes 2 APIs on the [APIs.io](https://apis.io/) network: Datasets API and Upload API. Tagged areas include Company, Ai, Artificial Intelligence, Machine Learning, and Training Data.


  Adaption''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 44.5
  delta: -0.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.8
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 44.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adaption/refs/heads/main/screenshots/adaption-2026-07-25T181551.png
security:
- kind: domain-security
  name: Adaption Domain Security
  slug: adaption-domain-security
  summary_line: TLSv1.2 · DMARC
slug: adaption
tags:
- Company
- Ai
- Artificial Intelligence
- Machine Learning
- Training Data
- Datasets
- Data Augmentation
- LLM
- Model Training
- Developer Tools
website: https://docs.adaptionlabs.ai/
---
