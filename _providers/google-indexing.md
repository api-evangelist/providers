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
- acting_count: 1
  human_in_the_loop: 0
  name: Google Indexing Agentic Access
  operation_count: 2
  slug: google-indexing-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The urlNotifications API from Google Indexing — 1 operation(s) for urlnotifications.
  name: Google Indexing urlNotifications API
  slug: google-indexing-urlnotifications-api
- description: The urlNotifications:publish API from Google Indexing — 1 operation(s) for urlnotifications:publish.
  name: Google Indexing urlNotifications:publish API
  slug: google-indexing-urlnotifications-publish-api
artifact_total: 15
collections:
- collection_type: open
  name: Google Indexing API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-indexing-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-indexing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-indexing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-indexing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-indexing-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/search/apis/indexing-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/search/apis/indexing-api/v3/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/search/apis/indexing-api
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/search/apis/indexing-api/v3/prereqs
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
  url: https://developers.google.com/search/apis/indexing-api/v3/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/context.jsonld
created: '2026-03-13'
description: The Google Indexing API allows site owners to directly notify Google when pages are added or removed. It enables requesting crawling for updated content and notifying of page removals, leading to fresher content in search results. Primarily intended for sites with job postings or livestream structured data.
finops:
- name: Google Indexing Finops
  service_category: API
  slug: google-indexing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-indexing.png
json_schemas:
- name: Google Indexing URL Notification
  property_count: 3
  slug: UrlNotification
jsonld:
- class_count: 13
  name: context Context
  property_count: 0
  slug: context
layout: provider
modified: '2026-05-19'
name: Google Indexing
nav: Providers
network: true
overview: 'Google Indexing publishes 2 APIs on the [APIs.io](https://apis.io/) network: urlNotifications API and urlNotifications:publish API. Tagged areas include Crawling, Google, Indexing, Search, and SEO.


  The Google Indexing catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Indexing''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, and 9 more developer resources.'
plans:
- name: Google Indexing Plans Pricing
  plan_count: 3
  slug: google-indexing-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Google Indexing Rate Limits
  slug: google-indexing-rate-limits
rules:
- name: Google Indexing API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-indexing-jsonschema-spectral-rules
- name: Google Indexing API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 4
  slug: google-indexing-spectral-rules
scopes:
- name: Google Indexing Scopes
  scope_count: 1
  slug: google-indexing-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 63.2
  delta: 4.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.6
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 47.4
  previous_composite: 58.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-indexing/refs/heads/main/screenshots/google-indexing-2026-06-20T182255.png
security:
- kind: authentication
  name: Google Indexing Authentication
  slug: google-indexing-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Indexing Domain Security
  slug: google-indexing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Indexing Vulnerability Disclosure
  slug: google-indexing-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-indexing
tags:
- Crawling
- Google
- Indexing
- Search
- SEO
- URLs
website: https://developers.google.com/search/apis/indexing-api
---
