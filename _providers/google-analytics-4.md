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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Analytics 4 Agentic Access
  operation_count: 8
  slug: google-analytics-4-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 2
apis:
- description: The Measurement Protocol for Google Analytics 4 allows developers to send events directly to Google Analytics servers for web and app streams.
  name: Google Analytics Measurement Protocol
  slug: google-analytics-measurement-protocol
- description: The V1beta API from Google Analytics 4 — 8 operation(s) for v1beta.
  name: Google Analytics 4 V1beta API
  slug: google-analytics-4-v1beta-api
artifact_total: 11
collections:
- collection_type: open
  name: Google Analytics Data API
  slug: open-google-analytics-4
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-analytics-4-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-analytics-4-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-analytics-4-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-analytics-4-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-analytics-4-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/googleanalytics4
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/analytics
- group: start
  title: ''
  type: Console
  url: https://analytics.google.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/analytics/devguides/reporting/data/v1/basics#authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/analytics/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.google.com/analytics
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/analytics/devguides/reporting/data/v1/client-libraries
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://marketingplatform.google.com/about/analytics/compare/
created: '2024-01-01'
description: Google Analytics 4 (GA4) is the latest generation of Analytics that collects event-based data from websites and apps. It provides intelligent insights and predictive analytics powered by machine learning.
finops:
- name: Google Analytics 4 Finops
  service_category: API
  slug: google-analytics-4-finops
image: https://www.gstatic.com/analytics-suite/header/suite/v2/ic_analytics.svg
layout: provider
modified: '2026-04-28'
name: Google Analytics 4
nav: Providers
network: true
overview: 'Google Analytics 4 publishes 1 API on the [APIs.io](https://apis.io/) network: V1beta API. Tagged areas include Analytics, Data Collection, Marketing, Measurement, and Mobile Analytics.


  Google Analytics 4''s developer surface includes authentication, developer portal, developer console, support, pricing, and 11 more developer resources.'
plans:
- name: Google Analytics 4 Plans Pricing
  plan_count: 3
  slug: google-analytics-4-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Google Analytics 4 Rate Limits
  slug: google-analytics-4-rate-limits
scopes:
- name: Google Analytics 4 Scopes
  scope_count: 2
  slug: google-analytics-4-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 48.1
  delta: -2.4
  facets:
    commercial_clarity: 71.1
    contract_quality: 51.3
    developer_ergonomics: 37.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 50.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-analytics-4/refs/heads/main/screenshots/google-analytics-4-2026-06-20T182011.png
security:
- kind: authentication
  name: Google Analytics 4 Authentication
  slug: google-analytics-4-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Analytics 4 Domain Security
  slug: google-analytics-4-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Analytics 4 Vulnerability Disclosure
  slug: google-analytics-4-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-analytics-4
tags:
- Analytics
- Data Collection
- Marketing
- Measurement
- Mobile Analytics
- Reporting
- Web Analytics
website: https://developers.google.com/analytics
---
