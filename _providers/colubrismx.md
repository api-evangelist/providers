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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/colubrismx/refs/heads/main/hosts/colubrismx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colubrismx-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://endoquestrobotics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://endoquestrobotics.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://endoquestrobotics.com/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/colubrismx/refs/heads/main/security/colubrismx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colubrismx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://endoquestrobotics.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://endoquestrobotics.com/mcp
  - status: 200
    url: https://endoquestrobotics.com
  - status: 403
    url: https://equityzen.com/company/colubrismx
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: Colubrismx is a stub entry originating from the API Evangelist secondary‑market harvest. The company currently lacks a publicly verified corporate website, and no official API documentation or developer portal has been identified. This placeholder record will be enriched as further information becomes available, including a proper description, branding image, and link‑property pointers when they can be verified.
layout: provider
modified: '2026-10-09'
name: Colubrismx
nav: Providers
network: true
overview: Colubrismx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 18
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 37.5
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Colubrismx Domain Security
  slug: colubrismx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: colubrismx
tags:
- Company
website: https://endoquestrobotics.com
---
