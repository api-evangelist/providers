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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-10-03'
api_count: 1
apis:
- baseURL: https://proof-random-api.pn-26f.workers.dev
  baseurl_source: spec
  description: The Random API from Proof Random API (Kepler Ops) — 1 operation(s) for random.
  name: Proof Random API (Kepler Ops) Random API
  slug: proof-random-api-random-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proof-random-api/refs/heads/main/rules/proof-random-api-rules.yml
  title: ''
  type: Spectral
  url: rules/proof-random-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proof-random-api/refs/heads/main/errors/proof-random-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/proof-random-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proof-random-api/refs/heads/main/conformance/proof-random-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/proof-random-api-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/proof-random-api/refs/heads/main/hosts/proof-random-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/proof-random-api-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/proof-random-api/refs/heads/main/vendors/proof-random-api-vendors.yml
  title: ''
  type: Vendors
  url: vendors/proof-random-api-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proof-random-api/refs/heads/main/security/proof-random-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proof-random-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://proof-random-api.pn-26f.workers.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://proof-random-api.pn-26f.workers.dev/openapi.json
- group: agent
  title: ''
  type: llms.txt
  url: https://proof-random-api.pn-26f.workers.dev/llms.txt
created: '2026-09-27'
description: Proof Random API (Kepler Ops) provides a free public randomness service by relaying the drand quicknet beacon. It offers a simple endpoint to derive reproducible integers from the latest beacon using a user‑supplied nonce. The API returns the sampled value, beacon round, signature digest verification, and indicates that no BLS verification or x402 billing is performed. This service is intended for non‑adversarial use cases such as testing, demos, or low‑stakes applications.
image: https://proof-random-api.pn-26f.workers.dev/logo.png
layout: provider
modified: '2026-09-27'
name: Proof Random API (Kepler Ops)
nav: Providers
network: true
overview: 'Proof Random API (Kepler Ops) publishes 1 API on the [APIs.io](https://apis.io/) network: Random API. Tagged areas include Company, Randomness, Public APIs, Drand, and Free Service.


  The Proof Random API (Kepler Ops) catalog on APIs.io includes 1 Spectral governance ruleset.


  Proof Random API (Kepler Ops)''s developer surface includes API reference and 8 more developer resources.'
random_paper: 11
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Proof Random API (Kepler Ops) API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: proof-random-api-rules
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Proof Random Api Domain Security
  slug: proof-random-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: proof-random-api
tags:
- Company
- Randomness
- Public APIs
- Drand
- Free Service
website: https://proof-random-api.pn-26f.workers.dev/
---
