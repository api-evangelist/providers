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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Creditbenchmark Agentic Access
  operation_count: 11
  slug: creditbenchmark-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 6
apis:
- description: Portfolio analytics and risk calculations
  name: Credit Benchmark Analytics API
  slug: creditbenchmark-analytics-api
- description: JWT token generation and authentication
  name: Credit Benchmark Authentication API
  slug: creditbenchmark-authentication-api
- description: Contributor-specific analytics using client/bank internal PD data. Requires ent_CLIENT-DATA entitlement.
  name: Credit Benchmark Contributor Data API
  slug: creditbenchmark-contributor-data-api
- description: Entity-specific data and rating information
  name: Credit Benchmark Entity Data API
  slug: creditbenchmark-entity-data-api
- description: Entity name matching and identification
  name: Credit Benchmark Entity Matching API
  slug: creditbenchmark-entity-matching-api
- description: Portfolio-level analytics and summaries
  name: Credit Benchmark Portfolio Analytics API
  slug: creditbenchmark-portfolio-analytics-api
artifact_total: 11
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.creditbenchmark.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.creditbenchmark.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.creditbenchmark.com/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.creditbenchmark.com/delivery-channels/getting-access
- group: operate
  title: ''
  type: Support
  url: https://www.creditbenchmark.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.creditbenchmark.com/insights/
- group: start
  title: ''
  type: Login
  url: https://analytics.creditbenchmark.com/cri/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creditbenchmark.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.creditbenchmark.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/creditbenchmark-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/creditbenchmark-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/creditbenchmark-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/creditbenchmark-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/creditbenchmark-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/creditbenchmark-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/creditbenchmark-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/creditbenchmark-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/creditbenchmark-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/creditbenchmark-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/creditbenchmark-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creditbenchmark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.creditbenchmark.com/
created: '2026-07-17'
description: Credit Benchmark is a financial data company that aggregates internal credit risk assessments contributed by more than 40 leading global financial institutions into anonymized, consensus Credit Consensus Ratings and analytics covering roughly 120,000 public and private entities — over 90% of which are unrated by the traditional credit rating agencies. Its REST API delivers consensus ratings, rating distributions, aggregate credit trends, entity rating changes, and portfolio analytics, along with entity-name-to-CBID resolution (matching) and contributor-data analytics. Delivery is also available via a web app, an Excel Add-In, and file/SFTP feeds. Access is enterprise/sales-gated; the JWT-authenticated API base is https://api.creditbenchmark.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/creditbenchmark.png
layout: provider
mcp_servers:
- description: ''
  name: creditbenchmark-mcp.yml
  slug: creditbenchmark-mcpyml
modified: '2026-07-18'
name: Credit Benchmark
nav: Providers
network: true
overview: 'Credit Benchmark publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Contributor Data API, and 3 more. Tagged areas include Company, Credit Risk, Financial Data, Credit Ratings, and Analytics.


  Credit Benchmark''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 44
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.2
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 47.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Creditbenchmark Authentication
  slug: creditbenchmark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Creditbenchmark Domain Security
  slug: creditbenchmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Creditbenchmark Trust Center
  slug: creditbenchmark-trust-center
  summary_line: trust center published
slug: creditbenchmark
tags:
- Company
- Credit Risk
- Financial Data
- Credit Ratings
- Analytics
- Risk Management
- Entity Resolution
- Consensus Data
website: http://www.creditbenchmark.com/
---
