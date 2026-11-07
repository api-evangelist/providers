---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/airfreightprice-com/llms/airfreightprice-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airfreightprice-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/airfreightprice-com/well-known/airfreightprice-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airfreightprice-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/airfreightprice-com/hosts/airfreightprice-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/airfreightprice-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/airfreightprice-com/vendors/airfreightprice-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/airfreightprice-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/airfreightprice-com/security/airfreightprice-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airfreightprice-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airfreightprice.com/
- group: company
  title: ''
  type: Blog
  url: https://airfreightprice.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airfreightprice.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airfreightprice.com/en/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://airfreightprice.com/en/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://airfreightprice.com/pricing-methodology/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found at the provider’s API host.
  evidence:
  - status: 0
    url: https://api.airfreightprice.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Air Freight Price provides an instant air freight rate calculator and comparison platform, offering transparent pricing across 50+ carriers and 200+ countries. Users can obtain indicative rates, request precise quotes, and access detailed service level information. The site emphasizes fast 24‑hour quote responses, GDPR compliance, and a range of services from express to economy shipping, supporting various cargo types and international routes.
layout: provider
modified: '2026-11-01'
name: Air Freight Price
nav: Providers
network: true
overview: 'Air Freight Price is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight, Shipping, Rate Calculator, and Air Cargo.


  Air Freight Price''s developer surface includes engineering blog, pricing, and 9 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 11.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Airfreightprice Com Domain Security
  slug: airfreightprice-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: airfreightprice-com
tags:
- Logistics
- Freight
- Shipping
- Rate Calculator
- Air Cargo
website: https://airfreightprice.com/
---
