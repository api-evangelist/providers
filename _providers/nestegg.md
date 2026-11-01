---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/nestegg/hosts/nestegg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nestegg-hosts.yml
- group: other
  href: https://artifacts.apis.io/nestegg/vendors/nestegg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nestegg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.nestegg.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.nestegg.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://community.nestegg.ai/login
- group: other
  title: ''
  type: Leadership
  url: https://nestegg.ai/team/
- group: company
  title: ''
  type: Blog
  url: https://nestegg.ai/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.nestegg.ai/
- group: auth
  href: https://artifacts.apis.io/nestegg/security/nestegg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nestegg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nestegg.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://nestegg.ai
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: NestEgg matches UK credit union members with affordable loans, acting as a free broker that does not lend directly. It offers loans from £200 to £25,000, supports all credit histories, and does not affect credit scores. The service is funded by credit unions that pay a fee only when a loan is made, providing a not‑for‑profit, transparent lending marketplace for consumers in the United Kingdom.
image: https://nestegg.ai/wp-content/uploads/2025/08/notice-of-correction-1024x576.jpg
layout: provider
modified: '2026-10-21'
name: NestEgg
nav: Providers
network: true
overview: 'NestEgg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Lending, CreditUnion, and UK.


  NestEgg''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nestegg Domain Security
  slug: nestegg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nestegg
tags:
- Company
- FinTech
- Lending
- CreditUnion
- UK
website: https://nestegg.ai
---
