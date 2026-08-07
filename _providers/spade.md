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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Spade Agentic Access
  operation_count: 73
  slug: spade-agentic-access
  summary_line: 73 operations · 51 acting
api_count: 8
apis:
- description: Enrich card transactions
  name: Spade Card Enrichment API
  slug: spade-card-enrichment-api
- description: Register category action triggers and receive triggered actions in enrichment responses
  name: Spade Category Action Triggers API
  slug: spade-category-action-triggers-api
- description: Create custom categories and personalize enrichments
  name: Spade Category Personalization API
  slug: spade-category-personalization-api
- description: Provide feedback on card events or report enrichment errors
  name: Spade Feedback and Reporting API
  slug: spade-feedback-and-reporting-api
- description: Register merchant action triggers and receive triggered actions in enrichment responses
  name: Spade Merchant Action Triggers API
  slug: spade-merchant-action-triggers-api
- description: Search for Spade merchants
  name: Spade Merchant Search API
  slug: spade-merchant-search-api
- description: Enrich transfers
  name: Spade Transfer Enrichment API
  slug: spade-transfer-enrichment-api
- description: The Universal Enrichment API from Spade — 3 operation(s) for universal enrichment.
  name: Spade Universal Enrichment API
  slug: spade-universal-enrichment-api
artifact_total: 15
asyncapis:
- description: ''
  name: Spade Webhooks
  slug: spade-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spade.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spade.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spade.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spade.com/reference/integrate-with-spades-api
- group: operate
  title: ''
  type: Support
  url: https://www.spade.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spade.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spade.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spade.com/privacy
- group: operate
  title: ''
  type: SLA
  url: https://www.spade.com/sla
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.spade.com/changelog/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spade-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spade-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spade-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spade-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spade-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spade-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spade-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spade-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spade-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spade-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spade-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spade-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.spade.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/spade-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spade-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.spade.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spade-domain-security.yml
created: '2026-07-17'
description: Spade is a real-time transaction enrichment and merchant intelligence platform for financial services. Its API transforms raw, messy card, transfer, and universal transaction records into clean, structured, verified merchant, location, and category data with sub-50ms latency. Fintechs, banks, and card issuers use Spade for authorization decisions, rewards attribution, recurring-payment detection, risk and fraud signals, spend analytics, and category personalization, plus merchant search and account/program/user/card-scoped action triggers. Spade operates east and west US sandbox and production environments and is SOC 2 Type II certified.
image: https://spadewp.wpenginepowered.com/wp-content/uploads/2025/07/OpenGraph.webp
layout: provider
mcp_servers:
- description: ''
  name: spade-mcp.yml
  slug: spade-mcpyml
modified: '2026-07-21'
name: Spade
nav: Providers
network: true
overview: 'Spade publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Card Enrichment API, Category Action Triggers API, Category Personalization API, and 5 more. Tagged areas include Company, Financial Services, Transaction Enrichment, Merchant Intelligence, and Payments.


  The Spade catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spade''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, authentication, and 21 more developer resources.'
random_paper: 73
score:
  band: developing
  composite: 55.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 72.5
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 34.2
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Spade Authentication
  slug: spade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spade Domain Security
  slug: spade-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Spade Vulnerability Disclosure
  slug: spade-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Spade Trust Center
  slug: spade-trust-center
  summary_line: SOC 2 Type II
slug: spade
tags:
- Company
- Financial Services
- Transaction Enrichment
- Merchant Intelligence
- Payments
- Data Enrichment
- Fraud and Risk
- Fintech
website: https://docs.spade.com
---
