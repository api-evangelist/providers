---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.heraldapi.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.heraldai.com/ — a different registrable domain (heraldapi.com -> heraldai.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Herald Agentic Access
  operation_count: 18
  slug: herald-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Applications API from Herald — 2 operation(s) for applications.
  name: Herald Applications API
  slug: herald-applications-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Authentication API from Herald — 1 operation(s) for authentication.
  name: Herald Authentication API
  slug: herald-authentication-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Classifications API from Herald — 1 operation(s) for classifications.
  name: Herald Classifications API
  slug: herald-classifications-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Distributors API from Herald — 1 operation(s) for distributors.
  name: Herald Distributors API
  slug: herald-distributors-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Files API from Herald — 1 operation(s) for files.
  name: Herald Files API
  slug: herald-files-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Producers API from Herald — 1 operation(s) for producers.
  name: Herald Producers API
  slug: herald-producers-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Products API from Herald — 2 operation(s) for products.
  name: Herald Products API
  slug: herald-products-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Quotes API from Herald — 1 operation(s) for quotes.
  name: Herald Quotes API
  slug: herald-quotes-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Submissions API from Herald — 2 operation(s) for submissions.
  name: Herald Submissions API
  slug: herald-submissions-api
- baseURL: https://api.heraldapi.com
  baseurl_source: declared
  description: The Webhooks API from Herald — 2 operation(s) for webhooks.
  name: Herald Webhooks API
  slug: herald-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Herald Applications API
  slug: open-herald-applications-api
- collection_type: open
  name: Herald Applications Authentication API
  slug: open-herald-authentication-api
- collection_type: open
  name: Herald Applications Classifications API
  slug: open-herald-classifications-api
- collection_type: open
  name: Herald Applications Distributors API
  slug: open-herald-distributors-api
- collection_type: open
  name: Herald Applications Files API
  slug: open-herald-files-api
- collection_type: open
  name: Herald Applications Producers API
  slug: open-herald-producers-api
- collection_type: open
  name: Herald Applications Products API
  slug: open-herald-products-api
- collection_type: open
  name: Herald Applications Quotes API
  slug: open-herald-quotes-api
- collection_type: open
  name: Herald Applications Submissions API
  slug: open-herald-submissions-api
- collection_type: open
  name: Herald Applications Webhooks API
  slug: open-herald-webhooks-api
- collection_type: open
  name: Herald API
  slug: open-herald
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/herald-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/herald-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/herald-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/herald-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heraldapi
- group: company
  title: ''
  type: Website
  url: https://www.heraldapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.heraldapi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/herald-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/herald-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/herald-finops.yml
created: '2026-06-25'
description: Herald builds digital infrastructure for commercial insurance, providing a single unified REST API that lets software platforms quote and bind across many carriers and lines of business. Developers create applications, submit them to carriers, and receive normalized quotes, products, classifications, and files through one integration secured with OAuth2 client-credentials bearer tokens.
finops:
- name: Herald Finops
  service_category: Insurance
  slug: herald-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/herald.png
layout: provider
modified: '2026-06-25'
name: Herald
nav: Providers
network: true
overview: 'Herald publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Classifications API, and 7 more. Tagged areas include Insurance, Insurtech, Commercial Insurance, Quoting, and Carriers.


  Herald''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Herald Plans Pricing
  plan_count: 1
  slug: herald-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Herald Rate Limits
  slug: herald-rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.1
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 18.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/herald/refs/heads/main/screenshots/herald-2026-07-25T221009.png
security:
- kind: authentication
  name: Herald Authentication
  slug: herald-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Herald Domain Security
  slug: herald-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: herald
tags:
- Insurance
- Insurtech
- Commercial Insurance
- Quoting
- Carriers
website: https://www.heraldapi.com
---
