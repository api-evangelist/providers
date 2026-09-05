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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Extensiv Agentic Access
  operation_count: 14
  slug: extensiv-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: OAuth2-style token endpoint (endpointsConfirmed).
  name: Extensiv Authentication API
  slug: extensiv-authentication-api
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: Customer/tenant accounts (endpointsModeled).
  name: Extensiv Customers API
  slug: extensiv-customers-api
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: On-hand inventory and stock summaries (endpointsModeled).
  name: Extensiv Inventory API
  slug: extensiv-inventory-api
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: Customer SKU/item master (endpointsModeled).
  name: Extensiv Items API
  slug: extensiv-items-api
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: Sales/fulfillment orders (endpointsModeled).
  name: Extensiv Orders API
  slug: extensiv-orders-api
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: Inbound receivers / ASNs (endpointsModeled).
  name: Extensiv Receivers API
  slug: extensiv-receivers-api
- baseURL: https://secure-wms.com
  baseurl_source: declared
  description: Physical facilities (endpointsModeled).
  name: Extensiv Warehouses API
  slug: extensiv-warehouses-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication API
  slug: open-extensiv-authentication-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication Customers API
  slug: open-extensiv-customers-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication Inventory API
  slug: open-extensiv-inventory-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication Items API
  slug: open-extensiv-items-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication Orders API
  slug: open-extensiv-orders-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication Receivers API
  slug: open-extensiv-receivers-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled) Authentication Warehouses API
  slug: open-extensiv-warehouses-api
- collection_type: open
  name: Extensiv 3PL Warehouse Manager API (modeled)
  slug: open-extensiv
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/extensiv-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/extensiv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/extensiv-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/extensiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/extensiv-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/extensiv
- group: company
  title: ''
  type: Website
  url: https://www.extensiv.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.extensiv.com/en_US/rest-api
- group: commercial
  title: ''
  type: Plans
  url: plans/extensiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/extensiv-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/extensiv-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.extensiv.com/blog
created: '2026-07-04'
description: Extensiv (formerly 3PL Central, rebranded in 2022) is a cloud-native omnichannel fulfillment software company for third-party logistics providers (3PLs) and brands. Its platform combines warehouse management (3PL Warehouse Manager and Warehouse Manager), order management, inventory management, and integration tooling - built from the combination of 3PL Central, Skubana, Scout, and CartRover. The flagship developer surface is the 3PL Warehouse Manager REST API (auth server at secure-wms.com/AuthServer), which exposes orders, inventory, items, customers, receivers/ASN, stock summaries, and warehouses to external integrators. Access is provisioned with Client ID / Client Secret credentials that mint short-lived bearer tokens. NOTE - the SecureWMS/3PL Warehouse Manager REST API itself is documented in more detail in the sibling all/3plcentral entry; this entry profiles the Extensiv company and platform and its relationship to that API.
finops:
- name: Extensiv Finops
  service_category: Supply Chain and Logistics Software
  slug: extensiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/extensiv.png
layout: provider
modified: '2026-07-04'
name: Extensiv
nav: Providers
network: true
overview: 'Extensiv publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customers API, Inventory API, and 4 more. Tagged areas include 3PL, Warehouse Management, WMS, Order Management, and Inventory Management.


  Extensiv''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Extensiv Plans Pricing
  plan_count: 4
  slug: extensiv-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Extensiv Rate Limits
  slug: extensiv-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 48.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/extensiv/refs/heads/main/screenshots/extensiv-2026-07-25T213952.png
security:
- kind: authentication
  name: Extensiv Authentication
  slug: extensiv-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Extensiv Domain Security
  slug: extensiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Extensiv Trust Center
  slug: extensiv-trust-center
  summary_line: SOC 2, GDPR
slug: extensiv
tags:
- 3PL
- Warehouse Management
- WMS
- Order Management
- Inventory Management
- Fulfillment
- Logistics
- Supply Chain
website: https://www.extensiv.com
---
