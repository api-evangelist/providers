---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Creditbenchmark Agentic Access
  operation_count: 11
  slug: creditbenchmark-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 2
apis:
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Portfolio analytics and risk calculations
  name: Credit Benchmark Analytics API
  slug: creditbenchmark-analytics-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: JWT token generation and authentication
  name: Credit Benchmark Authentication API
  slug: creditbenchmark-authentication-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Contributor-specific analytics using client/bank internal PD data. Requires ent_CLIENT-DATA entitlement.
  name: Credit Benchmark Contributor Data API
  slug: creditbenchmark-contributor-data-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Entity-specific data and rating information
  name: Credit Benchmark Entity Data API
  slug: creditbenchmark-entity-data-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Entity name matching and identification
  name: Credit Benchmark Entity Matching API
  slug: creditbenchmark-entity-matching-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Portfolio-level analytics and summaries
  name: Credit Benchmark Portfolio Analytics API
  slug: creditbenchmark-portfolio-analytics-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Raw data extraction endpoints.
  name: Credit Benchmark Data API
  slug: creditbenchmark-data-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Entity name resolution endpoints.
  name: Credit Benchmark Entity Resolution API
  slug: creditbenchmark-entity-resolution-api
- baseURL: https://api.creditbenchmark.com
  baseurl_source: declared
  description: Metadata discovery endpoints.
  name: Credit Benchmark Metadata API
  slug: creditbenchmark-metadata-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Credit Benchmark Analytics API
  slug: open-creditbenchmark-analytics-api
- collection_type: open
  name: Credit Benchmark Analytics Authentication API
  slug: open-creditbenchmark-authentication-api
- collection_type: open
  name: Credit Benchmark Analytics Contributor Data API
  slug: open-creditbenchmark-contributor-data-api
- collection_type: open
  name: Credit Benchmark analytics data API
  slug: open-creditbenchmark-data-api
- collection_type: open
  name: Credit Benchmark Analytics Entity Data API
  slug: open-creditbenchmark-entity-data-api
- collection_type: open
  name: Credit Benchmark Analytics Entity Matching API
  slug: open-creditbenchmark-entity-matching-api
- collection_type: open
  name: Credit Benchmark analytics entity-resolution API
  slug: open-creditbenchmark-entity-resolution-api
- collection_type: open
  name: Credit Benchmark analytics metadata API
  slug: open-creditbenchmark-metadata-api
- collection_type: open
  name: Credit Benchmark Analytics Portfolio Analytics API
  slug: open-creditbenchmark-portfolio-analytics-api
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
  type: X-MCPServerCandidate
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
- group: operate
  title: ''
  type: StatusPage
  url: https://status.creditbenchmark.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/creditbenchmark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.creditbenchmark.com/vulnerability-disclosure/
created: '2026-07-17'
description: Credit Benchmark is a financial data company that aggregates internal credit risk assessments contributed by more than 40 leading global financial institutions into anonymized, consensus Credit Consensus Ratings and analytics covering roughly 120,000 public and private entities — over 90% of which are unrated by the traditional credit rating agencies. Its REST API delivers consensus ratings, rating distributions, aggregate credit trends, entity rating changes, and portfolio analytics, along with entity-name-to-CBID resolution (matching) and contributor-data analytics. Delivery is also available via a web app, an Excel Add-In, and file/SFTP feeds. Access is enterprise/sales-gated; the JWT-authenticated API base is https://api.creditbenchmark.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/creditbenchmark.png
layout: provider
modified: '2026-08-08'
name: Credit Benchmark
nav: Providers
network: true
overview: 'Credit Benchmark publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Contributor Data API, and 6 more. Tagged areas include Company, Credit Risk, Financial Data, Credit Ratings, and Analytics.


  Credit Benchmark''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creditbenchmark/refs/heads/main/screenshots/creditbenchmark-2026-07-25T210720.png
security:
- kind: authentication
  name: Creditbenchmark Authentication
  slug: creditbenchmark-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Creditbenchmark Domain Security
  slug: creditbenchmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Creditbenchmark Vulnerability Disclosure
  slug: creditbenchmark-vulnerability-disclosure
  summary_line: disclosure policy published
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
