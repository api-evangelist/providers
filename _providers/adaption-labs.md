---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Adaption Labs Agentic Access
  operation_count: 11
  slug: adaption-labs-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.prod.adaptionlabs.ai
  baseurl_source: declared
  description: Create, ingest, adapt, evaluate, and export datasets.
  name: Adaption Labs Datasets API
  slug: adaption-labs-datasets-api
- baseURL: https://api.prod.adaptionlabs.ai
  baseurl_source: declared
  description: Presigned file-upload lifecycle for local-file ingestion.
  name: Adaption Labs Upload API
  slug: adaption-labs-upload-api
artifact_total: 8
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
  type: X-MCPServerCandidate
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
modified: '2026-07-17'
name: Adaption Labs
nav: Providers
network: true
overview: 'Adaption Labs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Datasets API and Upload API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Training Data, and Datasets.


  Adaption Labs'' developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 19 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 13.5
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 34.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
- Machine-Learning
- Training Data
- Datasets
- LLM
- Adaptive Data
- SDK
website: https://www.adaptionlabs.ai/
---
