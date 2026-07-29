---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Import Io Agentic Access
  operation_count: 22
  slug: import-io-agentic-access
  summary_line: 22 operations · 8 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Retrieve crawl run executions and their result files.
  name: Import.io Crawlrun API
  slug: import-io-crawlrun-api
- description: Create, configure, run, and manage web data extractors.
  name: Import.io Extractor API
  slug: import-io-extractor-api
- description: Manage reports built on top of extractors.
  name: Import.io Report API
  slug: import-io-report-api
- description: Retrieve report run executions and their result files.
  name: Import.io ReportRun API
  slug: import-io-reportrun-api
- description: Information about the authenticated user and their subscription.
  name: Import.io User API
  slug: import-io-user-api
artifact_total: 12
collections:
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
  band: developing
  composite: 44.2
  delta: -2.2
  facets:
    commercial_clarity: 63.2
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
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
