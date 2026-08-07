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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Abstractapi Phone Agentic Access
  operation_count: 1
  slug: abstractapi-phone-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Validate and verify a phone number and return carrier, line type, and location.
  name: Abstract API Phone Validation Phone Validation API
  slug: abstractapi-phone-phone-validation-api
artifact_total: 8
collections:
- collection_type: open
  name: Abstract API Phone Validation
  slug: open-abstractapi-phone
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abstractapi-phone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abstractapi-phone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abstractapi-phone-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abstractapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abstract-api
- group: company
  title: ''
  type: Website
  url: https://www.abstractapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.abstractapi.com/api/phone-validation-api
- group: commercial
  title: ''
  type: Plans
  url: plans/abstractapi-phone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abstractapi-phone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/abstractapi-phone-finops.yml
created: '2026-07-12'
description: Abstract API's Phone Number Validation & Verification API validates and verifies a phone number in a single REST request. Given a number (ideally in E.164 format) it returns whether the number is valid, its local and international formats, the country, the registered location, the line type (mobile, landline, VoIP, and more), and the carrier - useful for form validation, lead scoring, fraud prevention, and cleaning phone data. The endpoint is a single authenticated GET call with the API key passed as a query parameter, and Abstract offers a free tier alongside paid plans. Phone Validation is one product in the broader Abstract API suite, which also includes email validation, IP geolocation, company enrichment, and other data APIs; each product has its own host and its own API key.
finops:
- name: Abstractapi Phone Finops
  service_category: Data Validation and Enrichment
  slug: abstractapi-phone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abstractapi-phone.png
layout: provider
modified: '2026-07-12'
name: Abstract API Phone Validation
nav: Providers
network: true
overview: 'Abstract API Phone Validation publishes 1 API on the [APIs.io](https://apis.io/) network: Phone Validation API. Tagged areas include Number Verification, Phone Validation, Phone Number, Phone Number Lookup, and Verification.


  Abstract API Phone Validation''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Abstractapi Phone Plans Pricing
  plan_count: 3
  slug: abstractapi-phone-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 2
  name: Abstractapi Phone Rate Limits
  slug: abstractapi-phone-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.3
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abstractapi-phone/refs/heads/main/screenshots/abstractapi-phone-2026-07-25T181408.png
security:
- kind: authentication
  name: Abstractapi Phone Authentication
  slug: abstractapi-phone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Abstractapi Phone Domain Security
  slug: abstractapi-phone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abstractapi-phone
tags:
- Number Verification
- Phone Validation
- Phone Number
- Phone Number Lookup
- Verification
- Carrier Lookup
- Line Type
- Data Validation
website: https://www.abstractapi.com
---
