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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Western Digital Agentic Access
  operation_count: 16
  slug: western-digital-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 7
apis:
- description: OAuth 2.0 authorization and token operations.
  name: western-digital Authentication API
  slug: western-digital-authentication-api
- description: Retrieve dynamic service endpoint configuration.
  name: western-digital Configuration API
  slug: western-digital-configuration-api
- description: Device registration and discovery.
  name: western-digital Device API
  slug: western-digital-device-api
- description: File and folder CRUD operations.
  name: western-digital Files API
  slug: western-digital-files-api
- description: Search files by parent directory.
  name: western-digital Search API
  slug: western-digital-search-api
- description: Create and manage file shares.
  name: western-digital Sharing API
  slug: western-digital-sharing-api
- description: User account information.
  name: western-digital User API
  slug: western-digital-user-api
artifact_total: 22
collections:
- collection_type: open
  name: WD My Cloud Home API
  slug: open-western-digital-my-cloud-home
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/western-digital-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-digital-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/western-digital-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.westerndigital.com
- group: start
  title: ''
  type: Portal
  url: https://developer.westerndigital.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.westerndigital.com/develop/wd-my-cloud-home/
- group: build
  title: ''
  type: SDKs
  url: https://developer.westerndigital.com/develop/wd/sdk.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westerndigital.com/legal/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westerndigital.com/legal/terms-of-use
- group: build
  title: ''
  type: GitHub
  url: https://github.com/westerndigitalcorporation
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/western-digital
- group: company
  title: ''
  type: Blog
  url: https://blog.westerndigital.com/feed/
description: Western Digital is a global leader in data infrastructure, providing storage solutions including hard disk drives, solid state drives, flash memory, and data center systems. Their developer program exposes the WD My Cloud Home REST API enabling third-party applications to manage files, folders, thumbnails, shares, and user accounts stored on WD My Cloud Home devices.
examples:
- key_count: 2
  name: Western Digital Create Share Example
  slug: western-digital-create-share-example
- key_count: 2
  name: Western Digital List Files Example
  slug: western-digital-list-files-example
finops:
- name: Western Digital Finops
  service_category: API
  slug: western-digital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western-digital.png
json_schemas:
- name: Device
  property_count: 9
  slug: western-digital-device
- name: File Item
  property_count: 9
  slug: western-digital-file
json_structures:
- name: Western Digital File Structure
  property_count: 0
  slug: western-digital-file-structure
jsonld:
- class_count: 0
  name: Western Digital Context
  property_count: 20
  slug: western-digital-context
layout: provider
modified: '2026-05-19'
name: western-digital
nav: Providers
network: true
overview: 'western-digital publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Configuration API, Device API, and 4 more. Tagged areas include Fortune 500.


  The western-digital catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  western-digital''s developer surface includes authentication, developer portal, documentation, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Western Digital Plans Pricing
  plan_count: 3
  slug: western-digital-plans-pricing
press:
- date: '2026-05-25'
  title: We Drive Certainty in the AI Era | Brand Evolution
  url: https://www.westerndigital.com/company/campaign/we-drive
- date: '2026-05-25'
  title: Western Digital Accelerates Storage Innovation for AI Era
  url: https://www.westerndigital.com/company/newsroom/press-releases/2026/2026-02-03-western-digital-accelerates-storage-innovation-for-ai-era
- date: '2026-05-25'
  title: Western Digital Doubles Down On AI Data Centers And ...
  url: https://finance.yahoo.com/news/western-digital-doubles-down-ai-070806616.html
- date: '2026-05-25'
  title: Western Digital Unveiled Go-Forward Strategy at Investor ...
  url: https://investor.wdc.com/news-releases/news-release-details/western-digital-unveiled-go-forward-strategy-investor-day-2025
- date: '2026-05-25'
  title: Western Digital forecasts quarterly revenue above ...
  url: https://www.reuters.com/business/western-digital-forecasts-quarterly-revenue-above-estimates-ai-storage-demand-2026-04-30/
random_paper: 115
rate_limits:
- limit_count: 5
  name: Western Digital Rate Limits
  slug: western-digital-rate-limits
rules:
- name: western-digital API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: western-digital-jsonschema-spectral-rules
- name: western-digital API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: western-digital-rules
score:
  band: developing
  composite: 46.3
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 67.5
    developer_ergonomics: 37.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/western-digital/refs/heads/main/screenshots/western-digital-2026-06-20T201446.png
security:
- kind: authentication
  name: Western Digital Authentication
  slug: western-digital-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Western Digital Domain Security
  slug: western-digital-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western-digital
tags:
- Fortune 500
website: https://www.westerndigital.com
---
