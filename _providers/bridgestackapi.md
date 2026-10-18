---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
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
  score: 17.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.bridgestackapi.com
  baseurl_source: declared
  description: The BridgeStackAPI API API from BridgeStackAPI — 1 operation(s) for bridgestackapi api.
  name: BridgeStackAPI BridgeStackAPI API
  slug: bridgestackapi-bridgestackapi-api-api
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/well-known/bridgestackapi-bridgestackapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bridgestackapi-bridgestackapi-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/well-known/bridgestackapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bridgestackapi-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/rules/bridgestackapi-rules.yml
  title: ''
  type: Spectral
  url: rules/bridgestackapi-rules.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/authentication/bridgestackapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bridgestackapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/conformance/bridgestackapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bridgestackapi-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/hosts/bridgestackapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgestackapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/vendors/bridgestackapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridgestackapi-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://bridgestackapi.statuspage.io/
- group: start
  title: ''
  type: Login
  url: https://www.bridgestackapi.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.bridgestackapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.bridgestackapi.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bridgestackapi.com/docs/getting-started/quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bridgestackapi/refs/heads/main/security/bridgestackapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgestackapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgestackapi.com/
created: '2026-10-16'
description: BridgeStackAPI provides a lightweight API gateway that enables per‑client usage control, rate‑limiting, and custom routing without rebuilding the gateway. It offers dashboards, real‑time logs, and integration guides for Node.js, cURL, and Python, helping developers quickly enforce policies and monitor API consumption.
layout: provider
modified: '2026-10-16'
name: BridgeStackAPI
nav: Providers
network: true
overview: 'BridgeStackAPI is listed with 1 API on the [APIs.io](https://apis.io/) network: BridgeStackAPI API. Tagged areas include API Gateway, Usage Control, B2B SaaS, and External APIs.


  The BridgeStackAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  BridgeStackAPI''s developer surface includes authentication, documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: BridgeStackAPI API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: bridgestackapi-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 11.9
    developer_ergonomics: 40.5
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Bridgestackapi Authentication
  slug: bridgestackapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bridgestackapi Domain Security
  slug: bridgestackapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bridgestackapi
tags:
- API Gateway
- Usage Control
- B2B SaaS
- External APIs
website: https://bridgestackapi.com/
---
