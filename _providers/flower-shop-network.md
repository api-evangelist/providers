---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Flower Shop Network Agentic Access
  operation_count: 11
  slug: flower-shop-network-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.flowershopnetwork.com/api/
  baseurl_source: declared
  description: Token issuance and validation
  name: Flower Shop Network Authentication API
  slug: flower-shop-network-authentication-api
- baseURL: https://api.flowershopnetwork.com/api/
  baseurl_source: declared
  description: Florist directory lookup
  name: Flower Shop Network Florists API
  slug: flower-shop-network-florists-api
- baseURL: https://api.flowershopnetwork.com/api/
  baseurl_source: declared
  description: Wire order receipt, acceptance, sending, and delivery
  name: Flower Shop Network Orders API
  slug: flower-shop-network-orders-api
- baseURL: https://api.flowershopnetwork.com/api/
  baseurl_source: declared
  description: Product catalog access
  name: Flower Shop Network Products API
  slug: flower-shop-network-products-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flower Shop Network JSON Authentication API
  slug: open-flower-shop-network-authentication-api
- collection_type: open
  name: Flower Shop Network JSON Authentication Florists API
  slug: open-flower-shop-network-florists-api
- collection_type: open
  name: Flower Shop Network JSON Authentication Orders API
  slug: open-flower-shop-network-orders-api
- collection_type: open
  name: Flower Shop Network JSON Authentication Products API
  slug: open-flower-shop-network-products-api
- collection_type: open
  name: Flower Shop Network JSON API
  slug: open-flower-shop-network
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flower-shop-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flower-shop-network-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flower-shop-network
- group: company
  title: ''
  type: Website
  url: https://www.flowershopnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.flowershopnetwork.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flowershopnetwork.com/blog/feed/
created: '2025-02-24'
description: Flower Shop Network is a platform that connects customers with local florists across the country. They provide an online marketplace where users can browse and purchase a wide variety of floral arrangements for all occasions, and expose a JSON API for partner POS systems to authenticate, look up products and florists, and exchange wire orders across the FSN florist network.
finops:
- name: Flower Shop Network Finops
  service_category: API
  slug: flower-shop-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flower-shop-network.png
layout: provider
modified: '2026-05-19'
name: Flower Shop Network
nav: Providers
network: true
overview: 'Flower Shop Network publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Florists API, Orders API, and 1 more. Tagged areas include Florists, Flowers, Wire Orders, and Point-of-Sale.


  Flower Shop Network''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Flower Shop Network Plans Pricing
  plan_count: 3
  slug: flower-shop-network-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Flower Shop Network Rate Limits
  slug: flower-shop-network-rate-limits
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flower-shop-network/refs/heads/main/screenshots/flower-shop-network-2026-06-20T181329.png
security:
- kind: domain-security
  name: Flower Shop Network Domain Security
  slug: flower-shop-network-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: flower-shop-network
tags:
- Florists
- Flowers
- Wire Orders
- Point-of-Sale
website: https://www.flowershopnetwork.com/
---
