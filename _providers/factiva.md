---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Factiva Agentic Access
  operation_count: 22
  slug: factiva-agentic-access
  summary_line: 22 operations · 4 acting
api_count: 3
apis:
- description: Provides programmatic access to create, retrieve, and manage news snapshots based on search queries and filters. Supports analytics explain jobs and time series operations for volume estimation and tr
  name: Factiva Snapshots API
  slug: factiva-snapshots-api
- description: Real-time streaming API that delivers continuous feeds of news content matching specified criteria and filters. Supports creating and managing stream subscriptions with listener methods for pushing co
  name: Factiva Streams API
  slug: factiva-streams-api
- description: 'Enables large-scale extraction of historical news articles and content based on complex queries and date ranges. After job validation, a Snapshot ID is provided along with a list of files to download '
  name: Factiva Extractions API
  slug: factiva-extractions-api
- description: Provides access to aggregated analytics, trends, and insights derived from Factiva's news and content database. Supports volume estimation, explain jobs, and time series analysis for understanding new
  name: Factiva Analytics API
  slug: factiva-analytics-api
- description: Explores the taxonomy of the Factiva databases using Dow Jones Intelligent Identifiers (DJID). Provides access to approximately 350,000 taxonomy codes covering industries, regions, news subjects, comp
  name: Factiva DJID Taxonomy API
  slug: factiva-djid-taxonomy-api
- description: Enables retrieval of codes necessary to search for companies, currencies, exchanges, locations, industries, instruments, and news subjects within Factiva. Each data item is identified by a unique Fact
  name: Factiva Code API
  slug: factiva-code-api
- description: Provides retrieval functionality that returns licensed news articles as part of trusted data sources in a retrieval-augmented generation (RAG) stack. Designed for enterprise customers building chatbot
  name: Factiva Retrieval API
  slug: factiva-retrieval-api
- description: Retrieves real-time quotes, delayed quotes, and time series market data for US, Canadian, and global companies. Supports lookups by Dow Jones Ticker, Factiva Code, CUSIP, DUNS, or ISIN to retrieve mar
  name: Factiva Market Data API
  slug: factiva-market-data-api
- baseURL: https://api.dowjones.com/factiva/snapshots/v1
  baseurl_source: declared
  description: The Content API from Factiva — 15 operation(s) for content.
  name: Factiva Content API
  slug: factiva-content-api
- baseURL: https://api.dowjones.com/factiva/snapshots/v1
  baseurl_source: declared
  description: The Content Search API from Factiva — 1 operation(s) for content search.
  name: Factiva Content Search API
  slug: factiva-content-search-api
- baseURL: https://api.dowjones.com/factiva/snapshots/v1
  baseurl_source: declared
  description: Default section
  name: Factiva Default API
  slug: factiva-default-api
- baseURL: https://api.dowjones.com/factiva/snapshots/v1
  baseurl_source: declared
  description: The Editions API from Factiva — 2 operation(s) for editions.
  name: Factiva Editions API
  slug: factiva-editions-api
- baseURL: https://api.dowjones.com/factiva/snapshots/v1
  baseurl_source: declared
  description: The Newsletters API from Factiva — 2 operation(s) for newsletters.
  name: Factiva Newsletters API
  slug: factiva-newsletters-api
artifact_total: 23
asyncapis:
- description: ''
  name: Factiva Streams Events
  slug: factiva-streams-events
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/factiva-content-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/factiva-search-and-fetch-article.md
- group: other
  title: ''
  type: Overlay
  url: overlays/factiva-newsletters-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/factiva-read-newsletter-editions.md
- group: other
  title: ''
  type: Overlay
  url: overlays/factiva-company-news-radar-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/factiva-company-news-radar.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/factiva-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: https://developer.dowjones.com/documents/factiva_integration-essentials-authentication
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dowjones/developer-platform-archived/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/factiva-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.postman.com/dj-cse/dow-jones-apis/collection/l9tpql6/factiva-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dowjones.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dowjones.com/privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://developer.dowjones.com/support
- group: company
  title: ''
  type: Website
  url: https://www.dowjones.com/business-intelligence/factiva/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/dowjones
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/dowjones
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dowjones
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dowjones/developer-platform-archived
- group: build
  title: ''
  type: SDKs
  url: packages/factiva-packages.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dow-jones
- group: other
  title: ''
  type: X
  url: https://twitter.com/DowJones
- group: start
  title: ''
  type: SignUp
  url: https://developer.dowjones.com/request-trial
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dowjones.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
- group: start
  title: ''
  type: Quickstart
  url: https://developer.dowjones.com/documents/site-docs-getting_started-quick_start-getting_credentials
- group: build
  title: ''
  type: Packages
  url: packages/factiva-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/factiva-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/factiva-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://accounts.dowjones.com/.well-known/openid-configuration
- group: design
  title: ''
  type: Conventions
  url: conventions/factiva-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/factiva-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.dowjones.com/documents/factiva_integration-essentials-deprecation_and_sunset-policy
- group: design
  title: ''
  type: Versioning
  url: https://developer.dowjones.com/documents/factiva_integration-essentials-versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/factiva-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/factiva-problem-types.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/factiva-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/factiva-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dowjones.com/iso-certification/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/factiva-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.dowjones.com/security/
- group: design
  title: ''
  type: DataModel
  url: data-model/factiva-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/factiva-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/factiva-streams-events.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/factiva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/factiva-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/factiva-finops.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/dj-cse/dow-jones-apis/documentation/l9tpql6/factiva-apis
created: '2024'
description: 'Factiva is Dow Jones'' business information and research service, providing licensed access to a global news and data archive drawn from more than 33,000 sources across 200 countries and 28 languages. Its API suite lets organizations search and retrieve licensed articles, run one-time historical extractions (Snapshots), subscribe to real-time filtered news streams over Google Cloud Pub/Sub, resolve the ~350,000-code Dow Jones Intelligent Identifiers taxonomy of companies, industries, regions and news subjects, and feed copyright-compliant content into retrieval-augmented generation stacks. Access is contract-based: there is no self-service signup and no published pricing, and credentials are issued by Dow Jones after a trial request.'
finops:
- name: Factiva Finops
  service_category: API
  slug: factiva-finops
image: https://www.dowjones.com/wp-content/uploads/sites/9/2021/03/factiva-logo.png
layout: provider
modified: '2026-08-13'
name: Factiva
nav: Providers
network: true
overview: 'Factiva publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Snapshots API, Streams API, Extractions API, and 8 more. Tagged areas include Artificial Intelligence, Business Intelligence, Content Aggregation, Enterprise Data, and GenAI.


  The Factiva catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Factiva''s developer surface includes authentication, getting-started guide, documentation, support, engineering blog, signup flow, API reference, and 44 more developer resources.'
plans:
- name: Factiva Plans Pricing
  plan_count: 0
  slug: factiva-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Factiva Rate Limits
  slug: factiva-rate-limits
scopes:
- name: Factiva Scopes
  scope_count: 8
  slug: factiva-scopes
  summary_line: 8 scopes · password/authorizationCode/implicit
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 59.5
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 86.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/factiva/refs/heads/main/screenshots/factiva-2026-06-20T181007.png
security:
- kind: authentication
  name: Factiva Authentication
  slug: factiva-authentication
  summary_line: apiKey/http/oauth2 · 2 schemes
- kind: domain-security
  name: Factiva Domain Security
  slug: factiva-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Factiva Vulnerability Disclosure
  slug: factiva-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Factiva Trust Center
  slug: factiva-trust-center
  summary_line: ISO/IEC 27001, ISAE 3000
slug: factiva
tags:
- Artificial Intelligence
- Business Intelligence
- Content Aggregation
- Enterprise Data
- GenAI
- Market Data
- Media Monitoring
- News
- News API
- Research
- Taxonomy
website: https://www.dowjones.com/business-intelligence/factiva/
---
