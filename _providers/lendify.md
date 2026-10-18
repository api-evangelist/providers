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
- description: Lendify's financing platform API (no public machine‑readable spec discovered).
  name: Lendify API
  slug: lendify-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lendify/refs/heads/main/hosts/lendify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lendify-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lendify/refs/heads/main/security/lendify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lendify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lendify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://lendify.com/om-oss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lendify.com/privacy-policy
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on api.lendify.com or lendify.com.
  evidence:
  - status: 60
    url: https://api.lendify.com/openapi.json
  - status: 404
    url: https://lendify.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Lendify provides financing solutions for businesses in Sweden, offering factoring, corporate loans, real‑estate loans, and consumer credit. Their platform enables fast cash flow improvements with quick approvals, flexible terms, and transparent pricing, aiming to support growth for companies of all sizes.
layout: provider
modified: '2026-10-15'
name: Lendify
nav: Providers
network: true
overview: 'Lendify is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, B2B, Factoring, Loans, and Sweden.


  Lendify''s developer surface includes documentation and 4 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lendify Domain Security
  slug: lendify-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: lendify
tags:
- Finance
- B2B
- Factoring
- Loans
- Sweden
website: https://lendify.com/
---
