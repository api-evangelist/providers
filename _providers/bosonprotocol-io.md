---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Boson Protocol enabling secure, agentic commerce for digital and physical assets.
  name: Boson Protocol API
  slug: boson-protocol-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bosonprotocol-io/hosts/bosonprotocol-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bosonprotocol-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/bosonprotocol-io/vendors/bosonprotocol-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bosonprotocol-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bosonprotocol.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bosonprotocol.io/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bosonprotocol
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bosonprotocol.io/docs/quickstart/x402-server/
- group: company
  title: ''
  type: Blog
  url: https://www.bosonprotocol.io/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.bosonprotocol.io/
- group: auth
  href: https://artifacts.apis.io/bosonprotocol-io/security/bosonprotocol-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bosonprotocol-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bosonprotocol.io/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no machine-readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 500
    url: https://dev.bosonprotocol.io/openapi.json
  - status: 500
    url: https://dev.bosonprotocol.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Boson Protocol enables secure, agentic commerce for digital and physical assets, allowing exchange with strong commitments that transactions execute as agreed or not at all. It provides a decentralized protocol for creating, managing, and transacting on tokenized assets, supporting escrow, dispute resolution, and zero platform fees, aimed at empowering creators, buyers, and agents in a trustless environment.
image: https://bosonwp.wpengine.com/wp-content/uploads/2025/11/Thumbnail.png
layout: provider
modified: '2026-11-02'
name: Boson Protocol
nav: Providers
network: true
overview: 'Boson Protocol is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Decentralized Commerce, Agentic Commerce, Escrow, Tokenized Assets, and Dispute Resolution.


  Boson Protocol''s developer surface includes getting-started guide, engineering blog, documentation, and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bosonprotocol Io Domain Security
  slug: bosonprotocol-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bosonprotocol-io
tags:
- Decentralized Commerce
- Agentic Commerce
- Escrow
- Tokenized Assets
- Dispute Resolution
- Composable Finance
- Machine Commerce
website: https://bosonprotocol.io/
---
