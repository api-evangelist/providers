---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Datalastic Agentic Access
  operation_count: 12
  slug: datalastic-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 1
apis:
- description: Past AIS positions for vessels and zones.
  name: Datalastic Historical API
  slug: datalastic-historical-api
- description: Real-time AIS vessel position and voyage data.
  name: Datalastic Live Tracking API
  slug: datalastic-live-tracking-api
- description: Global maritime port search.
  name: Datalastic Ports API
  slug: datalastic-ports-api
- description: Asynchronous bulk report jobs and account usage statistics.
  name: Datalastic Reports and Usage API
  slug: datalastic-reports-and-usage-api
- description: Static ship specifications and vessel search.
  name: Datalastic Vessel Data API
  slug: datalastic-vessel-data-api
- description: Vessels within a radius of a point, port, or moving vessel.
  name: Datalastic Zone Traffic API
  slug: datalastic-zone-traffic-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Datalastic Maritime Historical API
  slug: open-datalastic-historical-api
- collection_type: open
  name: Datalastic Maritime Historical Live Tracking API
  slug: open-datalastic-live-tracking-api
- collection_type: open
  name: Datalastic Maritime Historical Ports API
  slug: open-datalastic-ports-api
- collection_type: open
  name: Datalastic Maritime Historical Reports and Usage API
  slug: open-datalastic-reports-and-usage-api
- collection_type: open
  name: Datalastic Maritime Historical Vessel Data API
  slug: open-datalastic-vessel-data-api
- collection_type: open
  name: Datalastic Maritime Historical Zone Traffic API
  slug: open-datalastic-zone-traffic-api
- collection_type: open
  name: Datalastic Maritime API
  slug: open-datalastic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datalastic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datalastic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datalastic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datalastic/
- group: company
  title: ''
  type: Website
  url: https://datalastic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datalastic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://datalastic.com/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://datalastic.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/datalastic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datalastic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/datalastic-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://datalastic.com/blog/
created: '2026-07-11'
description: Datalastic is a maritime data API providing real-time AIS vessel tracking, historical ship movements, vessel specifications, and global port data over a simple REST interface. A database of 750,000+ ships is queryable by MMSI, IMO, or UUID for live position, speed, course, heading, destination, and ETA, plus zone traffic monitoring around any coordinate or port, up to 31 days of historical track per request, vessel and port finder search, and asynchronous bulk reports. Access is subscription-based with a monthly credit model and api-key authentication.
finops:
- name: Datalastic Finops
  service_category: Maritime Data and Vessel Tracking
  slug: datalastic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datalastic.png
layout: provider
modified: '2026-07-11'
name: Datalastic
nav: Providers
network: true
overview: 'Datalastic publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Historical API, Live Tracking API, Ports API, and 3 more. Tagged areas include Vessel Tracking, Maritime, AIS, Ships, and Ports.


  Datalastic''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Datalastic Plans Pricing
  plan_count: 6
  slug: datalastic-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 7
  name: Datalastic Rate Limits
  slug: datalastic-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datalastic/refs/heads/main/screenshots/datalastic-2026-07-25T211330.png
security:
- kind: authentication
  name: Datalastic Authentication
  slug: datalastic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Datalastic Domain Security
  slug: datalastic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datalastic
tags:
- Vessel Tracking
- Maritime
- AIS
- Ships
- Ports
- Shipping
website: https://datalastic.com
---
