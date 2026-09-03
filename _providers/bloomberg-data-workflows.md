---
access_model:
  confidence: high
  label: Enterprise contract
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://professional.bloomberg.com/products/data/data-license/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Batch and per-security delivery of Bloomberg's reference, pricing, regulatory and alternative data for integration into proprietary applications and workflows. The REST / hypermedia entry point is htt
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: 'The shared-server deployment of BLPAPI, providing real-time subscription and historical request/response market data to applications across a firm. SAPI is not an HTTP API: clients open a TCP session '
  name: Bloomberg SAPI (Server API)
  slug: bloomberg-server-api
artifact_total: 9
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://professional.bloomberg.com/support/api-library/
- group: docs
  title: ''
  type: APIReference
  url: https://bloomberg.github.io/blpapi-docs/
- group: operate
  title: ''
  type: Support
  url: https://professional.bloomberg.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: start
  title: ''
  type: Login
  url: https://bba.bloomberg.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/bloomberg-data-workflows-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bloomberg-data-workflows-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bloomberg-data-workflows-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-data-workflows-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomberg-data-workflows-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bloomberg-data-workflows-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloomberg-data-workflows-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloomberg-data-workflows-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bloomberg-data-workflows-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bloomberg-data-workflows-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomberg-data-workflows-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloomberg-data-workflows-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.bloomberg.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-data-workflows-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-data-workflows-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomberg-data-workflows-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/bloomberg-data-workflows-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloomberg-data-workflows-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bloomberg-data-workflows-finops.yml
created: '2024-01-01'
description: 'Bloomberg Data Workflows covers the programmatic paths institutional clients use to move Bloomberg''s financial data into their own systems: the Data License API, which delivers reference, pricing, regulatory and alternative data in bulk or per security over a JWT-authenticated REST/hypermedia endpoint at api.bloomberg.com/eap, over SFTP, or natively into the major cloud providers; and the Server API (SAPI), the shared-server deployment of BLPAPI that serves real-time subscription and historical request/response market data to applications across a firm. Both are gated behind an active Bloomberg Professional or Enterprise agreement. Bloomberg ships first-party BLPAPI SDKs for C++, Java, C# (.NET) and Python from its own distribution hosts, but publishes no OpenAPI, AsyncAPI, GraphQL schema or MCP server for either API, and keeps the API reference behind the DATA <GO> customer portal.'
finops:
- name: Bloomberg Data Workflows Finops
  service_category: API
  slug: bloomberg-data-workflows-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-data-workflows.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Data Workflows
nav: Providers
network: true
overview: 'Bloomberg Data Workflows publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Data, Financial Analytics, Financial-Services, Investment Management, and Market Data.


  Bloomberg Data Workflows'' developer surface includes developer portal, documentation, API reference, support, CLI, authentication, changelog, and 21 more developer resources.'
plans:
- name: Bloomberg Data Workflows Plans Pricing
  plan_count: 0
  slug: bloomberg-data-workflows-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Bloomberg Data Workflows Rate Limits
  slug: bloomberg-data-workflows-rate-limits
scopes:
- name: Bloomberg Data Workflows Scopes
  scope_count: 0
  slug: bloomberg-data-workflows-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 36.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-data-workflows/refs/heads/main/screenshots/bloomberg-data-workflows-2026-06-20T173412.png
security:
- kind: authentication
  name: Bloomberg Data Workflows Authentication
  slug: bloomberg-data-workflows-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Bloomberg Data Workflows Domain Security
  slug: bloomberg-data-workflows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Data Workflows Vulnerability Disclosure
  slug: bloomberg-data-workflows-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-data-workflows
tags:
- Enterprise Data
- Financial Analytics
- Financial-Services
- Investment Management
- Market Data
- Reference Data
- Trading
website: https://developer.bloomberg.com/
---
