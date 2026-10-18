---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 5.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Revrule Agentic Access
  operation_count: 3
  slug: revrule-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: RevRule by Payload provides a revenue‑sharing platform with x402 USDC payment endpoints.
  name: RevRule API
  slug: revrule-api
artifact_total: 5
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/agentic-access/revrule-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/revrule-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/rules/revrule-rules.yml
  title: ''
  type: Spectral
  url: rules/revrule-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/errors/revrule-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/revrule-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/conformance/revrule-conformance.yml
  title: ''
  type: Conformance
  url: conformance/revrule-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/hosts/revrule-hosts.yml
  title: ''
  type: Hosts
  url: hosts/revrule-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.dev/openapi.json/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/authentication/revrule-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revrule-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revrule/refs/heads/main/security/revrule-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revrule-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://payload-rail.fly.dev/openapi.json
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://payload-rail.fly.dev/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: RevRule by Payload provides a revenue‑sharing platform that turns agreements and revenue streams into auditable economic entitlements. Users upload agreements, connect revenue sources, and the system calculates who is owed what. Payments are facilitated via a two‑path x402 USDC endpoint on Base, requiring a 0.01 USDC payment per event. The API supports submitting revenue events, retrieving entitlement calculations, and managing payment transactions, enabling businesses to automate revenue distribution and maintain transparent ledgers.
layout: provider
modified: '2026-10-14'
name: RevRule by Payload
nav: Providers
network: true
overview: 'RevRule by Payload is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Revenue, Payments, and Fintech.


  The RevRule by Payload catalog on APIs.io includes 1 Spectral governance ruleset.


  RevRule by Payload''s developer surface includes documentation, authentication, API reference, and 6 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: RevRule by Payload API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: revrule-rules
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Revrule Authentication
  slug: revrule-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Revrule Domain Security
  slug: revrule-domain-security
  summary_line: TLSv1.3
slug: revrule
tags:
- Company
- Revenue
- Payments
- Fintech
---
