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
  - security
  - '{''url'': ''https://www.ezeetechnosys.com'', ''status'': 301, ''note'': ''declared website redirects to https://yanoljacloudsolution.com:443/ — a different registrable domain (ezeetechnosys.com -> yanoljacloudsolution.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- acting_count: 2
  human_in_the_loop: 0
  name: Ezee Agentic Access
  operation_count: 2
  slug: ezee-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://live.ipms247.com/pmsinterface/
  baseurl_source: declared
  description: The Inventory and Rates API from eZee Technosys — 1 operation(s) for inventory and rates.
  name: eZee Technosys Inventory and Rates API
  slug: ezee-inventory-and-rates-api
- baseURL: https://live.ipms247.com/pmsinterface/
  baseurl_source: declared
  description: The PMS Connectivity API from eZee Technosys — 1 operation(s) for pms connectivity.
  name: eZee Technosys PMS Connectivity API
  slug: ezee-pms-connectivity-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: eZee Technosys YCS Connectivity Inventory and Rates API
  slug: open-ezee-inventory-and-rates-api
- collection_type: open
  name: eZee Technosys YCS Connectivity Inventory and Rates PMS Connectivity API
  slug: open-ezee-pms-connectivity-api
- collection_type: open
  name: eZee Technosys YCS Connectivity API
  slug: open-ezee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ezee-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ezee-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezee-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ezee-technosys-pvt-ltd-/
- group: company
  title: ''
  type: Website
  url: https://www.ezeetechnosys.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.ezeetechnosys.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/ezee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ezee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ezee-finops.yml
created: '2026-06-21'
description: eZee Technosys is a hospitality technology company offering eZee Absolute (cloud hotel PMS), eZee Centrix (channel manager), eZee Reservation (booking engine), and eZee Optimus (restaurant POS). Its YCS Connectivity Portal exposes a partner-gated HTTP API for PMS connectivity, channel manager, booking engine, and POS integrations so third-party systems can sync reservations, room inventory, rates, restrictions, and guest data. eZee is now part of Yanolja Cloud (Yanolja Cloud Solution).
finops:
- name: Ezee Finops
  service_category: Hospitality Software
  slug: ezee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ezee.png
layout: provider
modified: '2026-06-21'
name: eZee Technosys
nav: Providers
network: true
overview: 'eZee Technosys publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inventory and Rates API and PMS Connectivity API. Tagged areas include Hospitality, Hotel, PMS, Channel Manager, and Reservations.


  eZee Technosys'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Ezee Plans Pricing
  plan_count: 2
  slug: ezee-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Ezee Rate Limits
  slug: ezee-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezee/refs/heads/main/screenshots/ezee-2026-07-25T214046.png
security:
- kind: authentication
  name: Ezee Authentication
  slug: ezee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ezee Domain Security
  slug: ezee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ezee Trust Center
  slug: ezee-trust-center
  summary_line: PCI DSS, GDPR
slug: ezee
tags:
- Hospitality
- Hotel
- PMS
- Channel Manager
- Reservations
website: https://www.ezeetechnosys.com
---
