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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Credit Benchmark Agentic Access
  operation_count: 12
  slug: credit-benchmark-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 5
apis:
- description: Analytics endpoints.
  name: Credit Benchmark analytics API
  slug: credit-benchmark-analytics-api
- description: Token generation endpoints.
  name: Credit Benchmark authentication API
  slug: credit-benchmark-authentication-api
- description: Raw data extraction endpoints.
  name: Credit Benchmark data API
  slug: credit-benchmark-data-api
- description: Entity name resolution endpoints.
  name: Credit Benchmark entity-resolution API
  slug: credit-benchmark-entity-resolution-api
- description: Metadata discovery endpoints.
  name: Credit Benchmark metadata API
  slug: credit-benchmark-metadata-api
artifact_total: 11
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.creditbenchmark.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.creditbenchmark.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.creditbenchmark.com/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.creditbenchmark.com/delivery-channels/getting-access
- group: start
  title: ''
  type: Login
  url: https://cbcbeta.creditbenchmark.com/
- group: company
  title: ''
  type: Blog
  url: https://www.creditbenchmark.com/research/
- group: operate
  title: ''
  type: Support
  url: https://www.creditbenchmark.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creditbenchmark.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creditbenchmark.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.creditbenchmark.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.creditbenchmark.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/credit-benchmark-consensus-data-openapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credit-benchmark-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/credit-benchmark-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/credit-benchmark-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/credit-benchmark-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/credit-benchmark-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/credit-benchmark-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/credit-benchmark-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/credit-benchmark-consensus-data-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/credit-benchmark-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/credit-benchmark-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/credit-benchmark-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/credit-benchmark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.creditbenchmark.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credit-benchmark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.creditbenchmark.com
created: '2026-07-17'
description: Credit Benchmark is a financial data company that aggregates confidential credit-risk estimates from over 40 leading global financial institutions into anonymized consensus Credit Consensus Ratings (CCRs) and analytics covering 120,000+ public and private entities, most of which are unrated by traditional agencies. Risk professionals across banking, insurance, and asset management use the data for customer onboarding and credit decisioning, portfolio monitoring, model calibration, market valuation, and regulatory and third-party risk validation. Delivery channels include a REST API (gateway.creditbenchmark.com), a web application, an Excel Add-In, SFTP/secure file transfer, and data marketplaces (Snowflake, Databricks, AWS Data Exchange). The Consensus Data API exposes JWT-authenticated entity resolution, raw data extraction, computed analytics (trends, breakdowns, rating changes, distributions), and metadata discovery. Backed by Index Ventures.
image: https://www.creditbenchmark.com/wp-content/uploads/2025/06/CB-Logo-for-News-Page-scaled.png
layout: provider
mcp_servers:
- description: ''
  name: credit-benchmark-mcp.yml
  slug: credit-benchmark-mcpyml
modified: '2026-07-18'
name: Credit Benchmark
nav: Providers
network: true
overview: 'Credit Benchmark publishes 5 APIs on the [APIs.io](https://apis.io/) network, including analytics API, authentication API, data API, and 2 more. Tagged areas include Company, Fintech, Credit Risk, Credit Ratings, and Financial Data.


  Credit Benchmark''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 22 more developer resources.'
random_paper: 39
score:
  band: developing
  composite: 48.9
  delta: -2.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 65.3
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/credit-benchmark/refs/heads/main/screenshots/credit-benchmark-2026-07-25T210718.png
security:
- kind: authentication
  name: Credit Benchmark Authentication
  slug: credit-benchmark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Credit Benchmark Domain Security
  slug: credit-benchmark-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Credit Benchmark Vulnerability Disclosure
  slug: credit-benchmark-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Credit Benchmark Trust Center
  slug: credit-benchmark-trust-center
  summary_line: trust center published
slug: credit-benchmark
tags:
- Company
- Fintech
- Credit Risk
- Credit Ratings
- Financial Data
- Analytics
- Data
- API
website: https://www.creditbenchmark.com
---
