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
    mcp_server: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/durchblicker/well-known/durchblicker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/durchblicker-well-known.yml
- group: other
  href: https://artifacts.apis.io/durchblicker/hosts/durchblicker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/durchblicker-hosts.yml
- group: other
  href: https://artifacts.apis.io/durchblicker/vendors/durchblicker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/durchblicker-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://durchblicker.at/anbieter/telefonundinternet/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/durchblicker
- group: auth
  href: https://artifacts.apis.io/durchblicker/security/durchblicker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/durchblicker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://durchblicker.at
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://durchblicker.at/impressum
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://partner.durchblicker.at/api/mcp
  - status: 200
    url: https://durchblicker.at
  reason: partner-login
  state: gated
created: '2026-11-06'
description: Durchblicker is an Austrian online platform that helps consumers compare and select insurance, electricity, gas, credit, internet and mobile phone tariffs. The site offers a wide range of comparison tools for auto, motorcycle, household, home, travel, legal protection, life, accident, liability, pet, e‑bike, bicycle, and health insurance, as well as energy providers and various loan products. Users can get personalized offers, read guides, and submit claims directly through the portal, simplifying the process of finding the best deals across multiple financial and utility services.
image: https://durchblicker.at/res/img/og/savings-slogan/extended.png
layout: provider
modified: '2026-11-06'
name: Durchblicker
nav: Providers
network: true
overview: 'Durchblicker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Finance, Comparison, and Austria.


  Durchblicker''s developer surface includes support and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 14.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Durchblicker Domain Security
  slug: durchblicker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: durchblicker
tags:
- Company
- Insurance
- Finance
- Comparison
- Austria
website: https://durchblicker.at
---
