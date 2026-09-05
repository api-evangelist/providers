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
- acting_count: 5
  human_in_the_loop: 0
  name: Maya Mobile Agentic Access
  operation_count: 9
  slug: maya-mobile-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.maya.net/connectivity/v1
  baseurl_source: declared
  description: eSIM provisioning, activation codes/QR, suspend and reactivate.
  name: Maya Mobile eSIMs API
  slug: maya-mobile-esims-api
- baseURL: https://api.maya.net/connectivity/v1
  baseurl_source: declared
  description: Placing and assigning data-package orders, including top-ups.
  name: Maya Mobile Orders API
  slug: maya-mobile-orders-api
- baseURL: https://api.maya.net/connectivity/v1
  baseurl_source: declared
  description: Pre-made data plans and the catalog of countries, regions, and networks.
  name: Maya Mobile Plans API
  slug: maya-mobile-plans-api
- baseURL: https://api.maya.net/connectivity/v1
  baseurl_source: declared
  description: Real-time eSIM status and data-usage reporting.
  name: Maya Mobile Usage API
  slug: maya-mobile-usage-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Maya Mobile Connect+ Connectivity eSIMs API
  slug: open-maya-mobile-esims-api
- collection_type: open
  name: Maya Mobile Connect+ Connectivity eSIMs Orders API
  slug: open-maya-mobile-orders-api
- collection_type: open
  name: Maya Mobile Connect+ Connectivity eSIMs Plans API
  slug: open-maya-mobile-plans-api
- collection_type: open
  name: Maya Mobile Connect+ Connectivity eSIMs Usage API
  slug: open-maya-mobile-usage-api
- collection_type: open
  name: Maya Mobile Connect+ Connectivity API
  slug: open-maya-mobile
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/maya-mobile-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/maya-mobile-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maya-mobile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maya-mobile-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mayamobile-us
- group: company
  title: ''
  type: Website
  url: https://maya.net/
- group: docs
  title: ''
  type: Documentation
  url: https://maya.net/business/esim-api
- group: commercial
  title: ''
  type: Plans
  url: plans/maya-mobile-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maya-mobile-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maya-mobile-finops.yml
created: '2026-06-21'
description: Maya Mobile (Mobile Maya Inc) is a US-based global eSIM and connectivity platform aggregating 400+ roaming networks across 200+ destinations. Its Connect+ Connectivity REST API lets resellers and developers provision eSIMs, assign data packages, monitor activation status and data usage, suspend or reactivate lines, process top-ups, and receive lifecycle events via webhooks.
finops:
- name: Maya Mobile Finops
  service_category: Networking and Connectivity
  slug: maya-mobile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maya-mobile.png
layout: provider
modified: '2026-06-21'
name: Maya Mobile
nav: Providers
network: true
overview: 'Maya Mobile publishes 4 APIs on the [APIs.io](https://apis.io/) network, including eSIMs API, Orders API, Plans API, and 1 more. Tagged areas include eSIM, Connectivity, Mobile Data, Roaming, and Telecom.


  Maya Mobile''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Maya Mobile Plans Pricing
  plan_count: 2
  slug: maya-mobile-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Maya Mobile Rate Limits
  slug: maya-mobile-rate-limits
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 13.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maya-mobile/refs/heads/main/screenshots/maya-mobile-2026-07-25T230448.png
security:
- kind: authentication
  name: Maya Mobile Authentication
  slug: maya-mobile-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Maya Mobile Domain Security
  slug: maya-mobile-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maya-mobile
tags:
- eSIM
- Connectivity
- Mobile Data
- Roaming
- Telecom
website: https://maya.net/
---
