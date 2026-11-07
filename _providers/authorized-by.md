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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/authorized-by/llms/authorized-by-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authorized-by-llms.txt
- group: agent
  href: https://artifacts.apis.io/authorized-by/well-known/authorized-by-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authorized-by-well-known.yml
- group: other
  href: https://artifacts.apis.io/authorized-by/hosts/authorized-by-hosts.yml
  title: ''
  type: Hosts
  url: hosts/authorized-by-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://www.authorized.by/blog/
- group: auth
  href: https://artifacts.apis.io/authorized-by/security/authorized-by-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authorized-by-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authorized.by/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://authorized.by/mcp
  - status: null
    url: https://www.authorized.by/mcp
  - status: 403
    url: https://app.authorized.by/api/mcp
  - status: 200
    url: https://authorized.by/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: authorized.by operates an authorization management platform that connects brands with their officially authorized retailers. The service verifies retailer identity and authorization in real time, displaying a live seal and TÜV‑ShopIdent verification to assure consumers, marketplaces and other systems of legitimate distribution channels. Brands control authorizations, can revoke them instantly, and use the platform to maintain transparent, trustworthy partnerships.
image: https://www.authorized.by/wp-content/uploads/2020/04/authorized-by-echtzeitsiegel.jpg
layout: provider
modified: '2026-11-02'
name: authorized.by
nav: Providers
network: true
overview: 'authorized.by is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Authorization, Retailer Verification, Brand Directory, Identity Verification, and Real-time Seal.


  authorized.by''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 4.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Authorized By Domain Security
  slug: authorized-by-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: authorized-by
tags:
- Authorization
- Retailer Verification
- Brand Directory
- Identity Verification
- Real-time Seal
- Marketplace Integration
website: https://authorized.by/
---
