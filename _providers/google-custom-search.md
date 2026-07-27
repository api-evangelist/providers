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
  name: Google Custom Search Agentic Access
  operation_count: 2
  slug: google-custom-search-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The Customsearch API from Google Custom Search — 2 operation(s) for customsearch.
  name: Google Custom Search Customsearch API
  slug: google-custom-search-customsearch-api
artifact_total: 12
collections:
- collection_type: open
  name: Google Custom Search JSON API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-custom-search-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-custom-search-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-custom-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-custom-search-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/custom-search
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/custom-search/v1/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/custom-search/v1/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/custom-search/v1/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/custom-search/v1/overview#pricing
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
  url: https://developers.google.com/custom-search/v1/overview#support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Custom Search JSON API allows programmatic searches over a website or collection of websites. It returns metadata about the search performed, metadata about the search engine used, and the search results including web pages and images.
finops:
- name: Google Custom Search Finops
  service_category: API
  slug: google-custom-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-custom-search.png
json_schemas:
- name: Google Custom Search Result
  property_count: 14
  slug: SearchResult
jsonld:
- class_count: 14
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Custom Search
nav: Providers
network: true
overview: 'Google Custom Search publishes 1 API on the [APIs.io](https://apis.io/) network: Customsearch API. Tagged areas include Custom Search, Google, Image Search, Search, and Web Search.


  The Google Custom Search catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Custom Search''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 8 more developer resources.'
plans:
- name: Google Custom Search Plans Pricing
  plan_count: 3
  slug: google-custom-search-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Google Custom Search Rate Limits
  slug: google-custom-search-rate-limits
rules:
- name: Google Custom Search API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-custom-search-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.4
  delta: 4.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.0
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 47.4
  previous_composite: 59.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-custom-search/refs/heads/main/screenshots/google-custom-search-2026-06-20T182152.png
security:
- kind: authentication
  name: Google Custom Search Authentication
  slug: google-custom-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Custom Search Domain Security
  slug: google-custom-search-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Custom Search Vulnerability Disclosure
  slug: google-custom-search-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-custom-search
tags:
- Custom Search
- Google
- Image Search
- Search
- Web Search
website: https://developers.google.com/custom-search
---
