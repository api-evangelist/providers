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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/agentpay-shop/hosts/agentpay-shop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentpay-shop-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentpay-shop/vendors/agentpay-shop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentpay-shop-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentpay-shop/security/agentpay-shop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentpay-shop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/up2itnow0822/agentpay-mcp
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found at the provider's API host.
  evidence:
  - status: 404
    url: https://api.agentpay.shop/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: AgentPay Shop provides a non-custodial payment layer for AI agents, enabling multi-chain wallets, spending limits, and machine-to-machine transactions. Their platform supports autonomous agents to manage crypto payments securely, with patented technology and integration via the AgentPay MCP Server.
layout: provider
modified: '2026-10-30'
name: agentpay-shop
nav: Providers
network: true
overview: agentpay-shop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Crypto, AI, Non-custodial, and AgentPay.
random_paper: 0
rate_limits:
- limit_count: 1
  name: Agentpay Shop Rate Limits
  slug: agentpay-shop-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentpay Shop Authentication
  slug: agentpay-shop-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentpay Shop Domain Security
  slug: agentpay-shop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentpay-shop
tags:
- Payments
- Crypto
- AI
- Non-custodial
- AgentPay
---
