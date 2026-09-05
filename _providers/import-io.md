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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
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
  description: Retrieve crawl run executions and their result files.
  name: Import.io Crawlrun API
  slug: import-io-crawlrun-api
- baseURL: https://api.import.io
  baseurl_source: declared
  description: Create, configure, run, and manage web data extractors.
  name: Import.io Extractor API
  slug: import-io-extractor-api
- baseURL: https://api.import.io
  baseurl_source: declared
  description: Manage reports built on top of extractors.
  name: Import.io Report API
  slug: import-io-report-api
- baseURL: https://api.import.io
  baseurl_source: declared
  description: Retrieve report run executions and their result files.
  name: Import.io ReportRun API
  slug: import-io-reportrun-api
- baseURL: https://api.import.io
  baseurl_source: declared
  description: Information about the authenticated user and their subscription.
  name: Import.io User API
  slug: import-io-user-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/import-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/import-io-domain-security.yml
- group: auth
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
- name: Import Io Finops
  service_category: API
  slug: import-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/import-io.png
layout: provider
modified: '2026-05-19'
name: Import.io
nav: Providers
network: true
overview: 'Import.io publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Crawlrun API, Extractor API, Report API, and 2 more. Tagged areas include Data Aggregation, Data Extraction, Data Integration, Pricing Intelligence, and Web Scraping.


  Import.io''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Import Io Plans Pricing
  plan_count: 3
  slug: import-io-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Import Io Rate Limits
  slug: import-io-rate-limits
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 54.1
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/import-io/refs/heads/main/screenshots/import-io-2026-06-20T183259.png
security:
- kind: authentication
  name: Import Io Authentication
  slug: import-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Import Io Domain Security
  slug: import-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: import-io
tags:
- Data Aggregation
- Data Extraction
- Data Integration
- Pricing Intelligence
- Web Scraping
website: https://www.import.io
---
