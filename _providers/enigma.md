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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: GraphQL API for querying Enigma business data — brands, operating locations, legal entities, card transactions, and industries — with text, lookup, natural-language prompt, and async segmentation sear
  name: Enigma GraphQL Data API
  slug: enigma-graphql-data-api
- description: REST API for business identity verification and compliance — identify and verify packages with TIN/EIN verification, OFAC watchlist screening, and SSN verification add-on tasks.
  name: Enigma KYB REST API
  slug: enigma-kyb-rest-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.enigma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.enigma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.enigma.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.enigma.com/reference/graphql_api/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.enigma.com/getting_started/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.enigma.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.enigma.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.enigma.com/company/support
- group: start
  title: ''
  type: SignUp
  url: https://console.enigma.com/
- group: start
  title: ''
  type: Login
  url: https://console.enigma.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enigma.com/company/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enigma.com/legal/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enigma.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.enigma.com/legal/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enigma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enigma-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enigma-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/enigma-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/enigma-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enigma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.enigma.com/legal/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enigma-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enigma-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enigma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enigma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enigma-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enigma-data-model.yml
created: '2026-07-17'
description: Enigma provides business identity infrastructure for the United States, built on entity-resolution technology that links brands, DBAs, operating locations, legal entities, and ownership into unified business records. Its Identity Graph aggregates hundreds of public and third-party sources plus 750M+ anonymized cards and 30B+ annual transactions, powering KYB and onboarding, sanctions and negative-news screening, payment risk and underwriting, and go-to-market data. Developers access this through a GraphQL Data API, a KYB REST API, and a remote MCP server.
image: https://www.enigma.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: enigma-mcp.yml
  slug: enigma-mcpyml
modified: '2026-07-19'
name: Enigma
nav: Providers
network: true
overview: 'Enigma publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Data, Identity Resolution, KYB, and Compliance.


  Enigma''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 20 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 36.3
  delta: 0.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 35.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enigma/refs/heads/main/screenshots/enigma-2026-07-25T213358.png
security:
- kind: authentication
  name: Enigma Authentication
  slug: enigma-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Enigma Domain Security
  slug: enigma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enigma Vulnerability Disclosure
  slug: enigma-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: enigma
tags:
- Company
- Business Data
- Identity Resolution
- KYB
- Compliance
- Fraud
- GraphQL
- Data Enrichment
- Financial Services
- MCP
website: https://www.enigma.com/
---
