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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/deciphex/hosts/deciphex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deciphex-hosts.yml
- group: other
  href: https://artifacts.apis.io/deciphex/vendors/deciphex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deciphex-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.deciphex.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deciphex.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.deciphex.com/news
- group: auth
  href: https://artifacts.apis.io/deciphex/security/deciphex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deciphex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deciphex.com
coverage:
  checked: '2026-10-22'
  detail: OpenAPI spec not found at https://api.deciphex.com/openapi.json (no response)
  evidence:
  - status: 0
    url: https://api.deciphex.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Deciphex builds a global network of AI‑empowered pathologists using its CipherX engine to provide precise, accessible pathology diagnostics. The platform aims to reduce wait times, improve drug development, and democratize high‑quality pathology services worldwide, leveraging artificial intelligence to assist clinicians and researchers.
image: https://cdn.prod.website-files.com/66fa983bd1cac285a7ea821b/670f7579c85728f342c54ec6_Deciphex_Open%20Graph.avif
layout: provider
modified: '2026-10-22'
name: Deciphex
nav: Providers
network: true
overview: Deciphex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Pathology, Healthcare, and Diagnostics.
random_paper: 2
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deciphex Domain Security
  slug: deciphex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deciphex
tags:
- Company
- Artificial Intelligence
- Pathology
- Healthcare
- Diagnostics
website: https://www.deciphex.com
---
