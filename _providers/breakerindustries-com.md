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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/breakerindustries-com/security/breakerindustries-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/breakerindustries-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/breakerindustries-com/llms/breakerindustries-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breakerindustries-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/breakerindustries-com/well-known/breakerindustries-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breakerindustries-com-security.txt
- group: agent
  href: https://artifacts.apis.io/breakerindustries-com/well-known/breakerindustries-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breakerindustries-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/breakerindustries-com/hosts/breakerindustries-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breakerindustries-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/breakerindustries-com/vendors/breakerindustries-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breakerindustries-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://breakerindustries.com/news/
- group: auth
  href: https://artifacts.apis.io/breakerindustries-com/security/breakerindustries-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/breakerindustries-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/breakerindustries-com/security/breakerindustries-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breakerindustries-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breakerindustries.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://breakerindustries.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://breakerindustries.com/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://breakerindustries.com/contact/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://breakerindustries.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Breaker Industries provides advanced energy management solutions for industrial facilities, enabling real-time monitoring, predictive maintenance, and optimization of power usage across complex operations. Their platform integrates IoT sensors, AI-driven analytics, and a robust API suite that allows customers to retrieve device data, control equipment, and automate workflows. Backed by Bessemer Venture Partners, Breaker aims to reduce energy costs and carbon footprints while improving operational efficiency for manufacturers, data centers, and large-scale infrastructure.
image: https://breakerindustries.com/img/ui/og-default.jpg
layout: provider
modified: '2026-10-21'
name: Breaker
nav: Providers
network: true
overview: Breaker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, IoT, Artificial Intelligence, Sustainability, and Industrial.
random_paper: 10
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 56.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/breakerindustries-com/breakerindustries-com-2026-11-03T122527.png
security:
- kind: domain-security
  name: Breakerindustries Com Domain Security
  slug: breakerindustries-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Breakerindustries Com Vulnerability Disclosure
  slug: breakerindustries-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: breakerindustries-com
tags:
- Energy
- IoT
- Artificial Intelligence
- Sustainability
- Industrial
website: https://breakerindustries.com/
---
