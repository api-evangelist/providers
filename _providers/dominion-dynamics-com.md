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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/dominion-dynamics-com/security/dominion-dynamics-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dominion-dynamics-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dominion-dynamics-com/llms/dominion-dynamics-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dominion-dynamics-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/dominion-dynamics-com/well-known/dominion-dynamics-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dominion-dynamics-com-security.txt
- group: agent
  href: https://artifacts.apis.io/dominion-dynamics-com/well-known/dominion-dynamics-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dominion-dynamics-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dominion-dynamics-com/hosts/dominion-dynamics-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dominion-dynamics-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dominion-dynamics-com/vendors/dominion-dynamics-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dominion-dynamics-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.defendthedominion.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.defendthedominion.com/news
- group: start
  title: ''
  type: Login
  url: https://www.defendthedominion.com/applicant/login
- group: company
  title: ''
  type: Website
  url: https://www.defendthedominion.com/
- group: auth
  href: https://artifacts.apis.io/dominion-dynamics-com/security/dominion-dynamics-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dominion-dynamics-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dominion-dynamics-com/security/dominion-dynamics-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dominion-dynamics-com-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.dominion-dynamics.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Dominion Dynamics provides advanced energy management and automation solutions for industrial and commercial facilities. Leveraging real-time data analytics, IoT sensors, and AI-driven optimization, the platform helps clients reduce energy consumption, improve operational efficiency, and achieve sustainability goals. Backed by Bessemer Venture Partners, the company focuses on delivering scalable, cloud-native services that integrate with existing building management systems and support predictive maintenance.
image: https://www.defendthedominion.com/og.jpg
layout: provider
modified: '2026-10-21'
name: Dominion Dynamics
nav: Providers
network: true
overview: Dominion Dynamics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, IoT, Automation, and Sustainability.
random_paper: 14
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dominion Dynamics Com Domain Security
  slug: dominion-dynamics-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dominion Dynamics Com Vulnerability Disclosure
  slug: dominion-dynamics-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dominion-dynamics-com
tags:
- Company
- Energy
- IoT
- Automation
- Sustainability
website: https://www.defendthedominion.com/
---
