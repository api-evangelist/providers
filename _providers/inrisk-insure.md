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
api_count: 1
apis:
- description: API allows integration with InRisk platform for insurance policy management. Documented at the Configuration & Integrations page.
  name: InRisk API
  slug: inrisk-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/inrisk-insure/hosts/inrisk-insure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inrisk-insure-hosts.yml
- group: other
  href: https://artifacts.apis.io/inrisk-insure/vendors/inrisk-insure-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inrisk-insure-vendors.yml
- group: auth
  href: https://artifacts.apis.io/inrisk-insure/security/inrisk-insure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inrisk-insure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inrisklabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://inrisklabs.com/
- group: company
  title: ''
  type: Blog
  url: https://inrisklabs.com/blogs
- group: start
  title: ''
  type: GettingStarted
  url: https://inrisklabs.com/solutions/crop
created: '2026-10-21'
description: InRisk provides parametric insurance solutions leveraging advanced data and technology to help governments, development agencies, insurers, and intermediaries manage climate and disaster risk. Their platform offers tailored products for crops, livestock, energy, infrastructure and more, delivering rapid, transparent payouts based on objective weather data. InRisk aims to redefine risk financing through proactive, data‑driven methodologies, supporting a wide range of stakeholders in building resilient economies.
image: https://firebasestorage.googleapis.com/v0/b/inrisk-labs.firebasestorage.app/o/assets%2Finrisk-logo.svg?alt=media
layout: provider
modified: '2026-10-21'
name: InRisk
nav: Providers
network: true
overview: 'InRisk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, ClimateTech, Parametric, and FinTech.


  InRisk''s developer surface includes documentation, engineering blog, getting-started guide, and 4 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Inrisk Insure Domain Security
  slug: inrisk-insure-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: inrisk-insure
tags:
- Company
- Insurance
- ClimateTech
- Parametric
- FinTech
website: https://inrisklabs.com/
---
