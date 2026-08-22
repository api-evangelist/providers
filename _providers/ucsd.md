---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ucsd Agentic Access
  operation_count: 7
  slug: ucsd-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 9
apis:
- description: The UC San Diego ITS developer guide provides the information needed to understand and navigate campus systems and build applications that conform to recommended architecture and guidelines. It is the
  name: UC San Diego ITS Developer Guide
  slug: developer-portal
- description: The UC San Diego API Portal documents campus Web APIs and REST guidelines. APIs are available to UCSD developers (staff, students, and faculty) who have a Single Sign-On account; at this time the APIs
  name: UC San Diego Web API Portal
  slug: web-api-portal
- description: The UC San Diego Library Digital Collections is a public search and discovery interface for over 100,000 digital objects (documents, photographs, audio, video, and datasets) managed in the locally dev
  name: UC San Diego Library Digital Collections
  slug: library-digital-collections
- description: Speech synthesis and transcription endpoints.
  name: University of California, San Diego audio API
  slug: ucsd-audio-api
- description: Chat completion endpoints.
  name: University of California, San Diego chat API
  slug: ucsd-chat-api
- description: Text completion endpoints.
  name: University of California, San Diego completions API
  slug: ucsd-completions-api
- description: Embedding generation endpoints.
  name: University of California, San Diego embeddings API
  slug: ucsd-embeddings-api
- description: Image generation endpoints.
  name: University of California, San Diego images API
  slug: ucsd-images-api
- description: Model discovery endpoints.
  name: University of California, San Diego models API
  slug: ucsd-models-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio API
  slug: open-ucsd-audio-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio chat API
  slug: open-ucsd-chat-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio completions API
  slug: open-ucsd-completions-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio embeddings API
  slug: open-ucsd-embeddings-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio images API
  slug: open-ucsd-images-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio models API
  slug: open-ucsd-models-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ucsd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucsd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucsd.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ucsd.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UCSD
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucsdlib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-san-diego/
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsd-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'University of California, San Diego (UCSD) is a public research university in La Jolla, California, ranked #36 in the QS World University Rankings 2025. Its developer and API footprint is operated primarily by Information Technology Services (ITS) through a developer guide and an SSO-gated Web API Portal, with most institutional APIs restricted to UCSD staff, students, and faculty who hold a Single Sign-On account. UCSD also runs TritonAI, an LLM gateway for campus users, and maintains active open-source GitHub organizations and a publicly browsable Library Digital Collections repository.'
examples:
- key_count: 2
  name: Ucsd Chat Completion Example
  slug: ucsd-chat-completion-example
- key_count: 2
  name: Ucsd Embeddings Example
  slug: ucsd-embeddings-example
finops:
- name: Ucsd Finops
  service_category: Education
  slug: ucsd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsd.png
json_schemas:
- name: TritonAI Chat Completion Request
  property_count: 7
  slug: ucsd-chat-completion-request
- name: TritonAI Embedding Request
  property_count: 3
  slug: ucsd-embedding-request
json_structures:
- name: Ucsd Chat Completion Structure
  property_count: 7
  slug: ucsd-chat-completion-structure
- name: Ucsd Embedding Structure
  property_count: 3
  slug: ucsd-embedding-structure
jsonld:
- class_count: 14
  name: Ucsd Context
  property_count: 3
  slug: ucsd-context
layout: provider
modified: '2026-06-03'
name: University of California, San Diego
nav: Providers
network: true
overview: 'University of California, San Diego publishes 6 APIs on the [APIs.io](https://apis.io/) network, including audio API, chat API, completions API, and 3 more. Tagged areas include Education, Higher Education, University, Research, and United States.


  The University of California, San Diego catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of California, San Diego''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: Ucsd Plans Pricing
  plan_count: 2
  slug: ucsd-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ucsd Rate Limits
  slug: ucsd-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of California, San Diego API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ucsd-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of California, San Diego API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: ucsd-rules
score:
  band: thin
  composite: 37.4
  delta: -5.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 62.8
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsd/refs/heads/main/screenshots/ucsd-2026-06-20T195946.png
security:
- kind: authentication
  name: Ucsd Authentication
  slug: ucsd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ucsd Domain Security
  slug: ucsd-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ucsd
tags:
- Education
- Higher Education
- University
- Research
- United States
- California
website: https://www.ucsd.edu/
---
