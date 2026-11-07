---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Morning Consult Agentic Access
  operation_count: 26
  slug: morning-consult-agentic-access
  summary_line: 26 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.morningconsult.com/v1
  baseurl_source: declared
  description: Morning Consult's AI backed by survey data responses.
  name: Morning Consult AI API
  slug: morning-consult-ai-api
- baseURL: https://api.morningconsult.com/v1
  baseurl_source: declared
  description: Authentication related operations.
  name: Morning Consult Authentication API
  slug: morning-consult-authentication-api
- baseURL: https://api.morningconsult.com/v1
  baseurl_source: declared
  description: Syndicated tracking survey data data responses.
  name: Morning Consult Data API
  slug: morning-consult-data-api
- baseURL: https://api.morningconsult.com/v1
  baseurl_source: declared
  description: Metadata information related to syndicated surveys.
  name: Morning Consult Lookup API
  slug: morning-consult-lookup-api
arazzos:
- description: Authenticate, resolve a data source and country, find the brand entity and the question that measures it, then pull the aggregated response timeseries.
  name: Morning Consult — brand trendline
  slug: morning-consult-brand-trendline
- description: Authenticate, resolve the data source and questions, submit an asynchronous bulk responses request, then poll it to completion for the Parquet result.
  name: Morning Consult — bulk Data Bridge load
  slug: morning-consult-bulk-data-bridge
- description: Authenticate, discover an available score and the data sources it is available in, bind it to a brand entity, and request the score timeseries.
  name: Morning Consult — compute a score
  slug: morning-consult-compute-score
artifact_total: 21
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://morningconsult.com/articles/rss.xml
- group: other
  href: https://artifacts.apis.io/morning-consult/capabilities/morning-consult-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/morning-consult-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/morning-consult/overlays/morning-consult-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/morning-consult-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/morning-consult/mcp/morning-consult-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/morning-consult-mcp.yml
- group: auth
  href: https://artifacts.apis.io/morning-consult/security/morning-consult-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/morning-consult-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/morning-consult/security/morning-consult-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/morning-consult-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/morning-consult/security/morning-consult-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/morning-consult-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://morningconsult.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.morningconsult.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.morningconsult.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.morningconsult.com/docs/#reference
- group: start
  title: ''
  type: GettingStarted
  url: https://api.morningconsult.com/docs/#introduction
- group: auth
  href: https://artifacts.apis.io/morning-consult/authentication/morning-consult-authentication.yml
  title: ''
  type: Authentication
  url: authentication/morning-consult-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://morningconsult.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://morningconsult.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morningconsult
- group: start
  title: ''
  type: SignUp
  url: https://morningconsult.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://intel.morningconsult.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://morningconsult.com/mci-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://morningconsult.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://morningconsult.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://morningconsult.com/security
- group: agent
  href: https://artifacts.apis.io/morning-consult/llms/morning-consult-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/morning-consult-llms.txt
- group: build
  href: https://artifacts.apis.io/morning-consult/packages/morning-consult-packages.yml
  title: ''
  type: Packages
  url: packages/morning-consult-packages.yml
- group: build
  href: https://artifacts.apis.io/morning-consult/examples/morning-consult-examples.yml
  title: ''
  type: Examples
  url: examples/morning-consult-examples.yml
- group: operate
  href: https://artifacts.apis.io/morning-consult/rate-limits/morning-consult-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/morning-consult-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/morning-consult/errors/morning-consult-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/morning-consult-problem-types.yml
- group: design
  href: https://artifacts.apis.io/morning-consult/data-model/morning-consult-data-model.yml
  title: ''
  type: DataModel
  url: data-model/morning-consult-data-model.yml
- group: design
  href: https://artifacts.apis.io/morning-consult/conventions/morning-consult-conventions.yml
  title: ''
  type: Conventions
  url: conventions/morning-consult-conventions.yml
- group: design
  href: https://artifacts.apis.io/morning-consult/lifecycle/morning-consult-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/morning-consult-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://api.morningconsult.com/docs/#migration-guide
- group: design
  href: https://artifacts.apis.io/morning-consult/conformance/morning-consult-conformance.yml
  title: ''
  type: Conformance
  url: conformance/morning-consult-conformance.yml
- group: agent
  href: https://artifacts.apis.io/morning-consult/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/morning-consult/arazzo/_index.yml
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
- group: agent
  href: https://artifacts.apis.io/morning-consult/agentic-access/morning-consult-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/morning-consult-agentic-access.yml
created: '2026-08-01'
description: Morning Consult is a decision intelligence company that fields more than 30,000 online surveys every day across 45+ countries, turning continuous consumer interviewing into brand, reputation, economic and category tracking data. Its flagship product, Morning Consult Intelligence (MCI), exposes that data programmatically through the Morning Consult API — a versioned REST API at api.morningconsult.com/v1 that serves metadata lookup (data sources, countries, categories, entities, questions, scores), on-demand aggregated survey responses and scores with custom audience filtering and calendar-interval aggregation, asynchronous bulk/Data Bridge requests that return Parquet files for Snowflake, BigQuery and Databricks, and an AI resolve endpoint that answers natural-language questions against the syndicated survey corpus.
image: https://morningconsult.com/hubfs/MorningConsult_FeaturedImage.png
json_schemas:
- name: Morning Consult API schemas
  property_count: 0
  slug: morning-consult-schemas
layout: provider
modified: '2026-10-06'
name: Morning Consult
nav: Providers
network: true
overview: 'Morning Consult publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Authentication API, Data API, and 1 more. Tagged areas include Company, Market Research, Survey Data, Consumer Intelligence, and Brand Tracking.


  The Morning Consult catalog on APIs.io includes 1 Spectral governance ruleset.


  Morning Consult''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 28 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 5
  name: Morning Consult Rate Limits
  slug: morning-consult-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Morning Consult API Rules
  rule_count: 57
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 5
  slug: morning-consult-rules
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 58.9
    catalog_earned_first_party: 12.0
    catalog_gap: 56.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 61.4
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/morning-consult/morning-consult-2026-08-07T184308.png
security:
- kind: authentication
  name: Morning Consult Authentication
  slug: morning-consult-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Morning Consult Domain Security
  slug: morning-consult-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Morning Consult Vulnerability Disclosure
  slug: morning-consult-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Morning Consult Trust Center
  slug: morning-consult-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA, ISO 27001, ISO 27017
skill_count: 6
skills:
- name: Ask Morning Consult a natural-language question
  slug: morning-consult-ai-resolve
- name: Authenticate to the Morning Consult API
  slug: morning-consult-authenticate
- name: Pull a brand trendline from Morning Consult
  slug: morning-consult-brand-trendline
- name: Load Morning Consult data in bulk via Data Bridge
  slug: morning-consult-bulk-data-bridge
- name: Compute a Morning Consult score
  slug: morning-consult-compute-score
- name: Build a custom audience for a Morning Consult data request
  slug: morning-consult-custom-audience
slug: morning-consult
tags:
- Company
- Market Research
- Survey Data
- Consumer Intelligence
- Brand Tracking
- Decision Intelligence
- Public Opinion
- Analytics
- Data
- Artificial Intelligence
website: https://morningconsult.com/
---
