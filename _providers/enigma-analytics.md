---
access_model:
  confidence: high
  label: Self-serve signup with published list pricing
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://www.enigma.com/pricing
  - plans/enigma-analytics-plans-pricing.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.2
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: 'Enigma''s primary programmatic surface: a Relay-style GraphQL API over the business knowledge graph. Query Brand, LegalEntity, OperatingLocation, Address, Person, and Industry entities via connection-b'
  name: Enigma GraphQL API
  slug: enigma-graphql-api
- description: REST endpoint for Know Your Business verification. POST a business name, address, website, TIN and/or person and receive identity matching and compliance validation. The `identify` package returns bas
  name: Enigma KYB REST API
  slug: enigma-kyb-rest-api
- description: REST endpoint for screening persons and organizations against sanctions, PEP and watchlist databases. Accepts a batch of ENTITY searches carrying person_name and/or org_name descriptions and returns m
  name: Enigma Screen API
  slug: enigma-screen-api
- description: Remote Model Context Protocol server for U.S. business intelligence — entity resolution, KYB verification, sanctions and negative-news screening, card-transaction analytics and public-records search —
  name: Enigma MCP Server
  slug: enigma-mcp-server
artifact_total: 12
common:
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
- group: commercial
  title: ''
  type: Plans
  url: plans/enigma-analytics-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.enigma.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.enigma.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/enigma-io
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
- group: auth
  title: ''
  type: TrustCenter
  url: security/enigma-analytics-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enigma-analytics-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enigma-analytics-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enigma-analytics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/enigma-analytics-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enigma-analytics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/enigma-analytics-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/enigma-analytics-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/enigma-analytics-security.txt
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
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/enigma-analytics-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enigma-analytics-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/enigma-analytics-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/enigma-analytics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enigma-analytics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Enigma Analytics (Enigma Technologies) operates a knowledge graph of every U.S. business — 100M+ business registrations and 2B+ relationships spanning brands, legal entities, operating locations, addresses, and the people behind them, enriched with 750M+ anonymized cards and 30B+ annual card transactions. Enigma exposes this business identity infrastructure through three developer surfaces — a Relay-style GraphQL API, a KYB REST API, and a sanctions Screen API — plus a hosted Console and an OAuth 2.1 remote MCP server, powering Know Your Business (KYB) onboarding, sanctions and watchlist screening, negative-news and government-archive checks, TIN and SSN verification, card-transaction analytics, and payment underwriting and go-to-market signals for banks, fintechs, and payments platforms. Pricing is published and self-serve, metered in credits at one cent each.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enigma-analytics.png
layout: provider
mcp_servers:
- description: 'Remote MCP server for U.S. business intelligence: entity resolution, KYB verification, sanctions and negative-news screening, card-transaction analytics, and public-records search.'
  name: Enigma Analytics MCP Server
  slug: enigma-analytics-mcp-server
modified: '2026-08-14'
name: Enigma Analytics
nav: Providers
network: true
overview: 'Enigma Analytics publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Data, KYB, Identity Verification, and Compliance.


  Enigma Analytics'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, support, and 29 more developer resources.'
plans:
- name: Enigma Analytics Plans Pricing
  plan_count: 4
  slug: enigma-analytics-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 12
  name: Enigma Analytics Rate Limits
  slug: enigma-analytics-rate-limits
scopes:
- name: Enigma Analytics Scopes
  scope_count: 0
  slug: enigma-analytics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 48.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enigma-analytics/refs/heads/main/screenshots/enigma-analytics-2026-07-25T213359.png
security:
- kind: authentication
  name: Enigma Analytics Authentication
  slug: enigma-analytics-authentication
  summary_line: apiKey/oauth2/http · 4 schemes
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
- Agent Skills
- Payments Risk
website: https://www.enigma.com
---
