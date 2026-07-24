---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Confirming (reverse factoring) invoices and payment instructions.
  name: Novicap Confirming Standard API
  slug: novicap-confirming-standard-api
- description: Dynamic discounting suppliers, invoices, payment instructions and adjustments.
  name: Novicap Dynamic Discounting API
  slug: novicap-dynamic-discounting-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://novicap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.novicap.com/
- group: company
  title: ''
  type: Blog
  url: https://novicap.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.novicap.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: mailto:support@novicap.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novicap.com/aviso-legal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/novicap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/novicap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/novicap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/novicap-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/novicap-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/novicap-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/novicap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novicap-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/novicap-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/novicap-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/novicap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://novicap.com/.well-known/security.txt
created: '2026-07-17'
description: 'Novicap is a Spanish working-capital and supply-chain-finance fintech that helps companies optimize their circulating capital. Its REST API (base URL https://api.novicap.com/v1) lets partners programmatically register suppliers, submit and manage invoices, and create payment instructions and adjustments across two products: Dynamic Discounting and Confirming Standard (reverse factoring). The API uses Bearer API-key authentication with a required product_id scope, JSON payloads, and URI-path versioning, and is documented in a public developer reference. Novicap is backed by Partech and Techstars.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novicap.png
layout: provider
mcp_servers:
- description: ''
  name: novicap-mcp.yml
  slug: novicap-mcpyml
modified: '2026-07-20'
name: Novicap
nav: Providers
network: true
overview: 'Novicap publishes 2 APIs on the [APIs.io](https://apis.io/) network: Confirming Standard API and Dynamic Discounting API. Tagged areas include Company, Financial Services, Fintech, Working Capital, and Invoice Finance.


  Novicap''s developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 53.1
    developer_ergonomics: 41.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Novicap Authentication
  slug: novicap-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: vulnerability-disclosure
  name: Novicap Vulnerability Disclosure
  slug: novicap-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: novicap
tags:
- Company
- Financial Services
- Fintech
- Working Capital
- Invoice Finance
- Supply Chain Finance
- Dynamic Discounting
- Confirming
- Reverse Factoring
- Spain
website: https://novicap.com/
---
