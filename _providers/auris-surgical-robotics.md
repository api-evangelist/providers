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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auris-surgical-robotics/refs/heads/main/llms/auris-surgical-robotics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auris-surgical-robotics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auris-surgical-robotics/refs/heads/main/hosts/auris-surgical-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auris-surgical-robotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auris-surgical-robotics/refs/heads/main/vendors/auris-surgical-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auris-surgical-robotics-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.jnjmedtech.com/en-US/products/cardiovascular/carto/support/
- group: start
  title: ''
  type: SignUp
  url: https://www.jnjmedtech.com/en-US/register/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jnjmedtech.com/system/files/pdf/Privacy%20policy_0.pdf
- group: company
  title: ''
  type: Newsroom
  url: https://www.jnjmedtech.com/en-US/news/press-releases/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auris-surgical-robotics/refs/heads/main/security/auris-surgical-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auris-surgical-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jnjmedtech.com/en-US/products/robotics/monarch-platform/bronchoscopy/
coverage:
  checked: 2026-09-26
  detail: No public developer program or API documentation is available; attempts to fetch OpenAPI specs returned HTTP 403.
  evidence:
  - status: 403
    url: https://api.jnjmedtech.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Auris Health, now part of Johnson & Johnson MedTech, develops the MONARCH robotic-assisted bronchoscopy platform for lung diagnostics. The company focuses on innovative medical devices that enable physicians to navigate and biopsy hard-to-reach lung nodules, improving early detection and treatment of lung cancer. Through its integration with J&J MedTech, Auris Health leverages extensive resources to advance robotic bronchoscopy technology and expand its clinical impact worldwide.
layout: provider
modified: '2026-09-26'
name: Auris Health
nav: Providers
network: true
overview: 'Auris Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Robotics, Healthcare, and Bronchoscopy.


  Auris Health''s developer surface includes support, signup flow, and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auris Surgical Robotics Domain Security
  slug: auris-surgical-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auris-surgical-robotics
tags:
- Company
- Medical Devices
- Robotics
- Healthcare
- Bronchoscopy
website: https://www.jnjmedtech.com/en-US/products/robotics/monarch-platform/bronchoscopy/
---
