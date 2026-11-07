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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/silverware/well-known/silverware-mypass2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/silverware-mypass2-security.txt
- group: auth
  href: https://artifacts.apis.io/silverware/well-known/silverware-dashboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/silverware-dashboard-security.txt
- group: agent
  href: https://artifacts.apis.io/silverware/well-known/silverware-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/silverware-well-known.yml
- group: other
  href: https://artifacts.apis.io/silverware/hosts/silverware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/silverware-hosts.yml
- group: other
  href: https://artifacts.apis.io/silverware/vendors/silverware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/silverware-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.silverwarepos.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.silverwarepos.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.silverwarepos.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.silverwarepos.com/newsroom/tag/Blog
- group: auth
  href: https://artifacts.apis.io/silverware/security/silverware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/silverware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://silverwarepos.com/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts found despite probing known hosts.
  evidence:
  - status: 200
    url: https://www.silverwarepos.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Silverware provides a comprehensive point‑of‑sale (POS) platform for the hospitality industry, offering solutions for restaurants, hotels, bars, and other food‑service venues. Their suite includes point‑of‑sale software, guest experience tools, online ordering, mobile technology, loyalty programs, and device‑as‑a‑service options, all designed to streamline operations and enhance customer engagement across multi‑unit enterprises.
image: http://static1.squarespace.com/static/68077a1da623b161a37467f0/t/68f255fef038f630de703133/1760712190529/SilverwareLogo2025.png?format=1500w
layout: provider
modified: '2026-10-28'
name: Silverware
nav: Providers
network: true
overview: 'Silverware is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Point-of-Sale, Restaurant, Hotels, and Software.


  Silverware''s developer surface includes support, engineering blog, and 9 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 49.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.1
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/silverware/silverware-2026-11-03T143215.png
security:
- kind: domain-security
  name: Silverware Domain Security
  slug: silverware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silverware
tags:
- Hospitality
- Point-of-Sale
- Restaurant
- Hotels
- Software
website: https://silverwarepos.com/
---
