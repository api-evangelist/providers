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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Zamzar Agentic Access
  operation_count: 17
  slug: zamzar-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 6
apis:
- description: View account and plan information
  name: Zamzar Account API
  slug: zamzar-account-api
- description: Create, retrieve or delete files
  name: Zamzar Files API
  slug: zamzar-files-api
- description: List supported source and target formats
  name: Zamzar Formats API
  slug: zamzar-formats-api
- description: Import files from an external URL, (S)FTP server or Amazon S3 bucket
  name: Zamzar Imports API
  slug: zamzar-imports-api
- description: Start a new conversion job plus related operations
  name: Zamzar Jobs API
  slug: zamzar-jobs-api
- description: Get started with the Zamzar API
  name: Zamzar Welcome API
  slug: zamzar-welcome-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zamzar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zamzar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zamzar-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.zamzar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zamzar.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zamzar
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zamzar
- group: company
  title: ''
  type: Blog
  url: https://blog.zamzar.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.zamzar.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.zamzarstatus.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/zamzar
- group: commercial
  title: ''
  type: Plans
  url: plans/zamzar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zamzar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zamzar-finops.yml
created: '2026-06-13'
description: Zamzar is an online file conversion platform with a REST API for converting files between 100+ formats including documents, videos, audio, images, and CAD files. The API supports over 1,100 distinct format conversions processed asynchronously using a credit-based billing model. File sources include direct upload, HTTP/FTP/SFTP URLs, and Amazon S3. Both a production environment and a sandbox environment are provided for development.
examples:
- key_count: 4
  name: Get Account
  slug: get-account
- key_count: 4
  name: List Formats
  slug: list-formats
- key_count: 4
  name: Start Import
  slug: start-import
- key_count: 4
  name: Submit Job
  slug: submit-job
- key_count: 4
  name: Upload File
  slug: upload-file
finops:
- name: Zamzar Finops
  service_category: ''
  slug: zamzar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zamzar.png
json_schemas:
- name: Account
  property_count: 3
  slug: account
- name: Failure
  property_count: 2
  slug: failure
- name: File
  property_count: 6
  slug: file
- name: Format
  property_count: 2
  slug: format
- name: Import
  property_count: 8
  slug: import
- name: Job
  property_count: 13
  slug: job
jsonld:
- class_count: 36
  name: Zamzar Context
  property_count: 3
  slug: zamzar-context
layout: provider
modified: '2026-06-13'
name: Zamzar
nav: Providers
network: true
overview: 'Zamzar publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Files API, Formats API, and 3 more. Tagged areas include File Conversion, Documents, Video, Audio, and Images.


  The Zamzar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zamzar''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Zamzar Plans Pricing
  plan_count: 5
  slug: zamzar-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 0
  name: Zamzar Rate Limits
  slug: zamzar-rate-limits
rules:
- name: Zamzar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zamzar-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zamzar/refs/heads/main/screenshots/zamzar-2026-06-20T201800.png
security:
- kind: authentication
  name: Zamzar Authentication
  slug: zamzar-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zamzar Domain Security
  slug: zamzar-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: zamzar
tags:
- File Conversion
- Documents
- Video
- Audio
- Images
- CAD
- REST API
website: https://www.zamzar.com/
---
