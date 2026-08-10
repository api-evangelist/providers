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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-10'
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
random_paper: 56
score:
  band: emerging
  composite: 25.8
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 14.7
    developer_ergonomics: 29.9
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 10.5
  previous_composite: 25.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novicap/refs/heads/main/screenshots/novicap-2026-08-07T185613.png
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
