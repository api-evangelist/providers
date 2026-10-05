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
api_count: 1
apis:
- description: API for Axiom Cloud blockchain trading services
  name: Axiom Cloud API
  slug: axiom-cloud-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axiom-cloud/refs/heads/main/llms/axiom-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axiom-cloud-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axiom-cloud/refs/heads/main/well-known/axiom-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axiom-cloud-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-cloud/refs/heads/main/hosts/axiom-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiom-cloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axiom-cloud/refs/heads/main/vendors/axiom-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiom-cloud-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axiom.trade/getting-started/signup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axiom.trade/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axiom-cloud/refs/heads/main/security/axiom-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiom-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiom.trade
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI or other machine‑readable contract found on API or docs hosts.
  evidence:
  - status: 425
    url: https://api.axiom.trade/openapi.json
  - status: 404
    url: https://docs.axiom.trade/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Axiom Cloud provides a suite of blockchain-based trading and settlement services, offering APIs for on‑chain asset management, market data, and automated trading. The platform aims to simplify decentralized finance integration for developers and enterprises, delivering secure, scalable, and compliant solutions across multiple blockchain networks. It supports real‑time data feeds, order execution, and portfolio analytics through RESTful endpoints and WebSocket streams.
layout: provider
modified: '2026-09-27'
name: Axiom Cloud
nav: Providers
network: true
overview: 'Axiom Cloud publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Trading, and Fintech.


  Axiom Cloud''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.2
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
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 5.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiom Cloud Domain Security
  slug: axiom-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: axiom-cloud
tags:
- Company
- Blockchain
- Trading
- Fintech
website: https://axiom.trade
---
