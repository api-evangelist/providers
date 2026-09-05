---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Juro Agentic Access
  operation_count: 16
  slug: juro-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.juro.com/v3
  baseurl_source: declared
  description: Create, read, update, delete, and upload contracts.
  name: Juro Contracts API
  slug: juro-contracts-api
- baseURL: https://api.juro.com/v3
  baseurl_source: declared
  description: API status and key validity.
  name: Juro Health API
  slug: juro-health-api
- baseURL: https://api.juro.com/v3
  baseurl_source: declared
  description: Send contracts for e-signature and apply signatures.
  name: Juro Signatures API
  slug: juro-signatures-api
- baseURL: https://api.juro.com/v3
  baseurl_source: declared
  description: List and retrieve contract templates.
  name: Juro Templates API
  slug: juro-templates-api
- baseURL: https://api.juro.com/v3
  baseurl_source: declared
  description: Subscribe to contract lifecycle events (modeled).
  name: Juro Webhooks API
  slug: juro-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Juro Contracts API
  slug: open-juro-contracts-api
- collection_type: open
  name: Juro Contracts Health API
  slug: open-juro-health-api
- collection_type: open
  name: Juro Contracts Signatures API
  slug: open-juro-signatures-api
- collection_type: open
  name: Juro Contracts Templates API
  slug: open-juro-templates-api
- collection_type: open
  name: Juro Contracts Webhooks API
  slug: open-juro-webhooks-api
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
random_paper: 7
rate_limits:
- limit_count: 5
  name: Juro Rate Limits
  slug: juro-rate-limits
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 59.2
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Legal Tech
- E-Signature
- Contracts
website: https://juro.com
---
