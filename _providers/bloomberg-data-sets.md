---
access_model:
  confidence: high
  label: Contract
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://professional.bloomberg.com/products/data/data-management/data-license
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
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The Bloomberg Open API (BLPAPI) provides programmatic access to Bloomberg's market data, reference data, historical data and intraday tick data. It is an event-driven session protocol rather than an H
  name: Bloomberg Data API
  slug: bloomberg-data-api
- description: Bloomberg Data License provides bulk and per-security delivery of Bloomberg's reference, pricing, regulatory and alternative data for quantitative analysis, research and enterprise data management. De
  name: Bloomberg Data License
  slug: bloomberg-data-license
artifact_total: 9
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://professional.bloomberg.com/support/api-library/
- group: docs
  title: ''
  type: Documentation
  url: https://professional.bloomberg.com/support/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://bloomberg.github.io/blpapi-docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://professional.bloomberg.com/support/api-library/
- group: operate
  title: ''
  type: Support
  url: https://professional.bloomberg.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: company
  title: ''
  type: Blog
  url: https://www.techatbloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/bloomberg-data-sets-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bloomberg-data-sets-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bloomberg-data-sets-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-data-sets-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bloomberg-data-sets-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bloomberg-data-sets-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bloomberg-data-sets-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bloomberg-data-sets-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bloomberg-data-sets-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://assets.bbhub.io/professional/sites/27/Software-Update-and-Expiration-21en.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bloomberg-data-sets-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bloomberg-data-sets-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bloomberg-data-sets-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.bloomberg.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-data-sets-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-data-sets-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomberg-data-sets-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/bloomberg-data-sets-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bloomberg-data-sets-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bloomberg-data-sets-finops.yml
created: '2024-01-01'
description: Bloomberg L.P. delivers financial market data, reference data, pricing, regulatory and alternative data to financial professionals through two machine-facing surfaces. The Bloomberg Open API (BLPAPI) is a native session protocol with first-party SDKs in C++, Java, C# (.NET) and Python, covering real-time market data, reference data, historical data and intraday tick data across the Desktop API, Server API and B-PIPE products. Bloomberg Data License adds bulk and per-security delivery of the same content catalogue over a JWT-authenticated hypermedia REST API at api.bloomberg.com/eap, over SFTP, and natively in the major cloud providers. Bloomberg publishes no OpenAPI, AsyncAPI, GraphQL schema or MCP server; its API reference for the REST surface sits behind the Bloomberg Enterprise Console, while the BLPAPI SDK reference, downloads and version archive are fully public.
finops:
- name: Bloomberg Data Sets Finops
  service_category: API
  slug: bloomberg-data-sets-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-data-sets.png
layout: provider
modified: '2026-08-27'
name: Bloomberg Data Sets
nav: Providers
network: true
overview: 'Bloomberg Data Sets publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Datasets, Financial-Services, Market Data, and Reference Data.


  Bloomberg Data Sets'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 23 more developer resources.'
plans:
- name: Bloomberg Data Sets Plans Pricing
  plan_count: 0
  slug: bloomberg-data-sets-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Bloomberg Data Sets Rate Limits
  slug: bloomberg-data-sets-rate-limits
scopes:
- name: Bloomberg Data Sets Scopes
  scope_count: 3
  slug: bloomberg-data-sets-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-data-sets/refs/heads/main/screenshots/bloomberg-data-sets-2026-06-20T173438.png
security:
- kind: authentication
  name: Bloomberg Data Sets Authentication
  slug: bloomberg-data-sets-authentication
  summary_line: oauth2/openIdConnect/http · 3 schemes
- kind: domain-security
  name: Bloomberg Data Sets Domain Security
  slug: bloomberg-data-sets-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Data Sets Vulnerability Disclosure
  slug: bloomberg-data-sets-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-data-sets
tags:
- Analytics
- Datasets
- Financial-Services
- Market Data
- Reference Data
- Historical Data
- Financial Data
- Data Licensing
website: https://professional.bloomberg.com/support/api-library/
---
