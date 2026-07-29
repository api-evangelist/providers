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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Enigma''s primary programmatic surface: a Relay-style GraphQL API over the business knowledge graph. Query Brand, LegalEntity, OperatingLocation, Address, Person, and Industry entities via connection-b'
  name: Enigma GraphQL API
  slug: enigma-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/enigma-analytics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enigma-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enigma.com
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
  url: https://documentation.enigma.com/getting_started/enigma_data
- group: start
  title: ''
  type: SignUp
  url: https://console.enigma.com
- group: start
  title: ''
  type: Login
  url: https://console.enigma.com
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
  url: https://www.enigma.com/contact-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enigma.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enigma.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enigma.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.enigma.com/legal/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.enigma.com/legal/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enigma-analytics-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enigma-analytics-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enigma-analytics-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/enigma-analytics-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enigma-analytics-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enigma-analytics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enigma-analytics-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/enigma-analytics-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/enigma-analytics-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enigma-analytics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Enigma Analytics (Enigma Technologies) operates a knowledge graph of every U.S. business — 100M+ business registrations and 2B+ relationships spanning brands, legal entities, operating locations, addresses, and the people behind them. Enigma exposes this business identity infrastructure through a Relay-style GraphQL API, a hosted Console, and a remote MCP server, powering Know Your Business (KYB) onboarding, sanctions and watchlist screening, negative-news and government-archive checks, TIN verification, card-transaction analytics, and payment underwriting and go-to-market signals for banks, fintechs, and payments platforms.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enigma-analytics.png
layout: provider
mcp_servers:
- description: ''
  name: enigma-analytics-mcp.yml
  slug: enigma-analytics-mcpyml
modified: '2026-07-19'
name: Enigma Analytics
nav: Providers
network: true
overview: 'Enigma Analytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Data, KYB, Identity Verification, and Compliance.


  Enigma Analytics'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 21 more developer resources.'
random_paper: 58
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 38.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enigma-analytics/refs/heads/main/screenshots/enigma-analytics-2026-07-25T213359.png
security:
- kind: authentication
  name: Enigma Analytics Authentication
  slug: enigma-analytics-authentication
  summary_line: apiKey/bearer · 2 schemes
- kind: domain-security
  name: Enigma Analytics Domain Security
  slug: enigma-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enigma Analytics Vulnerability Disclosure
  slug: enigma-analytics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Enigma Analytics Trust Center
  slug: enigma-analytics-trust-center
  summary_line: SOC 2
slug: enigma-analytics
tags:
- Company
- Business Data
- KYB
- Identity Verification
- Compliance
- Sanctions Screening
- GraphQL
- Fintech
- Data Enrichment
- MCP
website: https://www.enigma.com
---
