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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Pagespeed Agentic Access
  operation_count: 1
  slug: google-pagespeed-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Page performance analysis
  name: Google PageSpeed Analysis API
  slug: google-pagespeed-analysis-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google PageSpeed PageSpeed Insights Analysis API
  slug: postman-google-pagespeed-analysis-api
- collection_type: open
  name: Google PageSpeed PageSpeed Insights API
  slug: open-pagespeed-insights
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-pagespeed/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-pagespeed-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-pagespeed-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-pagespeed-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pagespeed
- group: start
  title: ''
  type: Portal
  url: https://pagespeed.web.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/speed/docs/insights/v5/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/speed/docs/insights
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/speed/docs/insights/v5/get-started#APIKey
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
  url: https://support.google.com/webmasters
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/apis/library/pagespeedonline.googleapis.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-pagespeed-context.jsonld
created: '2026-03-13'
description: Google PageSpeed Insights provides APIs for analyzing the performance of web pages on both mobile and desktop devices, returning performance scores, Core Web Vitals metrics, and actionable optimization recommendations powered by Lighthouse.
finops:
- name: Google Pagespeed Finops
  service_category: API
  slug: google-pagespeed-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-pagespeed.png
json_schemas:
- name: PageSpeed Insights Result
  property_count: 5
  slug: google-pagespeed-result
jsonld:
- class_count: 0
  name: Google Pagespeed Context
  property_count: 3
  slug: google-pagespeed-context
layout: provider
modified: '2026-05-19'
name: Google PageSpeed
nav: Providers
network: true
overview: 'Google PageSpeed publishes 1 API on the [APIs.io](https://apis.io/) network: Analysis API. Tagged areas include Core Web Vitals, Google, Lighthouse, Page Speed, and SEO.


  The Google PageSpeed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google PageSpeed''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, developer console, and 9 more developer resources.'
plans:
- name: Google Pagespeed Plans Pricing
  plan_count: 3
  slug: google-pagespeed-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Google Pagespeed Rate Limits
  slug: google-pagespeed-rate-limits
rules:
- name: Google PageSpeed API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-pagespeed-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.4
  delta: -3.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.2
    developer_ergonomics: 54.3
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-pagespeed/refs/heads/main/screenshots/google-pagespeed-2026-06-20T182219.png
security:
- kind: authentication
  name: Google Pagespeed Authentication
  slug: google-pagespeed-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Google Pagespeed Domain Security
  slug: google-pagespeed-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: google-pagespeed
tags:
- Core Web Vitals
- Google
- Lighthouse
- Page Speed
- SEO
- Web Performance
website: https://pagespeed.web.dev/
---
