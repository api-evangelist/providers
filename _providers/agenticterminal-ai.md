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
- description: Public API providing tools to search merchants, retrieve merchant details, verify payment endpoints, and query rate limits.
  name: Agentic Terminal API
  slug: agentic-terminal-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/agenticterminal-ai/hosts/agenticterminal-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticterminal-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticterminal-ai/vendors/agenticterminal-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticterminal-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agenticterminal-ai/security/agenticterminal-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticterminal-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticterminal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agenticterminal.ai/about/
- group: docs
  title: ''
  type: APIReference
  url: https://agenticterminal.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticterminal.ai/how-it-works
- group: start
  title: ''
  type: SignUp
  url: https://agenticterminal.ai/submit
coverage:
  checked: '2026-11-01'
  detail: API reference page is HTML without any published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec.
  evidence:
  - status: 301
    url: https://agenticterminal.ai/api-docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agentic Terminal is a decentralized marketplace that connects task posters with independent agents who fulfill work using the Observer Protocol. Users can post tasks, list their services, and browse a supply of merchants, with verifiable identities anchored by DIDs. The platform supports multi‑rail payments including Lightning, USDT, BOLT12 and L402, enabling non‑custodial, direct settlement between parties. All API endpoints are publicly accessible without authentication, providing tools to search merchants, retrieve merchant details, verify payment endpoints, and query rate limits. The service emphasizes trust through OP credentials and transparent credentialing, allowing agents and merchants to be ranked by verification tiers.
image: https://agenticterminal.ai/how-it-works/directory.png
layout: provider
modified: '2026-11-01'
name: Agentic Terminal
nav: Providers
network: true
overview: 'Agentic Terminal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Decentralized, Payments, ObserverProtocol, and Agents.


  Agentic Terminal''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 4 more developer resources.'
plans:
- name: Agenticterminal Ai Plans Pricing
  plan_count: 0
  slug: agenticterminal-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Agenticterminal Ai Rate Limits
  slug: agenticterminal-ai-rate-limits
scopes:
- name: Agenticterminal Ai Scopes
  scope_count: 0
  slug: agenticterminal-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 13.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticterminal Ai Authentication
  slug: agenticterminal-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenticterminal Ai Domain Security
  slug: agenticterminal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenticterminal-ai
tags:
- Marketplace
- Decentralized
- Payments
- ObserverProtocol
- Agents
website: https://agenticterminal.ai/
---
