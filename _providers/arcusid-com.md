---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The ArcID indexer API provides searchable access to agent registry data.
  name: ArcID Indexer API
  slug: arcid-indexer-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/arcusid-com/hosts/arcusid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcusid-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcusid-com/vendors/arcusid-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcusid-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://arcusid.com/security
- group: auth
  href: https://artifacts.apis.io/arcusid-com/security/arcusid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcusid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcusid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://arcusid.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://arcusid.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://arcusid.com/create-agent
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcusid.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcusid.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arcusid
coverage:
  checked: '2026-11-02'
  detail: Docs are publicly accessible but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL contract was found.
  evidence:
  - status: 200
    url: https://arcusid.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ArcID provides an identity and reputation layer for AI agents on the Arc network. Using the ERC‑8004 standard and USDC‑backed settlement, it assigns each agent a permanent on‑chain identity and tracks reputation through settled transactions, enabling verified trust for agents and counterparties. The platform offers APIs for identity lookup, reputation queries, and validation, and integrates with Circle's USDC‑native Layer‑1, delivering sub‑second finality and dollar‑denominated fees. Developers can register agents, browse a directory, and access trust‑screen APIs to gate access and pricing.
image: https://arcusid.com/icon.svg?b0d258bd7e0f0d00
layout: provider
modified: '2026-11-01'
name: ArcID
nav: Providers
network: true
overview: 'ArcID is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Artificial Intelligence, Blockchain, Arc, and ERC-8004.


  ArcID''s developer surface includes documentation, getting-started guide, signup flow, and 8 more developer resources.'
plans:
- name: Arcusid Com Plans Pricing
  plan_count: 0
  slug: arcusid-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Arcusid Com Rate Limits
  slug: arcusid-com-rate-limits
scopes:
- name: Arcusid Com Scopes
  scope_count: 0
  slug: arcusid-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 20.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcusid Com Authentication
  slug: arcusid-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arcusid Com Domain Security
  slug: arcusid-com-domain-security
  summary_line: TLSv1.3
slug: arcusid-com
tags:
- Identity
- Artificial Intelligence
- Blockchain
- Arc
- ERC-8004
- USDC
website: https://arcusid.com/
---
