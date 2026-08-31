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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Create, list, run, evaluate, download, and publish adaptive datasets.
  name: Adaption Datasets API
  slug: adaption-datasets-api
- description: Pre-signed direct-to-S3 upload lifecycle for file-sourced datasets.
  name: Adaption Upload API
  slug: adaption-upload-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adaption Adaptive Data Datasets API
  slug: open-adaption-datasets-api
- collection_type: open
  name: Adaption Adaptive Data Datasets Upload API
  slug: open-adaption-upload-api
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
created: '2026-07-17'
description: Adaption (Adaption Labs) is a San Francisco AI research company building adaptive, continuously-learning AI systems rather than relying on ever-larger static models. Founded in 2026 by former Cohere leaders Sara Hooker and Sudip Roy, it exited stealth with a $50M seed round led by Emergence Capital. Its first product, Adaptive Data, exposes a REST API and official Python SDK to ingest, adapt, evaluate, and export model-ready training datasets — folding data-optimization techniques usually reserved for frontier labs into a self-serve workflow for everyday teams.
image: https://adaptionlabs.ai/opengraph-image.jpg?opengraph-image.28ce77cd.jpg
layout: provider
modified: '2026-07-17'
name: Adaption
nav: Providers
network: true
overview: 'Adaption publishes 2 APIs on the [APIs.io](https://apis.io/) network: Datasets API and Upload API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Training Data, and Datasets.


  Adaption''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, and 5 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 54.1
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 36.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Artificial Intelligence
- Machine-Learning
- Training Data
- Datasets
- Data Augmentation
- LLM
- Model Training
- Developer Tools
website: https://docs.adaptionlabs.ai/
---
