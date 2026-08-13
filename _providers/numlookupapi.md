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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Numlookupapi Agentic Access
  operation_count: 2
  slug: numlookupapi-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Account quota and usage status.
  name: NumLookupAPI Account API
  slug: numlookupapi-account-api
- description: Phone number validation and lookup.
  name: NumLookupAPI Validation API
  slug: numlookupapi-validation-api
artifact_total: 9
collections:
- collection_type: open
  name: NumLookupAPI
  slug: open-numlookupapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/numlookupapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/numlookupapi-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numlookupapi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everapihq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everapi
- group: company
  title: ''
  type: Website
  url: https://numlookupapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://numlookupapi.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/numlookupapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/numlookupapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/numlookupapi-finops.yml
created: '2026-07-12'
description: NumLookupAPI is a phone number validation and lookup REST API from everapi. A single GET request validates a phone number and returns whether it is valid along with its local and international formats, country prefix, ISO country code and name, geographic location, carrier, and line type (mobile, landline, etc.). It offers a free tier of 100 requests per month, is authenticated with a simple API key, and is used for phone verification, data validation, and caller identity enrichment.
finops:
- name: Numlookupapi Finops
  service_category: Data Enrichment and Validation
  slug: numlookupapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numlookupapi.png
layout: provider
modified: '2026-07-12'
name: NumLookupAPI
nav: Providers
network: true
overview: 'NumLookupAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Validation API. Tagged areas include Number Verification, Phone Validation, Phone Number Lookup, Carrier Lookup, and Line Type.


  NumLookupAPI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Numlookupapi Plans Pricing
  plan_count: 5
  slug: numlookupapi-plans-pricing
random_paper: 116
rate_limits:
- limit_count: 6
  name: Numlookupapi Rate Limits
  slug: numlookupapi-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numlookupapi/refs/heads/main/screenshots/numlookupapi-2026-08-07T185737.png
security:
- kind: authentication
  name: Numlookupapi Authentication
  slug: numlookupapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Numlookupapi Domain Security
  slug: numlookupapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: numlookupapi
tags:
- Number Verification
- Phone Validation
- Phone Number Lookup
- Carrier Lookup
- Line Type
- Verification
- Data Validation
- Caller Identity
website: https://numlookupapi.com
---
