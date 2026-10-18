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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides access to sensor data, analytics and platform features for corrosion monitoring.
  name: CorrosionRadar API
  slug: corrosionradar-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/corrosionradar/refs/heads/main/hosts/corrosionradar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/corrosionradar-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corrosionradar.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://corrosionradar.com/resources/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/corrosionradar/refs/heads/main/security/corrosionradar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/corrosionradar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corrosionradar.com
- group: docs
  title: ''
  type: Documentation
  url: https://corrosionradar.com/resources/
- group: start
  title: ''
  type: GettingStarted
  url: https://corrosionradar.com/about-us/
- group: operate
  title: ''
  type: Contact
  url: https://corrosionradar.com/contact/
coverage:
  checked: '2026-10-11'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://corrosionradar.com/resources/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-11'
description: CorrosionRADAR provides an enterprise monitoring and management solution for Corrosion Under Insulation (CUI) targeting oil, gas and petrochemical operators. Their AI‑powered platform combines sensor hardware, data analytics and a cloud service to predict and mitigate hidden corrosion risks, reducing inspection costs by up to 65% and delivering ROI within six months.
layout: provider
modified: '2026-10-11'
name: Corrosionradar
nav: Providers
network: true
overview: 'Corrosionradar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oil and Gas, Corrosion, Artificial Intelligence, and Monitoring.


  Corrosionradar''s developer surface includes documentation, getting-started guide, and 6 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 7.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Corrosionradar Domain Security
  slug: corrosionradar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: corrosionradar
tags:
- Company
- Oil and Gas
- Corrosion
- Artificial Intelligence
- Monitoring
website: https://corrosionradar.com
---
