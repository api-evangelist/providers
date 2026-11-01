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
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/penny/hosts/penny-hosts.yml
  title: ''
  type: Hosts
  url: hosts/penny-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pennypension.com/legal/terms-and-documents
- group: operate
  title: ''
  type: Support
  url: https://pennypension.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pennypension.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/penny/security/penny-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/penny-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pennypension.com/
coverage:
  checked: '2026-10-29'
  detail: No public API or developer program is offered on the company's website.
  evidence:
  - status: 200
    url: https://pennypension.com/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Penny (operating as Penny Pension) is a fintech platform that consolidates users' pension accounts into a single mobile application, enabling effortless tracking, protection, and planning for retirement. The service offers secure aggregation of pension data, personalized insights, and tools to help users make informed decisions about their future financial wellbeing. Users can download the app to start managing their pensions in one place.
image: https://framerusercontent.com/assets/HVxxcUCbsQQ9FkqbqkoVprPROaw.jpg
layout: provider
modified: '2026-10-29'
name: Penny
nav: Providers
network: true
overview: 'Penny is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Retirement, Pensions, MobileApp, and FinancialPlanning.


  Penny''s developer surface includes support and 5 more developer resources.'
plans:
- name: Penny Plans Pricing
  plan_count: 0
  slug: penny-plans-pricing
random_paper: 2
scopes:
- name: Penny Scopes
  scope_count: 0
  slug: penny-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Penny Authentication
  slug: penny-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Penny Domain Security
  slug: penny-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: penny
tags:
- Fintech
- Retirement
- Pensions
- MobileApp
- FinancialPlanning
website: https://pennypension.com/
---
