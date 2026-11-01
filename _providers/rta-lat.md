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
api_count: 1
apis:
- description: Zero‑knowledge proof service exposing tools/list and verify_proof via MCP JSON‑RPC.
  name: RTA MCP
  slug: rta-mcp
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/rta-lat/llms/rta-lat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rta-lat-llms.txt
- group: agent
  href: https://artifacts.apis.io/rta-lat/well-known/rta-lat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rta-lat-well-known.yml
- group: other
  href: https://artifacts.apis.io/rta-lat/hosts/rta-lat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rta-lat-hosts.yml
- group: other
  href: https://artifacts.apis.io/rta-lat/vendors/rta-lat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rta-lat-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rta-lat/security/rta-lat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rta-lat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rta.lat/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found; only MCP JSON‑RPC tools/list is available.
  evidence:
  - status: 200
    url: https://rta.lat/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: RTA (ṚTA) provides a privacy‑preserving proof‑of‑concept service that allows agents to prove that certain conditions hold without revealing the underlying data. Using cryptographic zero‑knowledge techniques, RTA enables verification of account age, balances, stakes, and transaction counts via simple API calls. The platform operates on Base mainnet with a pay‑per‑use model, offering a free tier for up to 20 checks per day and paid plans for higher volume. No account creation or credit card is required; users interact through wallet‑based payments. Documentation, status, and demo pages are publicly accessible, and the service includes a sandbox environment for testing.
layout: provider
modified: '2026-10-30'
name: rta-lat
nav: Providers
network: true
overview: rta-lat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Privacy, Zero-Knowledge, Proof-of-Concept, Blockchain, and API.
random_paper: 21
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rta Lat Domain Security
  slug: rta-lat-domain-security
  summary_line: TLSv1.3
slug: rta-lat
tags:
- Privacy
- Zero-Knowledge
- Proof-of-Concept
- Blockchain
- API
website: https://rta.lat/
---
