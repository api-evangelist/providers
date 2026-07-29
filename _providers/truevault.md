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
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: TrueVault Safe is a REST API and secure datastore for sensitive personal data. Resources include Users, Groups (with policy-based Access Grid permissions), Vaults, BLOBs, Documents, Schemas, Search (f
  name: TrueVault Safe REST API
  slug: truevault-safe-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.truevault.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truevault.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.truevault.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.truevault.com/Overview.html
- group: operate
  title: ''
  type: Support
  url: https://www.truevault.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.truevault.com/learn
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truevault
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truevault.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.truevault.com/register
- group: start
  title: ''
  type: Login
  url: https://console.truevault.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truevault.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.truevault.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.truevault.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/truevault-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/truevault-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truevault-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truevault-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truevault-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truevault-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/truevault-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truevault-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truevault-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truevault-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truevault-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truevault-domain-security.yml
created: '2026-07-17'
description: TrueVault provides developer infrastructure for storing and managing sensitive personal data in a compliant way. Its original product, TrueVault Safe, is a HIPAA-oriented REST API and secure datastore that lets applications create Vaults and store encrypted Documents, BLOBs, Users, and Schemas, with group-based access control (the Access Grid), full-text and geospatial Search, transactional Email/SMS messaging, password-reset flows, and scoped access tokens. Authentication is via API keys or user access tokens passed in an HTTP Basic header. TrueVault's newer Polaris product is privacy-compliance software that helps ecommerce brands comply with US state privacy laws, the GDPR, and the CCPA. TrueVault is a Y Combinator-backed company.
image: https://github.com/truevault.png
layout: provider
mcp_servers:
- description: ''
  name: TrueVault MCP Server manifest (candidate)
  slug: truevault-mcp-server-manifest-candidate
modified: '2026-07-21'
name: TrueVault
nav: Providers
network: true
overview: 'TrueVault publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Privacy, Security, Compliance, and HIPAA.


  TrueVault''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 32
score:
  band: thin
  composite: 35.0
  delta: -1.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 36.5
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Truevault Authentication
  slug: truevault-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Truevault Domain Security
  slug: truevault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truevault
tags:
- Company
- Data Privacy
- Security
- Compliance
- HIPAA
- Data Storage
- Encryption
- Identity
- Privacy
- PII
website: https://console.truevault.com/
---
