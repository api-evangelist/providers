---
agent_readiness:
  band: agent-aware
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://auth.smaapis.de
  baseurl_source: declared
  description: 'SMA Solar Technology API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: SMA Solar Technology API
  slug: sma-solar-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/plans/sma-solar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sma-solar-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/rules/sma-solar-rules.yml
  title: ''
  type: Spectral
  url: rules/sma-solar-rules.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/sandbox/sma-solar-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sma-solar-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sma.de/en/cybersecurity
- group: auth
  title: ''
  type: Security
  url: https://www.sma.de/en/cybersecurity/responsible-disclosure
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/conformance/sma-solar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sma-solar-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/well-known/sma-solar-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sma-solar-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/well-known/sma-solar-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sma-solar-developer-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/well-known/sma-solar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sma-solar-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/vendors/sma-solar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sma-solar-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.sma.de/newsroom/uebersicht
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/security/sma-solar-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sma-solar-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/security/sma-solar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sma-solar-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sma-solar/refs/heads/main/security/sma-solar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sma-solar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sma.de/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sma.de/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sma.de/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sma.de/
- group: operate
  title: ''
  type: Support
  url: https://developer.sma.de/contact
coverage:
  checked: 2026-09-22
  detail: Developer portal pages are HTML rendered with JavaScript and provide no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://developer.sma.de/sma-apis
  - status: null
    url: https://developer.sma.de/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: SMA Solar Technology provides inverter and photovoltaic solutions worldwide, offering a portfolio of solar energy products, developer portals, and integration APIs. The company focuses on renewable energy technologies, smart energy management, and supports developers through comprehensive documentation, sandbox environments, and API access control. SMA serves residential, commercial, and utility-scale solar installations, emphasizing sustainability and innovation in solar power generation.
image: https://www.sma.de/adobe/dynamicmedia/deliver/dm-aid--316c062b-1b27-4abb-a3d2-11d3c7afa475/sma-solar-technology-16-9.jpg?width=1200&crop=0.0p,3.3p,100.0p,93.3p&quality=85&preferwebp=true
layout: provider
modified: '2026-09-22'
name: SMA Solar Technology
nav: Providers
network: true
overview: 'SMA Solar Technology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Energy, Inverters, and Renewables.


  The SMA Solar Technology catalog on APIs.io includes 1 Spectral governance ruleset.


  SMA Solar Technology''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, and 14 more developer resources.'
plans:
- name: Sma Solar Plans Pricing
  plan_count: 10
  slug: sma-solar-plans-pricing
random_paper: 9
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: SMA Solar Technology API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: sma-solar-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.6
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 40.5
    discoverability: 68.5
    operational_transparency: 10.5
  previous_composite: 43.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.7
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sma Solar Domain Security
  slug: sma-solar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sma Solar Vulnerability Disclosure
  slug: sma-solar-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sma Solar Trust Center
  slug: sma-solar-trust-center
  summary_line: ISO 27001, GDPR
slug: sma-solar
tags:
- Company
- Solar
- Energy
- Inverters
- Renewables
website: https://www.sma.de/
---
