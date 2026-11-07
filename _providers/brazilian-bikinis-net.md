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
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Brazilian Bikinis Net product catalog and ordering (if any). No public machine‑readable contract was found; documentation is limited to HTML guides.
  name: Brazilian Bikinis API
  slug: brazilian-bikinis-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/brazilian-bikinis-net/plans/brazilian-bikinis-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brazilian-bikinis-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/brazilian-bikinis-net/llms/brazilian-bikinis-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brazilian-bikinis-net-llms.txt
- group: other
  href: https://artifacts.apis.io/brazilian-bikinis-net/a2a/brazilian-bikinis-net-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/brazilian-bikinis-net-a2a.yml
- group: agent
  href: https://artifacts.apis.io/brazilian-bikinis-net/well-known/brazilian-bikinis-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brazilian-bikinis-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/brazilian-bikinis-net/hosts/brazilian-bikinis-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brazilian-bikinis-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/brazilian-bikinis-net/vendors/brazilian-bikinis-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brazilian-bikinis-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brazilian-bikinis-net/security/brazilian-bikinis-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brazilian-bikinis-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brazilian-bikinis.net/
- group: docs
  title: ''
  type: Documentation
  url: https://brazilian-bikinis.net/guide/
- group: commercial
  title: ''
  type: Pricing
  url: https://brazilian-bikinis.net/faq/pricing-and-payment/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brazilian-bikinis.net/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brazilian-bikinis.net/privacy-policy/
coverage:
  checked: '2026-11-03'
  detail: No public OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract was discovered despite probing known endpoints and documentation pages.
  evidence:
  - status: 0
    url: https://api.brazilian-bikinis.net/openapi.json
  - status: 404
    url: https://brazilian-bikinis.net/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Mar Egeu is a family‑owned Brazilian swimwear manufacturer founded in 1971 in São Paulo. They design, develop and produce high‑quality swimwear for brands worldwide, offering custom designs, premium fabrics, and international shipping to over 100 countries. Their website showcases collections, pricing, and a full guide for partners looking to launch their own swimwear line.
image: https://brazilian-bikinis.net/assets/hero-model-clean.webp
layout: provider
modified: '2026-11-03'
name: Mar Egeu
nav: Providers
network: true
overview: 'Mar Egeu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Swimwear, Manufacturing, Custom Design, Brazil, and E-Commerce.


  Mar Egeu''s developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Brazilian Bikinis Net Plans Pricing
  plan_count: 1
  slug: brazilian-bikinis-net-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brazilian Bikinis Net Domain Security
  slug: brazilian-bikinis-net-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: brazilian-bikinis-net
tags:
- Swimwear
- Manufacturing
- Custom Design
- Brazil
- E-Commerce
website: https://brazilian-bikinis.net/
---
