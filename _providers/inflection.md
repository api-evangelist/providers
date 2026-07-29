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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Inflection Agentic Access
  operation_count: 8
  slug: inflection-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 5
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
artifact_total: 13
collections:
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
overview: 'Inflection AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Discovery API, Embeddings API, and 2 more. Tagged areas include AI, LLM, Personal AI, Pi, and Foundation Models.


  Inflection AI''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Inflection Plans Pricing
  plan_count: 3
  slug: inflection-plans-pricing
random_paper: 66
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
  composite: 36.3
  delta: -3.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- AI
- LLM
- Personal AI
- Pi
- Foundation Models
- Empathetic AI
website: https://inflection.ai/
---
