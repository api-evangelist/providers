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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Cloudmersive Agentic Access
  operation_count: 13
  slug: cloudmersive-agentic-access
  summary_line: 13 operations · 12 acting
api_count: 1
apis:
- baseURL: https://localhost
  baseurl_source: spec
  description: The Scan API from Cloudmersive — 3 operation(s) for scan.
  name: Cloudmersive Scan API
  slug: cloudmersive-scan-api
- baseURL: https://localhost
  baseurl_source: spec
  description: The ScanCloudStorage API from Cloudmersive — 10 operation(s) for scancloudstorage.
  name: Cloudmersive ScanCloudStorage API
  slug: cloudmersive-scancloudstorage-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: virusapi Scan API
  slug: open-cloudmersive-scan-api
- collection_type: open
  name: virusapi Scan ScanCloudStorage API
  slug: open-cloudmersive-scancloudstorage-api
- collection_type: open
  name: virusapi
  slug: open-cloudmersive-virus-scan
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudmersive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudmersive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudmersive-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cloudmersive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudmersive
- group: company
  title: ''
  type: Website
  url: https://cloudmersive.com/
- group: start
  title: ''
  type: Portal
  url: https://cloudmersive.com/developer
- group: start
  title: ''
  type: Console
  url: https://api-console.cloudmersive.com/swagger/index.html
- group: docs
  title: ''
  type: OpenAPI Index
  url: https://api.cloudmersive.com/openapi.asp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudmersive.com/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudmersive-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudmersive-rules.yml
created: '2024-11-13'
description: Cloudmersive provides a portfolio of utility APIs covering virus and malware scanning, document conversion, OCR, image recognition, NLP, validation, security threat detection (spam, phishing, fraud, DLP, CDR), speech, video, barcode, currency, and data integration. Each API is documented with a Swagger 2.0 / OpenAPI specification, has SDKs in multiple languages, and is consumable on api.cloudmersive.com behind an API key (`Apikey` header).
finops:
- name: Cloudmersive Finops
  service_category: Developer Tools / API
  slug: cloudmersive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudmersive.png
json_structures:
- name: Cloudmersive Structure
  property_count: 0
  slug: cloudmersive-structure
jsonld:
- class_count: 0
  name: Cloudmersive Context
  property_count: 6
  slug: cloudmersive-context
layout: provider
modified: '2026-05-19'
name: Cloudmersive
nav: Providers
network: true
overview: 'Cloudmersive publishes 2 APIs on the [APIs.io](https://apis.io/) network: Scan API and ScanCloudStorage API. Tagged areas include Barcodes, Conversions, Documents, Image Recognition, and Natural-Language.


  The Cloudmersive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudmersive''s developer surface includes authentication, developer portal, developer console, and 9 more developer resources.'
plans:
- name: Cloudmersive Plans Pricing
  plan_count: 8
  slug: cloudmersive-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 10
  name: Cloudmersive Rate Limits
  slug: cloudmersive-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Cloudmersive API Rules
  rule_count: 8
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 3
  slug: cloudmersive-rules
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 45.5
    contract_quality: 48.3
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 10.5
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudmersive/refs/heads/main/screenshots/cloudmersive-2026-06-20T174612.png
security:
- kind: authentication
  name: Cloudmersive Authentication
  slug: cloudmersive-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudmersive Domain Security
  slug: cloudmersive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudmersive
tags:
- Barcodes
- Conversions
- Documents
- Image Recognition
- Natural-Language
- OCR
- Processing
- Validation
- Virus Scanning
website: https://cloudmersive.com/
---
