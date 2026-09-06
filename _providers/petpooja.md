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
- acting_count: 4
  human_in_the_loop: 0
  name: Petpooja Agentic Access
  operation_count: 4
  slug: petpooja-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- baseURL: https://qle1yy2ydc.execute-api.ap-southeast-1.amazonaws.com/V1
  baseurl_source: declared
  description: Fetch a mapped restaurant's menu / catalog from Petpooja.
  name: Petpooja Menu API
  slug: petpooja-menu-api
- baseURL: https://qle1yy2ydc.execute-api.ap-southeast-1.amazonaws.com/V1
  baseurl_source: declared
  description: Push online orders into the Petpooja POS.
  name: Petpooja Orders API
  slug: petpooja-orders-api
- baseURL: https://qle1yy2ydc.execute-api.ap-southeast-1.amazonaws.com/V1
  baseurl_source: declared
  description: Item stock and availability.
  name: Petpooja Stock API
  slug: petpooja-stock-api
- baseURL: https://qle1yy2ydc.execute-api.ap-southeast-1.amazonaws.com/V1
  baseurl_source: declared
  description: Store / restaurant online-ordering availability.
  name: Petpooja Stores API
  slug: petpooja-stores-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Petpooja Online Ordering Menu API
  slug: open-petpooja-menu-api
- collection_type: open
  name: Petpooja Online Ordering Menu Orders API
  slug: open-petpooja-orders-api
- collection_type: open
  name: Petpooja Online Ordering Menu Stock API
  slug: open-petpooja-stock-api
- collection_type: open
  name: Petpooja Online Ordering Menu Stores API
  slug: open-petpooja-stores-api
- collection_type: open
  name: Petpooja Online Ordering API
  slug: open-petpooja
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/petpooja-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/petpooja-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/petpooja-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/petpooja-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/petpooja
- group: company
  title: ''
  type: Website
  url: https://www.petpooja.com
- group: docs
  title: ''
  type: Documentation
  url: https://onlineorderingapisv210.docs.apiary.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/petpooja-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/petpooja-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/petpooja-finops.yml
created: '2026-06-21'
description: Petpooja is a restaurant point-of-sale (POS) and management platform serving 75,000+ restaurants across India, the Middle East, Canada, and South Africa. Its Online Ordering API lets aggregators and partner ordering platforms sync a restaurant's menu/catalog, push orders into the Petpooja POS, receive order-status callbacks, and toggle item stock and store availability.
finops:
- name: Petpooja Finops
  service_category: Business Application Software
  slug: petpooja-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/petpooja.png
layout: provider
modified: '2026-06-21'
name: Petpooja
nav: Providers
network: true
overview: 'Petpooja publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Menu API, Orders API, Stock API, and 1 more. Tagged areas include Restaurant, Point-of-Sale, Online Ordering, Menus, and Food Delivery.


  Petpooja''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Petpooja Plans Pricing
  plan_count: 3
  slug: petpooja-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Petpooja Rate Limits
  slug: petpooja-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 9
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
    contract_quality: 53.6
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/petpooja/refs/heads/main/screenshots/petpooja-2026-09-02T151119.png
security:
- kind: authentication
  name: Petpooja Authentication
  slug: petpooja-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Petpooja Domain Security
  slug: petpooja-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Petpooja Vulnerability Disclosure
  slug: petpooja-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: petpooja
tags:
- Restaurant
- Point-of-Sale
- Online Ordering
- Menus
- Food Delivery
website: https://www.petpooja.com
---
