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
  band: human-only
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Loyalty program API documented at the provider's help site.
  name: CartaMe Loyalty
  slug: cartame-loyalty
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cartame/hosts/cartame-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cartame-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cartame.by/doc/privacy_policy.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://cartame.by/company/news/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cartame.by/
- group: auth
  href: https://artifacts.apis.io/cartame/security/cartame-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cartame-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cartame.by
coverage:
  checked: '2026-10-07'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on any discovered host.
  evidence:
  - status: 200
    url: https://help.cartame.by/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: 'Cartame is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://cartame.by/local/templates/CartameDesign/screenshot.jpg
layout: provider
modified: '2026-10-07'
name: Cartame
nav: Providers
network: true
overview: 'Cartame is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, Rewards, Retail, and Mobile App.


  Cartame''s developer surface includes documentation and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 40.2
    operational_transparency: 0.0
  previous_composite: 7.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cartame/cartame-2026-11-03T123424.png
security:
- kind: domain-security
  name: Cartame Domain Security
  slug: cartame-domain-security
  summary_line: TLSv1.3
slug: cartame
tags:
- Loyalty
- Rewards
- Retail
- Mobile App
website: https://cartame.by
---
