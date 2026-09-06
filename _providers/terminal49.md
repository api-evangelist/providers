---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
- acting_count: 11
  human_in_the_loop: 1
  name: Terminal49 Agentic Access
  operation_count: 28
  slug: terminal49-agentic-access
  summary_line: 28 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Containers API from Terminal49 — 4 operation(s) for containers.
  name: Terminal49 Containers API
  slug: terminal49-containers-api
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Shipments API from Terminal49 — 4 operation(s) for shipments.
  name: Terminal49 Shipments API
  slug: terminal49-shipments-api
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Shipping Lines API from Terminal49 — 2 operation(s) for shipping lines.
  name: Terminal49 Shipping Lines API
  slug: terminal49-shipping-lines-api
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Terminals API from Terminal49 — 1 operation(s) for terminals.
  name: Terminal49 Terminals API
  slug: terminal49-terminals-api
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Tracking Requests API from Terminal49 — 2 operation(s) for tracking requests.
  name: Terminal49 Tracking Requests API
  slug: terminal49-tracking-requests-api
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Transport Events API from Terminal49 — 3 operation(s) for transport events.
  name: Terminal49 Transport Events API
  slug: terminal49-transport-events-api
- baseURL: https://api.terminal49.com/v2
  baseurl_source: declared
  description: The Webhooks API from Terminal49 — 5 operation(s) for webhooks.
  name: Terminal49 Webhooks API
  slug: terminal49-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Terminal49 Containers API
  slug: open-terminal49-containers-api
- collection_type: open
  name: Terminal49 Containers Shipments API
  slug: open-terminal49-shipments-api
- collection_type: open
  name: Terminal49 Containers Shipping Lines API
  slug: open-terminal49-shipping-lines-api
- collection_type: open
  name: Terminal49 Containers Terminals API
  slug: open-terminal49-terminals-api
- collection_type: open
  name: Terminal49 Containers Tracking Requests API
  slug: open-terminal49-tracking-requests-api
- collection_type: open
  name: Terminal49 Containers Transport Events API
  slug: open-terminal49-transport-events-api
- collection_type: open
  name: Terminal49 Containers Webhooks API
  slug: open-terminal49-webhooks-api
- collection_type: open
  name: Terminal49 API
  slug: open-terminal49
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/terminal49-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/terminal49-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terminal49-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/terminal49-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Terminal49
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/terminal49
- group: company
  title: ''
  type: Website
  url: https://www.terminal49.com
- group: docs
  title: ''
  type: Documentation
  url: https://terminal49.com/docs/api-docs/api-reference/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/terminal49-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/terminal49-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/terminal49-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.terminal49.com/blog
created: '2026-06-21'
description: Terminal49 is an automated container and ocean-freight tracking platform. Its v2 REST API (JSON:API) lets shippers, forwarders, and logistics software track Bills of Lading, bookings, and container numbers across global ocean carriers and North American rail, returning normalized milestones, ETAs, terminal availability, holds, demurrage fees, and last free day, with webhooks for real-time updates.
finops:
- name: Terminal49 Finops
  service_category: Supply Chain and Logistics
  slug: terminal49-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/terminal49.png
layout: provider
modified: '2026-06-21'
name: Terminal49
nav: Providers
network: true
overview: 'Terminal49 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Containers API, Shipments API, Shipping Lines API, and 4 more. Tagged areas include Container Tracking, Ocean Freight, Supply Chain, Logistics, and Shipping.


  Terminal49''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Terminal49 Plans Pricing
  plan_count: 4
  slug: terminal49-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Terminal49 Rate Limits
  slug: terminal49-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 32.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/terminal49/refs/heads/main/screenshots/terminal49-2026-09-02T163138.png
security:
- kind: authentication
  name: Terminal49 Authentication
  slug: terminal49-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Terminal49 Domain Security
  slug: terminal49-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: terminal49
tags:
- Container Tracking
- Ocean Freight
- Supply Chain
- Logistics
- Shipping
website: https://www.terminal49.com
---
