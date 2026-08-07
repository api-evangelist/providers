---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 64.7
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for the Copper institutional digital asset platform. Covers organizations, portfolios, wallets and balances, the crypto address book, orders (transfers, withdrawals, staking, smart calls, set
  name: Copper Platform API
  slug: copper-co-platform-api
artifact_total: 8
asyncapis:
- description: ''
  name: Copper Co Webhooks
  slug: copper-co-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://copper.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.copper.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.copper.co/guides/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.copper.co/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.copper.co/api-reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/copper-co-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://help.copper.co
- group: company
  title: ''
  type: Blog
  url: https://copper.co/en/insights/company-news
- group: commercial
  title: ''
  type: Pricing
  url: https://copper.co/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://copper.co/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://copper.co/en/privacy
- group: build
  title: ''
  type: Postman
  url: https://developer.copper.co/api-reference/try-it-out#postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/copper-co-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/copper-co-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://copper.co/en/status
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/copper-co-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/copper-co-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/copper-co-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/copper-co-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/copper-co-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/copper-co-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/copper-co-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/copper-co-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/copper-co-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/copper-co-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/copper-co-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/copper-co-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://copper.co/en/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/copper-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copper-co-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/copper-co-packages.yml
created: '2026-08-04'
description: Copper is an institutional digital asset infrastructure provider headquartered in Zug, Switzerland, offering custody, prime services and collateral management to hedge funds, trading firms, exchanges, ETP providers, foundations and miners. Its Copper Platform API is a REST API over portfolios (called "accounts" in the UI), wallets, orders, transfers, withdrawals, staking, agency and bilateral lending, and ClearLoop — Copper's off-exchange settlement and collateral network that lets clients trade on connected exchanges while assets remain in custody. The API authenticates with an API key plus a per-request HMAC-SHA256 signature, publishes OpenAPI 3.1 specifications and a Postman collection, and offers a webhook system for real-time order, deposit, withdrawal, ClearLoop and address-book events.
image: https://cdn.sanity.io/images/ih0ldmk7/production/7362d67a23ba5de367175e92536225788ede190c-2400x1181.jpg
layout: provider
mcp_servers:
- description: ''
  name: copper-co-mcp.yml
  slug: copper-co-mcpyml
modified: '2026-08-04'
name: Copper.co
nav: Providers
network: true
overview: 'Copper.co publishes 1 API on the [APIs.io](https://apis.io/) network: Copper Platform API. Tagged areas include Company, Digital Asset Custody, Cryptocurrency, Financial Services, and Institutional Finance.


  The Copper.co catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Copper.co''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 4
  name: Copper Co Rate Limits
  slug: copper-co-rate-limits
score:
  band: strong
  composite: 59.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 55.6
    developer_ergonomics: 78.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 78.9
  previous_composite: 59.4
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Copper Co Authentication
  slug: copper-co-authentication
  summary_line: apiKey/httpSignature · 2 schemes
- kind: domain-security
  name: Copper Co Domain Security
  slug: copper-co-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Copper Co Vulnerability Disclosure
  slug: copper-co-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Copper Co Trust Center
  slug: copper-co-trust-center
  summary_line: SOC 2, ISO 27001, NIST Cybersecurity Framework
slug: copper-co
tags:
- Company
- Digital Asset Custody
- Cryptocurrency
- Financial Services
- Institutional Finance
- Prime Brokerage
- Collateral Management
- Lending
- Settlement
- Staking
- Blockchain
- Treasury Management
website: https://copper.co/
---
