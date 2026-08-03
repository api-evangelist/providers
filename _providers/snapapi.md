---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Snapapi Agentic Access
  operation_count: 6
  slug: snapapi-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 6
apis:
- description: The Metadata API from SnapAPI — 1 operation(s) for metadata.
  name: SnapAPI Metadata API
  slug: snapapi-metadata-api
- description: The Pdf API from SnapAPI — 1 operation(s) for pdf.
  name: SnapAPI Pdf API
  slug: snapapi-pdf-api
- description: The Screenshot API from SnapAPI — 1 operation(s) for screenshot.
  name: SnapAPI Screenshot API
  slug: snapapi-screenshot-api
- description: The Signup API from SnapAPI — 1 operation(s) for signup.
  name: SnapAPI Signup API
  slug: snapapi-signup-api
- description: The Text API from SnapAPI — 1 operation(s) for text.
  name: SnapAPI Text API
  slug: snapapi-text-api
- description: The Usage API from SnapAPI — 1 operation(s) for usage.
  name: SnapAPI Usage API
  slug: snapapi-usage-api
artifact_total: 27
collections:
- collection_type: open
  name: SnapAPI
  slug: open-snapapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snapapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snapapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snapapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://snap.michaelcli.com
- group: docs
  title: ''
  type: Documentation
  url: https://snap.michaelcli.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://snap.michaelcli.com/openapi.json
- group: start
  title: ''
  type: Signup
  url: https://snap.michaelcli.com/api/signup
- group: company
  title: ''
  type: Blog
  url: https://snap.michaelcli.com/blog/building-screenshot-api.html
created: '2026-05-27'
description: REST API for website screenshots, metadata extraction, text extraction, and PDF generation. Powered by headless Chromium. Free tier with 50 requests/month, no credit card required. API key issued via self-service signup.
examples:
- key_count: 2
  name: Snapapi Metadata Example
  slug: snapapi-metadata-example
- key_count: 2
  name: Snapapi Pdf Example
  slug: snapapi-pdf-example
- key_count: 2
  name: Snapapi Screenshot Example
  slug: snapapi-screenshot-example
- key_count: 2
  name: Snapapi Signup Example
  slug: snapapi-signup-example
- key_count: 2
  name: Snapapi Text Example
  slug: snapapi-text-example
finops:
- name: Snapapi Finops
  service_category: API
  slug: snapapi-finops
image: https://snap.michaelcli.com/favicon.ico
json_schemas:
- name: SnapAPI Metadata
  property_count: 2
  slug: snapapi-metadata
- name: SnapAPI PDF Request
  property_count: 3
  slug: snapapi-pdf-request
- name: SnapAPI Screenshot Request
  property_count: 5
  slug: snapapi-screenshot-request
- name: SnapAPI Screenshot Response
  property_count: 3
  slug: snapapi-screenshot-response
- name: SnapAPI Text Extraction Response
  property_count: 2
  slug: snapapi-text
- name: SnapAPI Usage
  property_count: 4
  slug: snapapi-usage
jsonld:
- class_count: 0
  name: Snapapi Context
  property_count: 9
  slug: snapapi-context
layout: provider
modified: '2026-05-27'
name: SnapAPI
nav: Providers
network: true
overview: 'SnapAPI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Pdf API, Screenshot API, and 3 more. Tagged areas include Screenshots, Website Screenshots, Metadata Extraction, Text Extraction, and PDF Generation.


  The SnapAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SnapAPI''s developer surface includes authentication, documentation, signup flow, engineering blog, and 4 more developer resources.'
plans:
- name: Snapapi Plans Pricing
  plan_count: 5
  slug: snapapi-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Snapapi Rate Limits
  slug: snapapi-rate-limits
rules:
- name: SnapAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: snapapi-jsonschema-spectral-rules
- name: SnapAPI API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: snapapi-rules
score:
  band: developing
  composite: 48.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.9
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snapapi/refs/heads/main/screenshots/snapapi-2026-06-20T194100.png
security:
- kind: authentication
  name: Snapapi Authentication
  slug: snapapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Snapapi Domain Security
  slug: snapapi-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: snapapi
tags:
- Screenshots
- Website Screenshots
- Metadata Extraction
- Text Extraction
- PDF Generation
- Headless Chromium
- Web Scraping
- Developer Tools
- REST
website: https://snap.michaelcli.com
---
