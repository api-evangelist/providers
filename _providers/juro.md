---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Juro Agentic Access
  operation_count: 16
  slug: juro-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 5
apis:
- description: Create, read, update, delete, and upload contracts.
  name: Juro Contracts API
  slug: juro-contracts-api
- description: API status and key validity.
  name: Juro Health API
  slug: juro-health-api
- description: Send contracts for e-signature and apply signatures.
  name: Juro Signatures API
  slug: juro-signatures-api
- description: List and retrieve contract templates.
  name: Juro Templates API
  slug: juro-templates-api
- description: Subscribe to contract lifecycle events (modeled).
  name: Juro Webhooks API
  slug: juro-webhooks-api
artifact_total: 11
collections:
- collection_type: open
  name: Juro API
  slug: open-juro
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/juro-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/juro-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juro
- group: company
  title: ''
  type: Website
  url: https://juro.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.juro.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/juro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/juro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/juro-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://juro.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://juro.com/terms/api-terms
- group: company
  title: ''
  type: Blog
  url: https://juro.com/learn
created: '2026-07-11'
description: Juro is an AI-native contract automation and contract lifecycle management (CLM) platform where legal, sales, HR, and finance teams create, negotiate, sign, and manage contracts in one browser-based workspace. Juro exposes a documented public REST API (v3, base https://api.juro.com/v3, with a sandbox at https://api-sandbox.juro.io/v3) authenticated with an x-api-key header. The API lets external systems initiate contracts from templates, upload PDFs, edit smart fields, send contracts for e-signature, download signed PDFs, and subscribe to a dozen-plus contract lifecycle webhook events (contract.created, contract.signed, approval events, and more). API access is plan-gated - it is included with a Juro subscription and enabled through your Customer Success Manager - so live calls require an eligible plan and issued key.
finops:
- name: Juro Finops
  service_category: Contract Lifecycle Management
  slug: juro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/juro.png
layout: provider
modified: '2026-07-11'
name: Juro
nav: Providers
network: true
overview: 'Juro publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contracts API, Health API, Signatures API, and 2 more. Tagged areas include Contract Management, CLM, Contract Lifecycle, Contract Automation, and Legal.


  Juro''s developer surface includes authentication, documentation, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Juro Plans Pricing
  plan_count: 3
  slug: juro-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Juro Rate Limits
  slug: juro-rate-limits
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/juro/refs/heads/main/screenshots/juro-2026-07-25T223336.png
security:
- kind: authentication
  name: Juro Authentication
  slug: juro-authentication
  summary_line: apiKey · 1 scheme
slug: juro
tags:
- Contract Management
- CLM
- Contract Lifecycle
- Contract Automation
- Legal
- LegalTech
- E-Signature
- Contracts
website: https://juro.com
---
