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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/assa-abloy/refs/heads/main/llms/assa-abloy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assa-abloy-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assa-abloy/refs/heads/main/hosts/assa-abloy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assa-abloy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/assa-abloy/refs/heads/main/vendors/assa-abloy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assa-abloy-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.assaabloy.com/be/fr/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.assaabloy.com/ng/en/privacy-center
- group: company
  title: ''
  type: Newsroom
  url: https://www.assaabloy.com/be/fr/stories/news
- group: start
  title: ''
  type: GettingStarted
  url: https://www.assaabloy.com/be/fr/solutions/topics/bim-specification/openings-studio/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.assaabloy.com/be/fr/service/downloads/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ASSAABLOY
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/assa-abloy/refs/heads/main/security/assa-abloy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assa-abloy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assaabloy.com/
coverage:
  checked: '2026-10-15'
  detail: Documentation pages are rendered via JavaScript with no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://www.assaabloy.com/be/fr/service/downloads/documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Assa Abloy is a global leader in access solutions, providing a wide range of electronic and mechanical locking systems, door automation, and identity management products. The company serves billions of users worldwide across sectors such as commercial buildings, residential properties, transportation, and healthcare. Through its extensive portfolio of brands, Assa Abloy delivers innovative security technologies that enhance safety and convenience, supporting digital transformation and smart building initiatives.
image: https://gw-assets.assaabloy.com/is/image/assaabloy/ASSA-ABLOY-entry-door-systems-1
layout: provider
modified: '2026-10-14'
name: Assa Abloy
nav: Providers
network: true
overview: 'Assa Abloy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Access Control, IoT, and SmartBuildings.


  Assa Abloy''s developer surface includes getting-started guide, documentation, and 9 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Assa Abloy Domain Security
  slug: assa-abloy-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: assa-abloy
tags:
- Company
- Security
- Access Control
- IoT
- SmartBuildings
website: https://assaabloy.com/
---
