---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bureau Of Transportation Statistics Agentic Access
  operation_count: 22
  slug: bureau-of-transportation-statistics-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: The BTS Open Data portal powered by Socrata provides programmatic access to transportation datasets via the Socrata Open Data API (SODA). Supports filtering, querying, and aggregation across aviation,
  name: BTS Open Data SODA API
  slug: bts-open-data-soda-api
- description: TranStats is BTS's aviation and transportation statistics database providing flight on-time performance data, carrier and airport snapshots, fuel consumption data, and comprehensive airline statistics
  name: TranStats - Airline On-Time Performance Data
  slug: transtats
- description: The Freight Analysis Framework integrates data from multiple sources to create a comprehensive picture of freight flows to, from, within, and through the United States. Includes volume, value, and mod
  name: BTS Freight Analysis Framework (FAF)
  slug: bts-freight-data
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: Dataset and view metadata
  name: Bureau of Transportation Statistics Metadata API
  slug: bureau-of-transportation-statistics-metadata-api
- baseURL: https://data.bts.gov/resource/
  baseurl_source: declared
  description: Dataset resource queries via SoQL
  name: Bureau of Transportation Statistics Resource API
  slug: bureau-of-transportation-statistics-resource-api
- baseURL: https://geodata.bts.gov
  baseurl_source: declared
  description: The search and catalog API behind Geospatial at the Bureau of Transportation Statistics, the home of the National Transportation Atlas Database (NTAD). It is a conformant OGC API - Records implementat
  name: BTS Geospatial Search API (NTAD)
  slug: bts-geospatial-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BTS Open Data SODA Metadata API
  slug: open-bureau-of-transportation-statistics-metadata-api
- collection_type: open
  name: BTS Open Data SODA Metadata Resource API
  slug: open-bureau-of-transportation-statistics-resource-api
- collection_type: open
  name: BTS Open Data SODA API
  slug: open-bureau-of-transportation-statistics
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/bureau-of-transportation-statistics-geodata-search-openapi.json
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-transportation-statistics-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-transportation-statistics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bureau-of-transportation-statistics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-transportation-statistics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bureau-of-transportation-statistics-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bureau-of-transportation-statistics-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-transportation-statistics-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-transportation-statistics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-transportation-statistics-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bureau-of-transportation-statistics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-transportation-statistics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-transportation-statistics-resource-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bureau-of-transportation-statistics-metadata-api-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-transportation-statistics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.transportation.gov/vulnerability-disclosure-policy
- group: docs
  title: ''
  type: APIReference
  url: https://dev.socrata.com/docs/endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.socrata.com/consumers/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.socrata.com/
- group: start
  title: ''
  type: SignUp
  url: https://data.bts.gov/signup
- group: operate
  title: ''
  type: Support
  url: https://www.bts.gov/learn-about-bts-and-our-work/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.bts.gov/newsroom
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bureau-of-transportation-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-transportation-statistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bureau-of-transportation-statistics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotbts
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-transportation-statistics-bts
- group: company
  title: ''
  type: Website
  url: https://www.bts.gov
- group: start
  title: ''
  type: Portal
  url: https://data.bts.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transportation.gov/privacy
- group: other
  title: ''
  type: TranStats
  url: https://www.transtats.bts.gov/
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=dot-gov&q=bts
created: '2024-11-30'
description: The Bureau of Transportation Statistics (BTS), part of the Department of Transportation (DOT) is the preeminent source of statistics on commercial aviation, multimodal freight activity, and transportation economics, and provides context to decision makers and the public for understanding statistics on transportation.
finops:
- name: Bureau Of Transportation Statistics Finops
  service_category: API
  slug: bureau-of-transportation-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-transportation-statistics.png
layout: provider
modified: '2026-09-05'
name: Bureau of Transportation Statistics
nav: Providers
network: true
overview: 'Bureau of Transportation Statistics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Metadata API, Resource API, and BTS Geospatial Search API (NTAD). Tagged areas include Federal-Government, Statistics, Transportation, Aviation, and Freight.


  Bureau of Transportation Statistics'' developer surface includes changelog, API reference, getting-started guide, documentation, signup flow, support, engineering blog, and 26 more developer resources.'
plans:
- name: Bureau Of Transportation Statistics Plans Pricing
  plan_count: 0
  slug: bureau-of-transportation-statistics-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Bureau Of Transportation Statistics Rate Limits
  slug: bureau-of-transportation-statistics-rate-limits
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.5
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 47.0
    developer_ergonomics: 58.9
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-transportation-statistics/refs/heads/main/screenshots/bureau-of-transportation-statistics-2026-06-20T173820.png
security:
- kind: authentication
  name: Bureau Of Transportation Statistics Authentication
  slug: bureau-of-transportation-statistics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bureau Of Transportation Statistics Domain Security
  slug: bureau-of-transportation-statistics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Transportation Statistics Vulnerability Disclosure
  slug: bureau-of-transportation-statistics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bureau-of-transportation-statistics
tags:
- Federal-Government
- Statistics
- Transportation
- Aviation
- Freight
- Open Data
website: https://www.bts.gov
---
