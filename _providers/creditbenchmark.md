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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Creditbenchmark Agentic Access
  operation_count: 23
  slug: creditbenchmark-agentic-access
  summary_line: 23 operations · 17 acting
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
artifact_total: 29
collections:
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
- group: other
  href: https://artifacts.apis.io/creditbenchmark/capabilities/creditbenchmark-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/creditbenchmark-capability-edges.yml
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
  href: https://artifacts.apis.io/creditbenchmark/security/creditbenchmark-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/creditbenchmark-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/creditbenchmark/authentication/creditbenchmark-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creditbenchmark-authentication.yml
- group: design
  href: https://artifacts.apis.io/creditbenchmark/conventions/creditbenchmark-conventions.yml
  title: ''
  type: Conventions
  url: conventions/creditbenchmark-conventions.yml
- group: design
  href: https://artifacts.apis.io/creditbenchmark/errors/creditbenchmark-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/creditbenchmark-problem-types.yml
- group: design
  href: https://artifacts.apis.io/creditbenchmark/lifecycle/creditbenchmark-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/creditbenchmark-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/creditbenchmark/conformance/creditbenchmark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creditbenchmark-conformance.yml
- group: design
  href: https://artifacts.apis.io/creditbenchmark/data-model/creditbenchmark-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creditbenchmark-data-model.yml
- group: other
  href: https://artifacts.apis.io/creditbenchmark/overlays/creditbenchmark-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/creditbenchmark-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/creditbenchmark/mcp/creditbenchmark-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/creditbenchmark-mcp.yml
- group: agent
  href: https://artifacts.apis.io/creditbenchmark/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/creditbenchmark/llms/creditbenchmark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/creditbenchmark-llms.txt
- group: agent
  href: https://artifacts.apis.io/creditbenchmark/agentic-access/creditbenchmark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/creditbenchmark-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/creditbenchmark/security/creditbenchmark-domain-security.yml
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
  href: https://artifacts.apis.io/creditbenchmark/security/creditbenchmark-vulnerability-disclosure.yml
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
overview: 'Credit Benchmark publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Contributor Data API, and 6 more. Tagged areas include Company, Credit Risk, Financial Data, Credit Ratings, and Analytics.


  The Credit Benchmark catalog on APIs.io includes 1 Spectral governance ruleset.


  Credit Benchmark''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Credit Benchmark API Rules
  rule_count: 61
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 5
  slug: creditbenchmark-rules
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 57.3
    developer_ergonomics: 56.5
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 44.4
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/creditbenchmark/creditbenchmark-2026-07-25T210720.png
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
  summary_line: no policy recorded
- kind: trust-center
  name: Creditbenchmark Trust Center
  slug: creditbenchmark-trust-center
  summary_line: trust center published
skill_count: 5
skills:
- name: Authenticate and extract Credit Benchmark data
  slug: creditbenchmark-authenticate-and-get-data
- name: Resolve company names to Credit Benchmark CB_IDs
  slug: creditbenchmark-entity-resolution
- name: Run Credit Benchmark portfolio analytics
  slug: creditbenchmark-portfolio-analytics
- name: Track consensus rating moves across a universe
  slug: creditbenchmark-rating-moves
- name: Resolve entities and pull consensus credit analytics
  slug: creditbenchmark-resolve-and-analyze
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
