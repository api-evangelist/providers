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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leaf-space/refs/heads/main/hosts/leaf-space-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leaf-space-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://leaf.space/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leaf-space/refs/heads/main/security/leaf-space-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leaf-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leaf.space/
- group: commercial
  title: ''
  type: Pricing
  url: https://leaf.space/price-calculator/
- group: operate
  title: ''
  type: Support
  url: https://leaf.space/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leaf.space/privacy-statement-eu/
- group: docs
  title: ''
  type: Documentation
  url: https://leaf.space/leaf-line/
- group: start
  title: ''
  type: SignUp
  url: https://leaf.space/login/
coverage:
  checked: 2026-09-23
  detail: The developer portal at https://portal.leaf.space/ returns a SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://portal.leaf.space/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Leaf Space simplifies satellite connectivity worldwide by offering a global network of ground stations, dedicated services like Leaf Line, Leaf Key, and Leaf Hosting, and innovative solutions such as TreeNet. The company provides end‑to‑end ground segment services, enabling real‑time communication, data downlink, and command & control for LEO satellites, reducing latency and increasing operational efficiency for space operators.
image: https://leaf.space/wp-content/uploads/2024/09/05.jpeg
layout: provider
modified: '2026-09-23'
name: Leaf Space
nav: Providers
network: true
overview: 'Leaf Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Connectivity, Ground Station, and Space.


  Leaf Space''s developer surface includes pricing, support, documentation, signup flow, and 5 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Leaf Space Domain Security
  slug: leaf-space-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: leaf-space
tags:
- Company
- Satellite
- Connectivity
- Ground Station
- Space
website: https://leaf.space/
---
