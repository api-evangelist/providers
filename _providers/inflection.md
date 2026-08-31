---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Inflection Agentic Access
  operation_count: 8
  slug: inflection-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 1
apis:
- description: The Chat API from Inflection AI — 2 operation(s) for chat.
  name: Inflection AI Chat API
  slug: inflection-chat-api
- description: The Discovery API from Inflection AI — 1 operation(s) for discovery.
  name: Inflection AI Discovery API
  slug: inflection-discovery-api
- description: The Embeddings API from Inflection AI — 1 operation(s) for embeddings.
  name: Inflection AI Embeddings API
  slug: inflection-embeddings-api
- description: The External API from Inflection AI — 3 operation(s) for external.
  name: Inflection AI External API
  slug: inflection-external-api
- description: The Status API from Inflection AI — 1 operation(s) for status.
  name: Inflection AI Status API
  slug: inflection-status-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inflection Inference Chat API
  slug: open-inflection-chat-api
- collection_type: open
  name: Inflection Inference Chat Discovery API
  slug: open-inflection-discovery-api
- collection_type: open
  name: Inflection Inference Chat Embeddings API
  slug: open-inflection-embeddings-api
- collection_type: open
  name: Inflection Inference Chat External API
  slug: open-inflection-external-api
- collection_type: open
  name: Inflection Inference Chat Status API
  slug: open-inflection-status-api
- collection_type: open
  name: Inflection Inference API
  slug: open-inflection
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inflection-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inflection-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inflection-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/inflection-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InflectionAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inflectionai
- group: company
  title: ''
  type: Website
  url: https://inflection.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.inflection.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/inflection-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inflection-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inflection-finops.yml
created: '2026-05-08'
description: Inflection AI is a foundation-model company behind the Pi personal AI assistant and the Inflection 3.0 family of empathetic large language models (Pi, Productivity). The Inflection Developer API serves these proprietary models for enterprise integration with cloud and on-premise deployment options.
finops:
- name: Inflection Finops
  service_category: AI and Machine Learning
  slug: inflection-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inflection.png
layout: provider
modified: '2026-05-19'
name: Inflection AI
nav: Providers
network: true
overview: 'Inflection AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Discovery API, Embeddings API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Personal AI, Pi, and Foundation Models.


  Inflection AI''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Inflection Plans Pricing
  plan_count: 3
  slug: inflection-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Inflection Rate Limits
  slug: inflection-rate-limits
scopes:
- name: Inflection Scopes
  scope_count: 0
  slug: inflection-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 50.1
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inflection/refs/heads/main/screenshots/inflection-2026-06-20T183333.png
security:
- kind: authentication
  name: Inflection Authentication
  slug: inflection-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Inflection Domain Security
  slug: inflection-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inflection
tags:
- Artificial Intelligence
- LLM
- Personal AI
- Pi
- Foundation Models
- Empathetic AI
website: https://inflection.ai/
---
