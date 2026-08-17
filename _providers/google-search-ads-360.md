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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Search Ads 360 Agentic Access
  operation_count: 4
  slug: google-search-ads-360-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- description: The Customers API from Google Search Ads 360 Reporting — 3 operation(s) for customers.
  name: Google Search Ads 360 Reporting Customers API
  slug: google-search-ads-360-customers-api
- description: The Google Search Ads 360 Reporting API API from Google Search Ads 360 Reporting — 1 operation(s) for google search ads 360 reporting api.
  name: Google Search Ads 360 Reporting Google Search Ads 360 Reporting API API
  slug: google-search-ads-360-google-search-ads-360-reporting-api-api
artifact_total: 17
collections:
- collection_type: postman
  name: Google Search Ads 360 Reporting Customers API
  slug: postman-google-search-ads-360-customers-api
- collection_type: postman
  name: Google Search Ads 360 Reporting Customers Google Search Ads 360 Reporting API API
  slug: postman-google-search-ads-360-google-search-ads-360-reporting-api-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Search Ads 360 Reporting Customers API
  slug: open-google-search-ads-360-customers-api
- collection_type: open
  name: Google Search Ads 360 Reporting Customers Google Search Ads 360 Reporting API API
  slug: open-google-search-ads-360-google-search-ads-360-reporting-api-api
- collection_type: open
  name: Google Search Ads 360 Reporting API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-search-ads-360-reporting/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-search-ads-360-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-search-ads-360-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-search-ads-360-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-search-ads-360-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-search-ads-360-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/search-ads
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/search-ads/reporting/quickstart/quickstart-guide
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/search-ads
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/search-ads/reporting/quickstart/quickstart-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/search-ads-360/
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
  url: https://developers.google.com/search-ads/reporting/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Search Ads 360 Reporting API enables automated report downloading and programmatic access to search advertising campaign data across multiple search engines. It provides search and streaming methods for querying campaign, ad group, keyword, and conversion data using a SQL-like query language.
finops:
- name: Google Search Ads 360 Finops
  service_category: API
  slug: google-search-ads-360-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-search-ads-360.png
layout: provider
modified: '2026-05-19'
name: Google Search Ads 360 Reporting
nav: Providers
network: true
overview: 'Google Search Ads 360 Reporting publishes 2 APIs on the [APIs.io](https://apis.io/) network: Customers API and Google Search Ads 360 Reporting API API. Tagged areas include Campaign Management, Conversions, Keywords, Reporting, and Search Ads 360.


  The Google Search Ads 360 Reporting catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Search Ads 360 Reporting''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Search Ads 360 Plans Pricing
  plan_count: 3
  slug: google-search-ads-360-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 5
  name: Google Search Ads 360 Rate Limits
  slug: google-search-ads-360-rate-limits
rules:
- name: Google Search Ads 360 Reporting API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-search-ads-360-jsonschema-spectral-rules
scopes:
- name: Google Search Ads 360 Scopes
  scope_count: 1
  slug: google-search-ads-360-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.2
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-search-ads-360/refs/heads/main/screenshots/google-search-ads-360-2026-06-20T182242.png
security:
- kind: authentication
  name: Google Search Ads 360 Authentication
  slug: google-search-ads-360-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Search Ads 360 Domain Security
  slug: google-search-ads-360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Search Ads 360 Vulnerability Disclosure
  slug: google-search-ads-360-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-search-ads-360
tags:
- Campaign Management
- Conversions
- Keywords
- Reporting
- Search Ads 360
- Search Advertising
website: https://developers.google.com/search-ads
---
