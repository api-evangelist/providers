---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
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
    error_semantics: verified
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
  score: 23.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Taalas Agentic Access
  operation_count: 6
  slug: taalas-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 3
apis:
- baseURL: https://api.taalas.com
  baseurl_source: declared
  description: 'Taalas-native REST interface for running inference against the HC1 hardcore-model silicon. Three operations: a public /health probe reporting server status, queue depth and the currently loaded LoRA a'
  name: Taalas API
  slug: taalas-api
- baseURL: https://api.taalas.com
  baseurl_source: declared
  description: The Models API from Taalas — 1 operation(s) for models.
  name: Taalas Models API
  slug: taalas-models-api
- baseURL: https://api.taalas.com
  baseurl_source: declared
  description: The Monitoring API from Taalas — 1 operation(s) for monitoring.
  name: Taalas Monitoring API
  slug: taalas-monitoring-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Taalas API
  slug: open-taalas-inference-api
- collection_type: open
  name: Taalas API — v1
  slug: open-taalas-inference-v1-api
- collection_type: open
  name: Taalas Models API
  slug: open-taalas-models-api
- collection_type: open
  name: Taalas Monitoring API
  slug: open-taalas-monitoring-api
common:
- group: company
  title: ''
  type: Website
  url: https://taalas.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.taalas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.taalas.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.taalas.com/v1/docs
- group: start
  title: ''
  type: SignUp
  url: https://taalas.com/api-request-form/
- group: operate
  title: ''
  type: Support
  url: https://api.taalas.com/bug-report
- group: company
  title: ''
  type: Blog
  url: https://taalas.com/mission-log/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.taalas.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taalas.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taalas.com/privacy-policy/
- group: other
  title: ''
  type: Products
  url: https://taalas.com/products/
- group: company
  title: ''
  type: Careers
  url: https://taalas.com/position/
- group: start
  title: ''
  type: Demo
  url: https://chatjimmy.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/taalas-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taalas-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/taalas-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/taalas-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taalas-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taalas-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/taalas-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/taalas-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taalas-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/taalas-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taalas-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taalas-agentic-access.yml
created: '2026-08-02'
description: 'Taalas is a Toronto-based semiconductor company building "Hardcore Models" — AI models etched directly into custom silicon rather than executed as software on general-purpose GPUs, under the tagline "The Model is The Computer." Its first product, the HC1 technology demonstrator, hard-wires Meta''s Llama 3.1 8B into an 815mm2 / 53-billion-transistor die on TSMC''s 6nm process and is publicly demonstrated through the ChatJimmy chatbot. Taalas exposes that silicon to developers through a hosted inference REST API at api.taalas.com, which publishes two OpenAPI 3.1.0 contracts: a root API with health, model-info and a Taalas-native /generate operation, and an OpenAI-compatible /v1 surface with /v1/completions and /v1/chat/completions. Access is by bearer API key issued through an application form; applications are currently closed due to demand.'
image: https://taalas.com/h-content/uploads/2024/01/cropped-favicon-192x192.png
layout: provider
modified: '2026-08-02'
name: Taalas
nav: Providers
network: true
overview: 'Taalas publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Models API, Monitoring API, and 1 more. Tagged areas include Company, Artificial Intelligence, AI Inference, Semiconductors, and AI Accelerator.


  Taalas'' developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 48.5
    developer_ergonomics: 31.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taalas/refs/heads/main/screenshots/taalas-2026-09-02T161654.png
security:
- kind: authentication
  name: Taalas Authentication
  slug: taalas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Taalas Domain Security
  slug: taalas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taalas
tags:
- Company
- Artificial Intelligence
- AI Inference
- Semiconductors
- AI Accelerator
- Large Language Models
- Llama
- Inference API
- OpenAI-Compatible
- Hardware
- Deep Tech
website: https://taalas.com/
---
