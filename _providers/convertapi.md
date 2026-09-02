---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 316
  human_in_the_loop: 0
  name: Convertapi Agentic Access
  operation_count: 320
  slug: convertapi-agentic-access
  summary_line: 320 operations · 316 acting
api_count: 1
apis:
- description: File Conversion API call
  name: ConvertAPI Conversion API
  slug: convertapi-conversion-api
- description: ConvertAPI temporary file storage
  name: ConvertAPI File Server API
  slug: convertapi-file-server-api
- description: API User
  name: ConvertAPI User API
  slug: convertapi-user-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Convert Conversion API
  slug: open-convertapi-conversion-api
- collection_type: open
  name: Convert Conversion File Server API
  slug: open-convertapi-file-server-api
- collection_type: open
  name: Convert Conversion User API
  slug: open-convertapi-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/convertapi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/convertapi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/convertapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/convertapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.convertapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.convertapi.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ConvertAPI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/convertapi
- group: company
  title: ''
  type: Blog
  url: https://www.convertapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.convertapi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.convertapi.com/
- group: other
  title: ''
  type: X
  url: https://x.com/ConvertAPI_
- group: commercial
  title: ''
  type: Plans
  url: plans/convertapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/convertapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/convertapi-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.convertapi.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://help.convertapi.com/
created: '2026-06-13'
description: ConvertAPI is a file conversion REST API supporting over 200 file format conversions including PDF, Microsoft Office documents (Word, Excel, PowerPoint), images, audio, video, and e-book formats. The API provides batch processing via Conversion Workflows, asynchronous conversion, a Virtual File Server for managing files, and SDKs across 12 programming languages. The platform is ISO 27001 certified and HIPAA and GDPR compliant with a 99.95% uptime guarantee.
examples:
- key_count: 12
  name: Convertapi Examples
  slug: convertapi-examples
- key_count: 4
  name: Docx To Pdf Example
  slug: docx-to-pdf-example
finops:
- name: Convertapi Finops
  service_category: ''
  slug: convertapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/convertapi.png
json_schemas:
- name: ConversionRequest
  property_count: 324
  slug: conversion-request
- name: ConversionResponse
  property_count: 15
  slug: conversion-response
- name: error
  property_count: 2
  slug: error
- name: fileId
  property_count: 0
  slug: fileId
jsonld:
- class_count: 0
  name: Convertapi Context
  property_count: 0
  slug: convertapi
layout: provider
modified: '2026-06-13'
name: ConvertAPI
nav: Providers
network: true
overview: 'ConvertAPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Conversion API, File Server API, and User API. Tagged areas include File Conversion, PDF, Documents, Image, and Audio.


  The ConvertAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ConvertAPI''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, and 11 more developer resources.'
plans:
- name: Convertapi Plans Pricing
  plan_count: 5
  slug: convertapi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Convertapi Rate Limits
  slug: convertapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ConvertAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: convertapi-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 42.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 53.7
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/convertapi/refs/heads/main/screenshots/convertapi-2026-06-20T174957.png
security:
- kind: authentication
  name: Convertapi Authentication
  slug: convertapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Convertapi Domain Security
  slug: convertapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Convertapi Trust Center
  slug: convertapi-trust-center
  summary_line: ISO 27001
slug: convertapi
tags:
- File Conversion
- PDF
- Documents
- Image
- Audio
- Video
- Ebooks
- Office Documents
- Batch Processing
website: https://www.convertapi.com/
---
