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
- group: other
  href: https://artifacts.apis.io/lucidlane-com/hosts/lucidlane-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lucidlane-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/lucidlane-com/vendors/lucidlane-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lucidlane-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skylerhealth.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidlane
- group: auth
  href: https://artifacts.apis.io/lucidlane-com/security/lucidlane-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lucidlane-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skylerhealth.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.lucidlane.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Lucid Lane is a venture‑backed startup that was initially identified in the API Evangelist harvest backlog. Public information about its products, services, or API offerings is currently limited. The company appears to be associated with mental‑health and tele‑therapy services under the Skyler Health brand, as the domain lucidlane.com redirects to skylerhealth.com. No dedicated API documentation, developer portal, or official website specific to Lucid Lane could be verified at this time.
image: http://static1.squarespace.com/static/65109ce01fe2e415a3e4e68b/t/65c011657e1361611e808ab2/1757110087817/skyler-health-counseling-evaluation-logo-horizontal-light-512.png?format=1500w
layout: provider
modified: '2026-10-21'
name: Lucid Lane
nav: Providers
network: true
overview: Lucid Lane is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MentalHealth, Teletherapy, Startup, and VentureBacked.
random_paper: 13
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lucidlane Com Domain Security
  slug: lucidlane-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lucidlane-com
tags:
- Company
- MentalHealth
- Teletherapy
- Startup
- VentureBacked
website: https://www.skylerhealth.com/
---
