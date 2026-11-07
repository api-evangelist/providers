---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Import Io Agentic Access
  operation_count: 22
  slug: import-io-agentic-access
  summary_line: 22 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.import.io
  baseurl_source: declared
  description: The schedule.import.io API from Import.io — 2 operation(s) for schedule.import.io.
  name: Import.io Schedule.import.io API
  slug: import-io-schedule-import-io-api
artifact_total: 16
collections:
- collection_type: open
  name: Import.io Crawlrun API
  slug: open-import-io-crawlrun-api
- collection_type: open
  name: Import.io Crawlrun Extractor API
  slug: open-import-io-extractor-api
- collection_type: open
  name: Import.io Crawlrun Report API
  slug: open-import-io-report-api
- collection_type: open
  name: Import.io Crawlrun ReportRun API
  slug: open-import-io-reportrun-api
- collection_type: open
  name: Import.io Crawlrun User API
  slug: open-import-io-user-api
- collection_type: open
  name: Import.io API
  slug: open-import-io
common:
- group: commercial
  href: https://artifacts.apis.io/import-io/plans/import-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/import-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/import-io/rate-limits/import-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/import-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/import-io/finops/import-io-finops.yml
  title: ''
  type: FinOps
  url: finops/import-io-finops.yml
- group: agent
  href: https://artifacts.apis.io/import-io/agentic-access/import-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/import-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/import-io/security/import-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/import-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/import-io/authentication/import-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/import-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/import-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/import-io
- group: company
  title: ''
  type: Website
  url: https://www.import.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.import.io
- group: other
  title: ''
  type: Products
  url: https://www.import.io/products
- group: commercial
  title: ''
  type: Pricing
  url: https://www.import.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.import.io/live-beta
- group: start
  title: ''
  type: Login
  url: https://app.import.io
- group: company
  title: ''
  type: Blog
  url: https://www.import.io/blog
- group: other
  title: ''
  type: Data Extraction
  url: https://www.import.io/data-extraction
- group: other
  title: ''
  type: Web Scraping as a Service
  url: https://www.import.io/web-scraping-as-a-service
- group: agent
  title: ''
  type: LlmsText
  url: https://api.docs.import.io/llms.txt
created: '2026-03-26'
description: Import.io is an AI-native web data extraction and integration platform trusted by enterprises to turn the web into structured, actionable intelligence. It manages extraction, transformation, delivery, and compliance end-to-end with adaptive intelligence that automatically handles website changes.
finops:
- has_sources: false
  method: generated
  name: Import Io Finops
  primary_unit: request
  service_category: API
  slug: import-io-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/import-io.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.import.io over HTTP.
  name: Import.io MCP Server
  slug: import-io
modified: '2026-05-19'
name: Import.io
nav: Providers
network: true
overview: 'Import.io publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Schedule.import.io API. Tagged areas include Data Aggregation, Data Extraction, Data Integration, Pricing Intelligence, and Web Scraping.


  The Import.io catalog on APIs.io includes 1 Spectral governance ruleset.


  Import.io''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Import Io Plans Pricing
  plan_count: 3
  slug: import-io-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Import Io Rate Limits
  slug: import-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Import.io API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: import-io-rules
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 25.0
    contract_governance: 13.6
    contract_quality: 46.0
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 14.3
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/import-io/import-io-2026-06-20T183259.png
security:
- kind: authentication
  name: Import Io Authentication
  slug: import-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Import Io Domain Security
  slug: import-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Import Io Vulnerability Disclosure
  slug: import-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: import-io
tags:
- Data Aggregation
- Data Extraction
- Data Integration
- Pricing Intelligence
- Web Scraping
website: https://www.import.io
---
