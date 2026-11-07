---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Aggregated marketplace API providing searchable auction lot data across multiple US liquidation platforms.
  name: BStalker API
  slug: bstalker-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bstalker-com/plans/bstalker-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bstalker-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/bstalker-com/security/bstalker-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bstalker-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bstalker-com/llms/bstalker-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bstalker-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/bstalker-com/well-known/bstalker-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bstalker-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bstalker-com/well-known/bstalker-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bstalker-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bstalker-com/hosts/bstalker-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bstalker-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bstalker-com/vendors/bstalker-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bstalker-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bstalker.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://bstalker.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bstalker.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bstalker.com/guides
- group: company
  title: ''
  type: Blog
  url: https://bstalker.com/blog
- group: auth
  href: https://artifacts.apis.io/bstalker-com/security/bstalker-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bstalker-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bstalker-com/security/bstalker-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bstalker-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bstalker.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://bstalker.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bstalker.com/sign-up
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://bstalker.com/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BStalker aggregates live feeds from nine US liquidation marketplaces, providing a single searchable interface for auction lots across B‑Stock, GovDeals, Liquidation.com, DirectLiquidation, 888 Lots, Via Trading, BlueLots, Musick, and QuickBidz. Users can save searches and receive email alerts when matching lots appear. The platform offers detailed statistics on lot counts, auctions tracked, and seller‑manifest items, supporting buyers and sellers in the secondary market.
image: https://bstalker.com/opengraph-image?e09d3655cba6daad
layout: provider
modified: '2026-11-03'
name: BStalker
nav: Providers
network: true
overview: 'BStalker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Auctions, Liquidation, Aggregator, and BStalker.


  BStalker''s developer surface includes documentation, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Bstalker Com Plans Pricing
  plan_count: 2
  slug: bstalker-com-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bstalker Com Domain Security
  slug: bstalker-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bstalker Com Vulnerability Disclosure
  slug: bstalker-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bstalker-com
tags:
- Marketplace
- Auctions
- Liquidation
- Aggregator
- BStalker
website: https://bstalker.com/
---
