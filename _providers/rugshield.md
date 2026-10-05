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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rugshield/refs/heads/main/hosts/rugshield-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rugshield-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rugshield/refs/heads/main/security/rugshield-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rugshield-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rugshield-x402.fly.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://rugshield-x402.fly.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rugshield-x402.fly.dev/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://rugshield-x402.fly.dev/health
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://rugshield-x402.fly.dev/
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: RugShield provides a parallel Solana risk advisory API for AI agents, offering token risk checks, transaction preflight, and aggregated independent advisor panels. It operates on a pay-per-call model using x402 USDC payments on Base or Solana, with no signup or API key required. The service is publicly documented, includes an OpenAPI spec, and supports free discovery of advisor pricing and capabilities.
layout: provider
modified: '2026-09-27'
name: RugShield Solana Safety API
nav: Providers
network: true
overview: 'RugShield Solana Safety API is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solana, Risk Management, Payments, and Artificial Intelligence.


  RugShield Solana Safety API''s developer surface includes documentation, API reference, support, and 3 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rugshield Domain Security
  slug: rugshield-domain-security
  summary_line: TLSv1.3
slug: rugshield
tags:
- Company
- Solana
- Risk Management
- Payments
- Artificial Intelligence
website: https://rugshield-x402.fly.dev/
---
