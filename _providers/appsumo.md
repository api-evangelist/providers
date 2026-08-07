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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Appsumo Agentic Access
  operation_count: 4
  slug: appsumo-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- description: License management for AppSumo marketplace purchases
  name: AppSumo Licenses API
  slug: appsumo-licenses-api
- description: Partner profile management
  name: AppSumo Profile API
  slug: appsumo-profile-api
artifact_total: 16
collections:
- collection_type: postman
  name: AppSumo Licensing Licenses API
  slug: postman-appsumo-licenses-api
- collection_type: postman
  name: AppSumo Licensing Licenses Profile API
  slug: postman-appsumo-profile-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/appsumo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appsumo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appsumo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appsumo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appsumo
- group: company
  title: ''
  type: Website
  url: https://appsumo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.licensing.appsumo.com/
- group: start
  title: ''
  type: Signup
  url: https://appsumo.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://appsumo.com/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://appsumo.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.licensing.appsumo.com/api/api__getting_started.html
- group: auth
  title: ''
  type: OAuth
  url: https://docs.licensing.appsumo.com/faq/faq__oauth.html
- group: design
  title: ''
  type: Webhooks
  url: https://docs.licensing.appsumo.com/webhook/webhook__getting_started.html
- group: start
  title: ''
  type: GettingStarted
  url: https://appsumooriginals.helpscoutdocs.com/article/889-api-access-for-developers
- group: operate
  title: ''
  type: Support
  url: https://appsumo.com/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appsumo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appsumo.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://blog.appsumo.com/
- group: company
  title: ''
  type: PartnerProgram
  url: https://appsumo.com/partners/
- group: other
  title: ''
  type: Affiliate
  url: https://appsumo.com/affiliate/
- group: other
  title: ''
  type: X
  url: https://twitter.com/appsumo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appsumo
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AppSumo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/appsumo
created: '2026-03-24'
description: AppSumo Licensing API Documentation - v2.
examples:
- key_count: 7
  name: License Example
  slug: license-example
finops:
- name: Appsumo Finops
  service_category: API
  slug: appsumo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appsumo.png
json_schemas:
- name: License
  property_count: 7
  slug: license
json_structures:
- name: License Structure
  property_count: 0
  slug: license-structure
jsonld:
- class_count: 10
  name: Appsumo Context
  property_count: 0
  slug: appsumo-context
layout: provider
modified: '2026-05-19'
name: AppSumo
nav: Providers
network: true
overview: 'AppSumo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Licenses API and Profile API. Tagged areas include Marketplace, SaaS, and Software Deals.


  The AppSumo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AppSumo''s developer surface includes authentication, documentation, signup flow, pricing, getting-started guide, support, engineering blog, and 17 more developer resources.'
plans:
- name: Appsumo Plans Pricing
  plan_count: 3
  slug: appsumo-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 5
  name: Appsumo Rate Limits
  slug: appsumo-rate-limits
rules:
- name: AppSumo API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: appsumo-jsonschema-spectral-rules
- name: AppSumo API Rules
  rule_count: 21
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 12
  slug: appsumo-spectral-rules
score:
  band: strong
  composite: 61.6
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 77.0
    developer_ergonomics: 41.3
    discoverability: 44.4
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appsumo/refs/heads/main/screenshots/appsumo-2026-06-20T172331.png
security:
- kind: authentication
  name: Appsumo Authentication
  slug: appsumo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appsumo Domain Security
  slug: appsumo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: appsumo
tags:
- Marketplace
- SaaS
- Software Deals
website: https://appsumo.com/
---
