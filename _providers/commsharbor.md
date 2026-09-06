---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST/HTTP API (OpenAPI 3.1) for transactional email, deliverability, sending domains, permission-based marketing, CRM, and multi-tenancy governance across 96 paths. Cross-linked with a hosted MCP serv
  name: CommsHarbor API
  slug: commsharbor-api
artifact_total: 9
asyncapis:
- description: ''
  name: Commsharbor Webhooks
  slug: commsharbor-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://commsharbor.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/commsharbor-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/commsharbor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commsharbor-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: security/commsharbor-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/commsharbor-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/commsharbor-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/commsharbor-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/commsharbor-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/commsharbor-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/commsharbor-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/commsharbor-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commsharbor.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commsharbor.com/privacy
- group: start
  title: ''
  type: Login
  url: https://commsharbor.com/app
created: '2026-09-05'
description: Transactional email and permission-based marketing infrastructure with tenant isolation, deliverability tracking, CRM, and multi-tenant governance. Self-describes as an agent-first HTTP API with a hosted MCP server.
image: https://commsharbor.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: CommsHarbor MCP Server
  slug: commsharbor-mcp-server
- description: Official hosted MCP server for CommsHarbor transactional email, permission-based marketing, CRM, and multi-tenant governance. Streamable HTTP transport, JSON-RPC 2.0, protocol version 2024-11-05. An a
  name: CommsHarbor MCP Server
  slug: commsharbor-mcp-server-2
modified: '2026-09-05'
name: CommsHarbor
nav: Providers
network: true
overview: 'CommsHarbor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Transactional Email, Email Marketing, Communications, and Messaging.


  The CommsHarbor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CommsHarbor''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Commsharbor Plans Pricing
  plan_count: 3
  slug: commsharbor-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Commsharbor Rate Limits
  slug: commsharbor-rate-limits
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 45.5
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Commsharbor Authentication
  slug: commsharbor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Commsharbor Domain Security
  slug: commsharbor-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Commsharbor Vulnerability Disclosure
  slug: commsharbor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: commsharbor
tags:
- Email
- Transactional Email
- Email Marketing
- Communications
- Messaging
- Deliverability
- CRM
- Multi-tenant SaaS
- Agent-native
- MCP
- Web3 payments
- x402
website: https://commsharbor.com
---
