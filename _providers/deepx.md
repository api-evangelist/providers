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
  href: https://artifacts.apis.io/deepx/well-known/deepx-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deepx-clarity-security.txt
- group: agent
  href: https://artifacts.apis.io/deepx/well-known/deepx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deepx-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: other
  href: https://artifacts.apis.io/deepx/hosts/deepx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepx-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepx/vendors/deepx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepx-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepx.co.jp/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/deepx/security/deepx-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deepx-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deepx/security/deepx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deepx.co.jp
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://deepx.co.jp/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: DeepX Inc. is a robotics and AI startup that develops autonomous operation technologies for construction machinery such as excavators, backhoes, and bulldozers. It integrates these solutions into active job sites to automate heavy equipment and provide real‑time site visualization. The company works with construction firms to address on‑site challenges through automation and remote control.
image: https://www.deepx.co.jp/wp-content/uploads/icons/ogp.jpg
layout: provider
modified: '2026-10-22'
name: Deepx
nav: Providers
network: true
overview: Deepx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Construction Automation, Heavy Equipment, Artificial Intelligence, and Site Visualization.
random_paper: 6
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
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deepx Domain Security
  slug: deepx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Deepx Vulnerability Disclosure
  slug: deepx-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deepx
tags:
- Robotics
- Construction Automation
- Heavy Equipment
- Artificial Intelligence
- Site Visualization
- Remote Control
website: https://deepx.co.jp
---
