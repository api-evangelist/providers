---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Fonts Agentic Access
  operation_count: 1
  slug: google-fonts-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Retrieve font family metadata
  name: Google Fonts Developer Fonts API
  slug: google-fonts-fonts-api
artifact_total: 11
collections:
- collection_type: open
  name: Google Fonts Developer API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-fonts-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-fonts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-fonts-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-fonts
- group: start
  title: ''
  type: Portal
  url: https://fonts.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/fonts/docs/getting_started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/fonts
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/fonts/docs/developer_api#APIKey
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/fonts/docs/support
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/json-ld/google-fonts.jsonld
created: '2026-03-13'
description: The Google Fonts Developer API provides programmatic access to the metadata for all font families served by Google Fonts. Developers can query for available font families, retrieve details about variants, subsets, and categories, access font file URLs, and work with variable font axis metadata. The API supports sorting and filtering to help applications discover and integrate web fonts.
finops:
- name: Google Fonts Finops
  service_category: API
  slug: google-fonts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-fonts.png
json_schemas:
- name: Google Fonts Developer API Schema
  property_count: 0
  slug: google-fonts
jsonld:
- class_count: 0
  name: Google Fonts Context
  property_count: 9
  slug: google-fonts
layout: provider
modified: '2026-05-19'
name: Google Fonts Developer
nav: Providers
network: true
overview: 'Google Fonts Developer publishes 1 API on the [APIs.io](https://apis.io/) network: Fonts API. Tagged areas include CSS, Design, Fonts, Google Fonts, and Typography.


  The Google Fonts Developer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Fonts Developer''s developer surface includes developer portal, getting-started guide, documentation, authentication, support, and 9 more developer resources.'
plans:
- name: Google Fonts Plans Pricing
  plan_count: 3
  slug: google-fonts-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Google Fonts Rate Limits
  slug: google-fonts-rate-limits
rules:
- name: Google Fonts Developer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: google-fonts-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.8
  delta: 4.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 56.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/screenshots/google-fonts-2026-06-20T182204.png
security:
- kind: domain-security
  name: Google Fonts Domain Security
  slug: google-fonts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Fonts Vulnerability Disclosure
  slug: google-fonts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-fonts
tags:
- CSS
- Design
- Fonts
- Google Fonts
- Typography
- Web Fonts
website: https://fonts.google.com/
---
