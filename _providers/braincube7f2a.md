---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation not publicly available; no machine-readable contract discovered.
  name: Braincube API
  slug: braincube-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braincube7f2a/refs/heads/main/llms/braincube7f2a-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/braincube7f2a-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braincube7f2a/refs/heads/main/well-known/braincube7f2a-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/braincube7f2a-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braincube7f2a/refs/heads/main/hosts/braincube7f2a-hosts.yml
  title: ''
  type: Hosts
  url: hosts/braincube7f2a-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braincube7f2a/refs/heads/main/vendors/braincube7f2a-vendors.yml
  title: ''
  type: Vendors
  url: vendors/braincube7f2a-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://braincube.com/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://braincube.com/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://braincube.com/privacy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braincube7f2a/refs/heads/main/security/braincube7f2a-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braincube7f2a-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://braincube.com
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on discovered hosts.
  evidence:
  - status: 200
    url: https://braincube.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Braincube is a real-time process optimization platform delivering industrial AI solutions for manufacturers. It provides a cloud-based analytics suite that ingests plant data, applies advanced algorithms, and offers actionable insights to reduce variability, improve margin, and accelerate decision-making across industries such as pulp & paper, building materials, tires, food & beverage, and mining. The company emphasizes continuous adaptation of operations, supporting roles from leadership to frontline teams, and offers a range of tools including productivity management, process engineering, and resource optimization.
image: https://16d524a6.delivery.rocketcdn.me/wp-content/uploads/2024/12/Logo-Partners-1.svg
layout: provider
modified: '2026-10-03'
name: Braincube7f2a
nav: Providers
network: true
overview: Braincube7f2a publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial AI, Process Optimization, Manufacturing, and Real-Time Analytics.
random_paper: 11
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Braincube7F2A Domain Security
  slug: braincube7f2a-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: braincube7f2a
tags:
- Company
- Industrial AI
- Process Optimization
- Manufacturing
- Real-Time Analytics
website: https://braincube.com
---
