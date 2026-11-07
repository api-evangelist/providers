---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.postex.pk/services/integration/api/order
  baseurl_source: declared
  description: Booking, tracking, and listing shipment orders
  name: PostEx Orders API
  slug: postex-orders-api
- baseURL: https://api.postex.pk/services/integration/api/order
  baseurl_source: declared
  description: Operational cities and merchant address reference data
  name: PostEx Reference API
  slug: postex-reference-api
artifact_total: 8
collections:
- collection_type: open
  name: PostEx Merchant Order Integration Orders API
  slug: open-postex-orders-api
- collection_type: open
  name: PostEx Merchant Order Integration Orders Reference API
  slug: open-postex-reference-api
common:
- group: company
  title: ''
  type: Blog
  url: https://postex.pk/blogs
- group: other
  href: https://artifacts.apis.io/postex/overlays/postex-order-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/postex-order-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/postex/security/postex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postex.pk
- group: agent
  href: https://artifacts.apis.io/postex/mcp/postex-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/postex-mcp.yml
- group: agent
  href: https://artifacts.apis.io/postex/llms/postex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postex-llms.txt
- group: agent
  href: https://artifacts.apis.io/postex/well-known/postex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postex-well-known.yml
- group: agent
  href: https://artifacts.apis.io/postex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/postex/authentication/postex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postex-authentication.yml
created: '2026-07-17'
description: PostEx is a Pakistani e-commerce logistics, courier, and fintech platform that provides cash-on-delivery parcel fulfilment with instant upfront payments to online merchants, alongside a business suite for expense management, working- capital financing, and the XPay payment gateway. Merchants and order- management systems integrate with PostEx through its merchant Order Integration API (https://api.postex.pk) to book shipments, look up operational cities and pickup addresses, track parcels, and reconcile orders. This profile was enriched by API Evangelist by live-probing the production API host, which confirmed a real merchant integration surface authenticated with a token request header. PostEx is backed by 500 Global.
image: https://postex.pk/favicon.ico
layout: provider
modified: '2026-10-06'
name: PostEx
nav: Providers
network: true
overview: 'PostEx publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Orders API and Reference API. Tagged areas include Company, Logistics, Couriers, Shipping, and E-Commerce.


  The PostEx catalog on APIs.io includes 1 Spectral governance ruleset.


  PostEx''s developer surface includes engineering blog, authentication, and 7 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: PostEx API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: postex-rules
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 50.2
    developer_ergonomics: 16.1
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - pakistan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 23.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/postex/postex-2026-09-02T151830.png
security:
- kind: authentication
  name: Postex Authentication
  slug: postex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postex Domain Security
  slug: postex-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: Book and track a PostEx shipment
  slug: postex-book-and-track-order
slug: postex
tags:
- Company
- Logistics
- Couriers
- Shipping
- E-Commerce
- Fulfillment
- Cash on Delivery
- Payments
- Fintech
- Pakistan
website: https://postex.pk
---
