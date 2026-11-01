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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/riley/llms/riley-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/riley-llms.txt
- group: auth
  href: https://artifacts.apis.io/riley/well-known/riley-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/riley-help-security.txt
- group: agent
  href: https://artifacts.apis.io/riley/well-known/riley-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riley-well-known.yml
- group: other
  href: https://artifacts.apis.io/riley/hosts/riley-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riley-hosts.yml
- group: other
  href: https://artifacts.apis.io/riley/vendors/riley-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riley-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rileyapp.com/tos
- group: operate
  title: ''
  type: Support
  url: https://help.rileyapp.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rileyapp.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.rileyapp.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.rileyapp.com/
- group: auth
  href: https://artifacts.apis.io/riley/security/riley-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riley-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rileyapp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://rileyapp.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Riley is a baby tracking and child development app that learns and grows with families, offering personalized, data‑backed guidance for every stage of parenting. It provides insights, milestone tracking, and expert advice to help parents feel confident and supported throughout their child’s growth journey.
image: https://www.rileyapp.com/opengraph-image.png?178767efb40a2faf
layout: provider
modified: '2026-10-24'
name: Riley
nav: Providers
network: true
overview: 'Riley is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, BabyTracker, Parenting, ChildDevelopment, and MobileApp.


  Riley''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
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
  name: Riley Domain Security
  slug: riley-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: riley
tags:
- Company
- BabyTracker
- Parenting
- ChildDevelopment
- MobileApp
website: https://rileyapp.com
---
