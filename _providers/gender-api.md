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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gender Api Agentic Access
  operation_count: 3
  slug: gender-api-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Get API from Gender API — 1 operation(s) for get.
  name: Gender API Get API
  slug: gender-api-get-api
- description: The Get Country Of Origin API from Gender API — 1 operation(s) for get country of origin.
  name: Gender API Get Country Of Origin API
  slug: gender-api-get-country-of-origin-api
- description: The Get Stats API from Gender API — 1 operation(s) for get stats.
  name: Gender API Get Stats API
  slug: gender-api-get-stats-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gender Get API
  slug: open-gender-api-get-api
- collection_type: open
  name: Gender Get Get Country Of Origin API
  slug: open-gender-api-get-country-of-origin-api
- collection_type: open
  name: Gender Get Get Stats API
  slug: open-gender-api-get-stats-api
- collection_type: open
  name: Gender API
  slug: open-gender-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gender-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gender-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gender-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GenderAPI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genderapi
- group: company
  title: ''
  type: Website
  url: https://gender-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://gender-api.com/en/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://gender-api.com/en/pricing
- group: start
  title: ''
  type: Signup
  url: https://gender-api.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://gender-api.com/en/login
- group: operate
  title: ''
  type: Contact
  url: https://gender-api.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gender-api.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gender-api.com/en/privacy
- group: company
  title: ''
  type: Blog
  url: https://gender-api.com/en/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://gender-api.com/llms.txt
created: '2025-01-07'
description: Gender-API is an AI-powered service that determines whether a first name is more likely to be used by males or females, with optional localization by country, IP address, or browser locale. The API returns a gender prediction with an accuracy score and supports multi-name lookups, email parsing, full-name splitting, and country-of-origin queries. Gender-API is delivered as a metered REST API with credit-based subscription plans and integrates with Zapier, Postman, Google Sheets, and HubSpot.
finops:
- name: Gender Api Finops
  service_category: API
  slug: gender-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gender-api.png
layout: provider
modified: '2026-05-19'
name: Gender API
nav: Providers
network: true
overview: 'Gender API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Get API, Get Country Of Origin API, and Get Stats API. Tagged areas include AI, Demographics, Gender, Identity, and Names.


  Gender API''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Gender Api Plans Pricing
  plan_count: 3
  slug: gender-api-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Gender Api Rate Limits
  slug: gender-api-rate-limits
score:
  band: thin
  composite: 34.2
  delta: -6.4
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 53.4
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/gender-api/refs/heads/main/screenshots/gender-api-2026-06-20T181719.png
security:
- kind: authentication
  name: Gender Api Authentication
  slug: gender-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gender Api Domain Security
  slug: gender-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gender-api
tags:
- AI
- Demographics
- Gender
- Identity
- Names
- Personal Data
website: https://gender-api.com/
---
